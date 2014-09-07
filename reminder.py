#! /usr/bin/env python3

# contains class encapsulating reminder object


__copyright__ = 'Yovary'
__author__ = 'karepker@gmail.com (Kar Epker)'


import calendar
import datetime
import json
import logging
import urllib.error
import urllib.parse
import urllib.request


def get_utc_timestamp(utc_datetime):
    return calendar.timegm(utc_datetime.utctimetuple())


def floor_datetime_to_day(utc_datetime):
    floored_datetime = utc_datetime - datetime.timedelta(hours=utc_datetime.hour,
            minutes=utc_datetime.minute, seconds=utc_datetime.second,
            microseconds=utc_datetime.microsecond)
    return floored_datetime


class Reminder:
    """A class encapsulating functionality needed for storing and sending a
    reminder."""

    api_token = 'f1e28817-3528-621a-70ac-8086fc300205'

    def __init__(self, username, time_of_day):
        self.username = username
        self.modulus = time_of_day
        self.recurring = True
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
            logging.info('Successfully sent yo to %s' % (self.username))
            return True
        except (urllib.error.URLError, urlib.error.HTTPError):
            logging.error('Failed to send yo to %s' % (self.username))
            return False

    def send_reminder(self):
        if not datetime.datetime.utcnow() > self.next_notification:
            return False

        self.send_yo()
        if self.recurring:
            self._set_next_send_time()
        return True

    def __lt__(self, other):
        return self.next_notification < other.next_notification

    def set_temporary(self):
        self.recurring = False
        
    def _set_next_send_time(self):
        self.next_notification += datetime.timedelta(days=1)

    def json_serialize(self):
        return json.dumps({
            'username': self.username,
            'modulus': str(self.modulus),
            'recurring': self.recurring,
            })
