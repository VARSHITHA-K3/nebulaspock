from algorithms.rule import init
#from alogrithims.isolation import noneAnomalyIsolation,anomalyIsolation,isolation

def detect(file_path=""):
    flagged_transactions, not_anomaly =init(file_path)
    #print(flagged_transactions,not_anomaly)
    print(flagged_transactions['ID'])
        
    
if __name__ == "__main__":
    detect(file_path="EventDate1.csv")
