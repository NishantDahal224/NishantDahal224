import datetime
import json
import os


class Diary:
    import datetime
    import json
    def __init__(self,title,content):
        self.title = title
        self.content = content

    def check(self):
        if not os.path.exists("dairy.json"):
            print("File not found")

    def Add(self):
        date = datetime.date.today()
        self.data = [self.title,self.content,str(date)]
        self.check()
        with open("dairy.json","a") as f:
            json.dump(self.data,f,indent=4)

    def view(self):
        self.check()
        with open("dairy.json","r") as f:
            loaded = json.load(f)
            print(loaded)

    def search(self):
        self.check()
        date = input("Enter date to search: ")
        with open("dairy.json","r") as f:
            loaded = json.load(f)
            filter = [data for data in loaded if data["date"] == date]
            print(filter)

entry1 = Diary("lorem","I am a good boy.")
entry1.Add()