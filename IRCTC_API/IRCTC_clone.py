import requests
class IRCTC:
    def __init__(self):
        user_input=input("""How would u like to proceed?
        1. Enter 1 to check live train status
        2. Enter 2 to check PNR
        3. Enter 3 to check train schedule""")
        
        if user_input=="1":
            print("live train status")
        elif user_input=="2":
            print("PNR checking")
        else:
            self.train_schedule()
    
    def train_schedule(self):
        train_number=input("Enter the train number")
        self.fetch_data(train_number)

    def fetch_data(self,train_no):
        data=requests.get("https://indianrailapi.com/api/v2/TrainSchedule/apikey/b8fe7f70e1686bb9dd8b3d600e5fa481/TrainNumber/{}".format(train_no))
        data=data.json()

        print(data["Route"])
        for i in data["Route"]:
            print(i["StationName"],"|",i["ArrivalTime"],"|",i["DepartureTime"],"|",i["Distance"],"kms")

obj=IRCTC()