import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["final_project_db"]
# mycol = mydb["employees"]