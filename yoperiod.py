#! /usr/bin/env python3

#gcalendar for reference
#https://github.com/insanum/gcalcli

import bottle
import calendar
import datetime
import os
import sortedcontainers
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

SEND_THREAD_MAX_SLEEP_TIME = 5  # in seconds

def get_utc_timestamp(utc_datetime):
    return calendar.timegm(utc_datetime.utctimetuple())


def floor_datetime_to_day(utc_datetime):
    floored_datetime = utc_datetime - datetime.timedelta(hours=utc_datetime.hour,
            minutes=utc_datetime.minute, seconds=utc_datetime.second,
            microseconds=utc_datetime.microsecond)
    return floored_datetime


class Reminder:
    api_token = 'f1e28817-3528-621a-70ac-8086fc300205'

    def __init__(self, username, time_of_day):
        self.username = username
        self.modulus = time_of_day
        utc_datetime = datetime.datetime.utcnow()
        utc_floor_day = floor_datetime_to_day(utc_datetime)
        # schedule for today
        if utc_floor_day + self.modulus > utc_datetime:
             self.next_notification = utc_floor_day + self.modulus

        # schedule for tomorrow
        else:
            self.next_notification = (utc_floor_day + datetime.timedelta(days=1)
                    + self.modulus)
           
    def send_yo(self):
        payload = {
            'api_token': Reminder.api_token,
            'username': self.username
            }
        data = urllib.parse.urlencode(payload)
        data = data.encode('utf-8')
        req = urllib.request.Request('http://api.justyo.co/yo/', data)
        try:
            urllib.request.urlopen(req)
            print('Sucessfully sent yo')
            return True
        except (urllib.error.URLError, urlib.error.HTTPError):
            print('Failed to send yo')
            return False

    def send_reminder(self):
        if not datetime.datetime.utcnow() > self.next_notification:
            return False

        self.send_yo()
        self._set_next_send_time()
        return True

    def __lt__(self, other):
        return self.next_notification < other.next_notification
        
    def _set_next_send_time(self):
        self.next_notification += datetime.timedelta(days=1)


class Reminders:

    def __init__(self):
        self.reminders = sortedcontainers.SortedList()

    def send_reminders(self):
        # send reminders until a reminder does not need to be sent
        while self.reminders and self.reminders[0].send_reminder():
            first_reminder = self.reminders[0] 
            del self.reminders[0]
            self.reminders.add(first_reminder)

    def add_reminder(self, reminder):
        # iterate through the list and remove other instance of username
        pruned_reminders = sortedcontainers.SortedList()
        for candidate in self.reminders:
            # filter reminders with the same username
            if candidate.username != reminder.username:
                pruned_reminders.append(candidate)

        pruned_reminders.add(reminder)
        self.reminders = pruned_reminders

    def get_seconds_until_next_reminder(self):
        # return an arbitrarily high sleep number
        if not self.reminders:
            return SEND_THREAD_MAX_SLEEP_TIME

        time_until_next_notification = (self.reminders[0].next_notification - 
                datetime.datetime.utcnow())
        seconds_until_next = time_until_next_notification.total_seconds()
        now = datetime.datetime.utcnow()
        return seconds_until_next


def send_messages():
    while True:
        reminders.send_reminders()
        time_to_sleep = min(reminders.get_seconds_until_next_reminder(),
                            SEND_THREAD_MAX_SLEEP_TIME)
        if time_to_sleep > 1:
           time.sleep(time_to_sleep)   


reminders = Reminders()
threading.Thread(target=send_messages).start()


@bottle.route('/<filename:path>')
def send_static(filename):
    return bottle.static_file(
            filename, os.path.dirname(os.path.realpath(__file__)))


@bottle.get('/')
def sign_up_page():
    return bottle.template('page', validation='', handle='', time='')


@bottle.post('/')
def sign_up():
    handle = bottle.request.forms.get('handle')
    time = bottle.request.forms.get('time')
    utc_offset = bottle.request.forms.get('utc_offset')

    # convert submitted time into a timezone
    time_parts = time.split(':', 2)

    # validate time is ints
    try:
        hour = int(time_parts[0])
        minute = int(time_parts[1])
        if hour > 24 or hour < 0 or minute > 60 or minute < 0:
            raise ValueError('Invalid hour or minute')
    except ValueError:
        return bottle.template('page',
                validation='You must input a vald time in the form HH:MM!',
                handle=handle, time=time)

    try:
        hours_from_utc = int(utc_offset)
    except ValueError:
        return bottle.template('page',
                validation='Could not detect timezone!',
                handle=handle, time=time)

    # convert local time to utc time
    utc_hour = (hour + hours_from_utc) % 24
    modulus = datetime.timedelta(hours=utc_hour, minutes=minute)

    # add the reminder
    reminders.add_reminder(Reminder(handle, modulus))
    return bottle.template('page', validation='', handle=handle, time=time)


@bottle.get('/list')
def list():
    return bottle.template('list', reminders=reminders)

# start bottle, start notifying thread
bottle.run(host='localhost', port=8080, debug=True)
