import pandas as pd
import pymongo
import json
from datetime import datetime
import os
from pymongo import MongoClient
from flask import Flask,jsonify,request
from pymongo import MongoClient,InsertOne
from pprint import pprint
app=Flask(__name__)


client = pymongo.MongoClient("mongodb://sanjay:sanjay1@ac-ykrsrfh-shard-00-00.p8vph3x.mongodb.net:27017,ac-ykrsrfh-shard-00-01.p8vph3x.mongodb.net:27017,ac-ykrsrfh-shard-00-02.p8vph3x.mongodb.net:27017/?ssl=true&replicaSet=atlas-n3yj7q-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

db=client['studentdata']
collection2=db['studenttbl2']
requesting=[]
@app.route('/free_bike_status',methods=['GET','POST'])
def test1():
    if request.method == 'GET':
       with open(r"C:\Users\Dell\Desktop\Reserved_bike.json") as f:
          for jsonObj in f:
            myDict = json.loads(jsonObj)
            requesting.append(InsertOne(myDict))
            collection2.bulk_write(requesting)
            z1=collection2.find()
            for i in z1:
             return jsonify(str(i))
cwd = os.getcwd()
with open(os.path.join(cwd, "test1.txt"), "a") as f:
  f.write("free_bike_status.py on " + str(datetime.now()) + "\n")

if __name__== '__main__' :
     app.run()