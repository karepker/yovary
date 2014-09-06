#! /usr/bin/env python3

#gcalendar for reference
#https://github.com/insanum/gcalcli

#what's a good way to scale this for many users??
import bottle
import datetime
import urllib.error
import urllib.parse
import urllib.request

class EmbryoUser:
    api_token = 'f1e28817-3528-621a-70ac-8086fc300205'
    username = 'DROMENIC'
    
def single_user_yo(user_class):
    payload = {
            'api_token': user_class.api_token,
            'username': user_class.username
            }
    data = urllib.parse.urlencode(payload)
    data = data.encode('utf-8')
    req = urllib.request.Request('http://api.justyo.co/yo/', data)
    print(urllib.request.urlopen(req))

def pill_reminder(user_class, timeRequest):
    if timeRequest in range[datetime.time-5,datetime.time+5]:
        #Once array is implemented, this should iterate through the array
        single_user_yo(user_class)
    
@bottle.route('/')
def sign_up():
    return bottle.template('page')

bottle.run(host='localhost', port=8080, debug=True)
