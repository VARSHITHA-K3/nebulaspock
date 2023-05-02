import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import IsolationForest



def isolation(file_Path=""):
    return anomalyIsolation(pd.read_csv(file_Path))


def anomalyIsolation(flagged_transactions_df:pd.DataFrame):
    
    # Create a new dataframe using flagged_transactions_np
    #flagged_transactions_df = pd.DataFrame(flagged_transactions_np, columns=flagged_transactions.columns)
    
    
    columns_to_drop = ["flagged", "rule"]
    df = flagged_transactions_df
    df = df.drop(columns=columns_to_drop) # Drop the columns
    df['ACCESSDATE'] = df['ACCESSDATE'].str.replace(r'[^0-9]+', '')

    X = df[['ID', 'ACCESSDATE', 'LOCATION', 'CARDNUMBER']]
    time_diff = df.groupby(['ID', 'ACCESSDATE', 'LOCATION', 'CARDNUMBER'])['ACCESSDATE'].diff().fillna(0) # type: ignore
    time_diff_threshold = 1800
    time_diff = np.where(time_diff > time_diff_threshold, 1, 0)

    X = np.concatenate([X, time_diff.reshape(-1, 1)], axis=1)
    scaler = StandardScaler()
    X_norm = scaler.fit_transform(X)
    model = IsolationForest(n_estimators=100, contamination=0.01)
    model.fit(X_norm)

    y_pred = model.predict(X_norm)
    anomalies = df[y_pred == -1]
    y_true = np.ones(len(df))
    y_true[y_pred == -1] = -1

    conf_mat = confusion_matrix(y_true, y_pred)
    accuracy = accuracy_score(y_true, y_pred)
    #print("Confusion Matrix:")
    #print(conf_mat)
    #print("Accuracy: {:.2f}%".format(accuracy*100))

    # Printing which are not anomalies
    X = df[['ID','LOCATION', 'ACCESSDATE', 'CARDNUMBER']]
    scaler = StandardScaler()
    X_norm = scaler.fit_transform(X)
    model = IsolationForest(n_estimators=100, max_samples='auto', contamination=float(0.01), random_state=42)
    model.fit(X_norm)
    y_pred = model.predict(X_norm)
    normal_indices = np.where(y_pred == 1)[0]
    normal_df = df.iloc[normal_indices]

    return anomalies, normal_df

    ####################################################################################
def noneAnomalyIsolation(not_anomaly:pd.DataFrame):
    not_anomaly = not_anomaly.drop(columns=["flagged", "rule"]) # Drop the columns
    not_anomaly['ACCESSDATE'] = not_anomaly['ACCESSDATE'].str.replace(r'[^0-9]+', '')

    X = not_anomaly[['ID', 'ACCESSDATE', 'LOCATION', 'CARDNUMBER']]
    time_diff = not_anomaly.groupby(['ID', 'ACCESSDATE', 'LOCATION', 'CARDNUMBER'])['ACCESSDATE'].diff().fillna(0) # type: ignore
    time_diff_threshold = 1800
    time_diff = np.where(time_diff > time_diff_threshold, 1, 0)

    X = np.concatenate([X, time_diff.reshape(-1, 1)], axis=1)
    scaler = StandardScaler()
    X_norm = scaler.fit_transform(X)
    model = IsolationForest(n_estimators=100, contamination=0.01)
    model.fit(X_norm)

    y_pred = model.predict(X_norm)
    anomalies1 = not_anomaly[y_pred == -1]
    y_true = np.ones(len(not_anomaly))
    y_true[y_pred == -1] = -1

    conf_mat = confusion_matrix(y_true, y_pred)
    accuracy = accuracy_score(y_true, y_pred)
    #print("Confusion Matrix:")
    #print(conf_mat)
    #print("Accuracy: {:.2f}%".format(accuracy*100))

    X = not_anomaly[['ID','LOCATION', 'ACCESSDATE', 'CARDNUMBER']]
    scaler = StandardScaler()
    X_norm = scaler.fit_transform(X)
    model = IsolationForest(n_estimators=100, max_samples='auto', contamination=float(0.01), random_state=42)
    model.fit(X_norm)
    y_pred = model.predict(X_norm)
    normal_indices = np.where(y_pred == 1)[0]
    normal_df1 = not_anomaly.iloc[normal_indices]

    return anomalies1, normal_df1

