import pandas as pd
from datetime import datetime, timedelta

def init(file_path):
    df = pd.read_csv(file_path)
    columns_to_drop = ["PERSONID", "EMPLOYEEID","LASTNAME","FIRSTNAME","Unnamed: 0"]
    df = df.drop(columns=columns_to_drop)
    df['ACCESSDATE'] = df['ACCESSDATE'].str.slice(stop=19)

    def check_anomaly(row):
        same_card_swipes1 = df[(df['CARDNUMBER'] == row['CARDNUMBER']) & (df['ACCESSDATE'] != row['ACCESSDATE'])]
        same_location = df[(df['CARDNUMBER'] == row['CARDNUMBER']) & (df['LOCATION'] == row['LOCATION']) & (df['ACCESSDATE'] != row['ACCESSDATE'])]
        for i, swipe in same_card_swipes1.iterrows():
            time_difference1 = datetime.strptime(row['ACCESSDATE'], '%Y-%m-%d %H:%M:%S') - datetime.strptime(swipe['ACCESSDATE'], '%Y-%m-%d %H:%M:%S')
            if time_difference1 < timedelta(minutes=10):
                return True, 'Rule 1' 
        for i, swipe in same_location.iterrows():
            time_difference2 = datetime.strptime(row['ACCESSDATE'], '%Y-%m-%d %H:%M:%S') - datetime.strptime(swipe['ACCESSDATE'], '%Y-%m-%d %H:%M:%S')
            if time_difference2 <= pd.Timedelta(minutes=10):
                return True, 'Rule 3'
        same_card_swipes3 = df[(df['CARDNUMBER'] == row['CARDNUMBER']) & (df['LOCATION'] != row['LOCATION'])]
        for i, swipe in same_card_swipes3.iterrows():
            time_difference3 = datetime.strptime(row['ACCESSDATE'], '%Y-%m-%d %H:%M:%S') - datetime.strptime(swipe['ACCESSDATE'], '%Y-%m-%d %H:%M:%S')
            if time_difference3 < timedelta(minutes=10):
                return True, 'Rule 2'
        return False, 'Not Anomaly'

    df[['flagged', 'rule']] = df.apply(lambda row: pd.Series(check_anomaly(row)), axis=1)
    flagged_transactions = df[df['flagged']]
    not_anomaly = df[~df['flagged']]

    return flagged_transactions, not_anomaly

if __name__ == "__main__":
    flagged_transactions, not_anomaly = init()
    flagged_transactions.to_csv('Flagged_transactions.csv', encoding = 'utf-8-sig')
    not_anomaly.to_csv('Not_anomaly.csv', encoding = 'utf-8-sig')
    #print("Flagged Transactions:")
    #print(flagged_transactions)
    #print("Not Anomaly Transactions:")
    #print(not_anomaly)
