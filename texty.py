import requests
import json
from loc import *
from datetime import datetime,date
from map import *

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()
d1 = today.strftime("%d/%m/%Y")
URL = 'https://www.sms4india.com/api/v1/sendCampaign'
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

mess1 = getLocation()
mess = str(mess1)
text = 'An accident has taken place at coordinates: {} at {} {}.'.format(mess,current_time,d1)
response = sendPostRequest(URL, 'apikey', 'secretKey', 'stage', 'number', 'senderId', text )
mapps(mess1[0],mess1[1])
print (response.text)