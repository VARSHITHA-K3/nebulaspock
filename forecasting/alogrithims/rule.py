import pandas as pd
import statsmodels.api as sm
import forecasting.models.predictionmodel as  predictionmodel

def ruleExecute(dataModel:predictionmodel.DataModel,file_path:str,startdate:str,enddate:str):
   
    #return dataModel,file_path,startdate,enddate
   return predict_val(file_path=file_path,
                       logValue=dataModel.logValue,
                       iterations=dataModel.iterations,
                       movingAvgValue=dataModel.movingAvgValue,
                       seasonalPeriod = dataModel.seasonalPeriod,
                       month = dataModel.month,
                       day=dataModel.day,
                       year = dataModel.year,
                      startDate = startdate,
                      endDate = enddate)

def predict_val(file_path, 
                       logValue, 
                       iterations, 
                       movingAvgValue,
                       seasonalPeriod,
                       month, 
                       day, 
                       year,
                       startDate,
                       endDate):
    print(startDate,endDate)
    df = pd.read_csv(file_path, index_col='DATE', parse_dates=True)

    df = df.loc[startDate:endDate]
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