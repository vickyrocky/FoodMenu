#!/usr/bin/env python
import json, os, requests
from awsauth import S3Auth
from renderMenu import db, FoodMenu

key = os.environ.get('UWOPENDATA_APIKEY')
ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

def getData(service):
	payload = {'key': key, 'service': service}
	r = requests.get('http://api.uwaterloo.ca/public/v1/', params=payload)
	return r

foodMenu = getData('FoodMenu').text
foodMenuData = FoodMenu(foodMenu)
# serviceInfo = getData('FoodServices').text
# requests.put('http://s3.amazonaws.com/uwfoodmenu/serviceInfo.txt', data=serviceInfo, auth=S3Auth(ACCESS_KEY, SECRET_KEY))
db.session.add(foodMenuData)
db.session.commit()
