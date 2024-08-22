import csv
with open("onlinefoods.csv") as file:
    csv_reader=csv.reader(file)
    liste=list(csv_reader)
    print(len(liste)-1)

with open("onlinefoods.csv") as file:
    csv_reader=csv.DictReader(file)
    num=len([user for user in csv_reader if user["Occupation"]==["Student"]])
    print(num)
    
with open("onlinefoods.csv") as file:
    csv_reader=csv.DictReader(file)
    users=(user for user in csv_reader if int(user["Age"])>= 20 and int(user["Age"])<=30)
    for i in users:
        print(i["latitude"],i["longitude"])