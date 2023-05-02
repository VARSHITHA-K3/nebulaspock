

from anomalies.algorithms.rule import init
import forecasting.alogrithims.rule as predict_next_value
import forecasting.models.predictionmodel as  predictionmodel

def prediction_response(request,model:predictionmodel,
            file_path:any=None,start_Date:any=None,end_Date:any=None):
    
    next_value:any=None
    try:
          next_value = predict_next_value(file_path, 
                                          model.logValue,
                                          model.iterations,
                                          model.movingAvgValue, 
                                          model.seasonalPeriod,
                                          month=model.month,
                                          day=model.day,
                                          year=model.year,
                                          start_Date=start_Date,
                                          end_Date=end_Date)
          print(f"The predicted value for {model}- is {next_value}")                
    except ValueError as e:
                print(e) 
    
def detect(file_path=""):
    flagged_transactions, not_anomaly =init(file_path)
    #print(flagged_transactions,not_anomaly)
    print(flagged_transactions['ID'])
        
    
if __name__ == "__main__":
    detect(file_path="C:/Users/dell/Desktop/spock/anomalies/EventDate1.csv")
    dataModel = predictionmodel.DataModel()
    dataModel.logValue = int(input("Enter Log value: "))
    dataModel.iterations = int(input("Enter Iterations value: "))
    dataModel.movingAvgValue = int(input("Enter Moving Avg value: "))
    dataModel.seasonalPeriod =  int(input("Enter Seasonal Period value: "))
    dataModel.year =  int(input("Enter Year value: "))
    dataModel.month =  int(input("Enter Month value: "))
    dataModel.day =  int(input("Enter Day value: "))
    start_date = input("Enter start date (in the format 'YYYY-MM-DD'): ")
    end_date = input("Enter end date (in the format 'YYYY-MM-DD'): ")
    file_path = input("Enter Data File Path: ")
    execute(dataModel,file_path,start_date,end_date)