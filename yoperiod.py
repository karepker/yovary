#import a bunch of shit

#gcalendar for reference
#https://github.com/insanum/gcalcli



#what's a good way to scale this for many users??
import requests
import datetime

preset_api_token= 'f1e28817-3528-621a-70ac-8086fc300205'



class EmbrYO_User:
	api_token= preset_api_token
	username='SARAHPG'

def single_user_yo( user_class ):
	payload= {'api_token': user_class.api_token, 'username': user_class.username}
	return requests.post("http://api.justyo.co/yo/", data=payload)

#Array of users with the same time should be used

def pill_reminder( user_class, timeRequest ):
	if timeRequest in range[datetime.time-5,datetime.time+5]:
		#Once array is implemented, this should iterate through the array
		single_user_yo( user_class )
	
testBunny=EmbrYO_User()
single_user_yo( testBunny )

#def ovary_action( api_token, username, dayPrediction):



	