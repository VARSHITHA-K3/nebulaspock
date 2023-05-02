import pandas as pd
import statsmodels.api as sm

def predict_next_value(file_path, logValue, iterations, movingAvgValue,
                       seasonalPeriod,month=None, day=None, year=None,
                       start_Date:any=None,end_Date:any=None):
    df = pd.read_csv(file_path, index_col='DATE', parse_dates=True)

    df = df.loc[start_Date:end_Date]
    if month is not None and day is not None and year is not None:
        prev_day = pd.to_datetime(f'{year}-{month}-{day}') - pd.offsets.Day(1)
        df = df.loc[:prev_day]
    model = sm.tsa.statespace.SARIMAX(df['VALUE'], order=(logValue, iterations, movingAvgValue), seasonal_order=(1, 1, 0, seasonalPeriod))
    result = model.fit()
    if month is not None and day is not None and year is not None:
        next_datetime = pd.to_datetime(f'{year}-{month}-{day}') + pd.offsets.Day(1)
    else:
        next_datetime = df.index[-1] + pd.offsets.Day(1)
    next_value = result.forecast(steps=1, index=[next_datetime])[0]

    return next_value