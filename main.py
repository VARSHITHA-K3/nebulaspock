from fastapi import FastAPI,Request
from anomalies.algorithms.rule import init
import forecasting.alogrithims.rule as ruleBase
import json
import forecasting.models.predictionmodel as  predictionmodel
app = FastAPI()



                                                                                                

@app.get("/")
def version(reg:Request):
    return "Nebula 2.3.0.55"


@app.post('/execute')
async def predict(req: Request):
    req_info = await req.json()
    dataModel = predictionmodel.DataModel()
    dataModel.logValue = req_info["logValue"]
    dataModel.day = req_info["day"]
    dataModel.iterations = req_info["iterations"]
    dataModel.month = req_info["month"]
    dataModel.movingAvgValue = req_info["movingAvgValue"]
    dataModel.seasonalPeriod = req_info["seasonalPeriod"]
    dataModel.year = req_info["year"]
    start_date = req_info["start_date"]
    end_date = req_info["end_date"]
    file_path = req_info["file_path"]
    #print(json.dumps(dataModel,default=vars),start_date,end_date,file_path)
    return ruleBase.ruleExecute(dataModel,file_path=str(file_path),startdate=str(start_date),enddate=str(end_date))


@app.post('/detect')
async def anomolies(req:Request):
    req_info = await req.json()
    file_path = req_info["file_path"]
    flagged_transactions, not_anomaly = init(file_path)
    if flagged_transactions:
        return {"status": "success", "message": flagged_transactions['ID']}
    else:
        return {"status": "success", "message": "No anomalies detected"}
    
if __name__ == "__main__":
    detect(file_path="C:/FastAPI/EventDate1.csv")
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
    ruleBase.predict_val(dataModel,file_path,start_date,end_date)