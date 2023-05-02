import random
from fastapi import FastAPI,Request
from anomalies.algorithms.rule import init
import forecasting.alogrithims.rule as ruleBase
import forecasting.models.predictionmodel as  predictionmodel
import json
from framework.interfaces.consumer.NebulaConsumer import NebulaConsumer
from framework.interfaces.producer.NebulaProducer import NebulaProducer
import time
from framework.services.kafka.consumer.NebulaKafkaConsumer import NebulaKafkaConsumer
from framework.services.kafka.producer.NebulaKafkaProducer import NebulaKafkaProducer
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
    

@app.post('/send')
async def producer(req:Request):
    req_info = await req.json()
    topic_name = req_info["topic_name"]
    json_object = req_info["payload"]
    messager_type = req_info["messager_type"]
    producer:NebulaProducer = None
    if(messager_type =="kafka"):
        producer = NebulaKafkaProducer('localhost:9092')

    producer.sendMessage(topic_name,json_object)
    return json_object


@app.get('/receive')
async def consumer(req:Request):
    req_info = await req.json()
    topic_name = req_info["topic_name"]
    consumer:NebulaConsumer = NebulaKafkaConsumer('localhost:9092')
    print("NebulaConsumer Topic Name=%s"%(topic_name))
    message = consumer.consumeMessage(topic_name)
    time_to_sleep = random.randint(1, 11)
    time.sleep(time_to_sleep)