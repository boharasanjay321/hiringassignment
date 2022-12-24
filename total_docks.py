import json
import requests
from flask import Flask, jsonify, request


app = Flask(__name__)
#Total Docks Avl (use station url)

@app.route('/Total_Docks_avl',methods=['GET','POST'])
def test1():

    if(request.method=='GET'):
        req = requests.get('https://gbfs.divvybikes.com/gbfs/en/station_status.json')
        response = req.json()
        total=0
        for i in range(0,1421):
            m=response['data']['stations'][i]['num_docks_available']
            total = total + m


        return jsonify(total)

#Total Bikes Avl (use station url)
@app.route('/Total_Bikes_avl',methods=['GET','POST'])
def test2():

    if(request.method=='GET'):
        req = requests.get('https://gbfs.divvybikes.com/gbfs/en/station_status.json')
        response = req.json()
        total = 0
        for i in range(0, 682):
            z = response['data']['stations'][i]['num_bikes_available']
            total = total + z


        return jsonify(total)


#Total Station Active (use station url)
@app.route('/Total_station_active',methods=['GET','POST'])
def test3():

    if(request.method=='GET'):
        req = requests.get('https://gbfs.divvybikes.com/gbfs/en/station_status.json')
        response = req.json()
        sum = -1
        for i in range(0, 1421):
            if response['data']['stations'][i]['station_status'] == "active":
                z = sum + i
            else:
                continue

        return jsonify(z)



#Total Bikes that is reserved (use free bike url)
@app.route('/Reserved_bike',methods=['GET','POST'])
def test4():

    if(request.method=='GET'):
        req = requests.get('https://gbfs.divvybikes.com/gbfs/en/free_bike_status.json')
        response = req.json()
        sum = 1
        for i in range(0, 50):
            if response['data']['bikes'][i]['is_reserved'] == 1:
                continue

            else:
                z = sum + i

        return jsonify("all bikes are avilable:", z)


if __name__== '__main__' :
     app.run()

