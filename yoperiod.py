#! /usr/bin/env python3

#gcalendar for reference
#https://github.com/insanum/gcalcli

import bottle
import calendar
import datetime
import sortedcontainers
import urllib.error
import urllib.parse
import urllib.request


def get_utc_timestamp(utc_datetime):
    return calendar.timegm(utc_datetime.utctimetuple())

def floor_datetime_to_day(utc_datetime):
    utc_datetime.replace(hour=0, minute=0, second=0, microseconds=0)


class Reminder:
    api_token = 'f1e28817-3528-621a-70ac-8086fc300205'

    def __init__(username, time_of_day):
        self.username = username
        self.modulus = time_of_day
        utc_datetime = datetime.datetime.utcnow()
        utc_floor_day = floor_datetime_to_day(utc_datetime)
        # schedule for today
        if (utc_floor_day + self.modulus <= utc_datetime)
             self.next_notification = utc_floor_day + self.modulus

        # schedule for tomorrow
        else:
            self.next_notification = (utc_floor_day + datetime.timedelta(days=1)
                    + self.modulus)
           
    def send_yo():
        payload = {
            'api_token': user_class.api_token,
            'username': user_class.username
            }
        data = urllib.parse.urlencode(payload)
        data = data.encode('utf-8')
        req = urllib.request.Request('http://api.justyo.co/yo/', data)
        try:
            urllib.request.urlopen(req)
            return True
        except urllib.error.URLError, urlib.error.HTTPError:
            return False

    def send_reminder():
        if not datetime.datetime.utcnow() > self.next_notification:
            return False

        self.send_yo()
        self._set_next_send_time()
        return True

    def _set_next_send_time():
        self.next_notification += datetime.timedelta(days=1)

class Reminders:

    def __init__(self):
        self.reminders = sortedcontainers.SortedList()

    def send_yos(self):
        # send reminders until a reminder does not need to be sent
        while self.reminders and self.reminders[0].send_reminder():
            first_reminder = self.reminders[0] 
            del self.reminders[0]
            self.reminders.add(first_reminder)

    def add_reminder(self, reminder):
        # iterate through the list and remove other instance of username
        pruned_reminders = sortedcontainers.SortedList()
        for candidate self.reminders:
            # filter reminders with the same username
            if candidate.username != reminder.username:
                pruned_reminders.append(candidate)

        pruned_reminders.add(reminder)
        self.reminders = pruned_reminders


reminders = Reminders()

@bottle.get('/')
def sign_up_page():
    return bottle.template('page')

@bottle.post('/')
def sign_up():
    handle = bottle.request.get('handle')
    time = bottle.request.get('time')

    # convert submitted time into a timezone
    hours, minutes = time.split(':', 2)
    modulus = datetime.timedelta(hour=hours, minute=minutes)
    
    # add the reminder
    reminders.add_reminder(Reminder(handle, modulus))
    return bottle.template('page')

bottle.run(host='localhost', port=8080, debug=True)
