from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from firebase import firebase

class ActionMentor(Action):
    def name(self):
        return 'action_mentor'
        
    def run(self, dispatcher, tracker, domain):
        #from apixu.client import ApixuClient
        #api_key = '2f34b02297f6ce077a7136be5669b465'
        #client = ApixuClient(api_key)
        
        act = tracker.get_slot('activity')
        #current = client.getCurrentWeather(q=loc)
        #api_address='http://api.apixu.com/v1/current.json?key={}&q={}'.format(api_key,loc)	
        #current = requests.get(api_address).json()
        firebase = firebase.FirebaseApplication("https://the-enigma-3f920.firebaseio.com/",None)
        result = firebase.get('/Art',None)
        #country = current['location']['country']
        #city = current['location']['name']
        #condition = current['current']['condition']['text']
        #temperature_c = current['current']['temp_c']
        #humidity = current['current']['humidity']
        #wind_mph = current['current']['wind_mph']
        
        #response = """ It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
        
        dispatcher.utter_message(result)
        return [SlotSet('activity',act)]
