#! /usr/bin/env python3

# Contains the production routes for the application.

__copyright__ = 'Yovary'
__author__ = 'karepker@gmail.com (Kar Epker)'


import bottle
import datetime
import os
import reminder
import threading

from reminders import reminders


POSTPONE_DURATION = 15  # in minutes


@bottle.route('/<filename:path>')
def send_static(filename):
    return bottle.static_file(
            filename, os.path.dirname(os.path.realpath(__file__)))


@bottle.get('/')
def sign_up_page():
    return bottle.template('page', validation='', username='', time='')


@bottle.post('/')
def sign_up():
    username = bottle.request.forms.get('username')
    time = bottle.request.forms.get('time')
    utc_offset = bottle.request.forms.get('utc_offset')

    # username and time are required parameters
    if not time or not username:
        return bottle.template('page',
                validation='You must send both time and username!',
                username=username, time=time)


    # validate username
    if not username.isalpha():
        return bottle.template('page',
                validation='Your username must consist of only alphabetical '
                'characters!', username=username, time=time)


    # convert submitted time into a timezone
    time_parts = time.split(':', 2)

    # validate time is ints
    try:
        hour = int(time_parts[0])
        minute = int(time_parts[1])
        if hour > 24 or hour < 0 or minute > 60 or minute < 0:
            raise ValueError('Invalid hour or minute')
    except (ValueError, TypeError):
        return bottle.template('page',
                validation='You must input a vald time in the form HH:MM!',
                username=username, time=time)

    try:
        hours_from_utc = int(utc_offset)
    except ValueError:
        return bottle.template('page',
                validation='Could not detect timezone!',
                username=username, time=time)

    # convert local time to utc time
    utc_hour = (hour + hours_from_utc) % 24
    modulus = datetime.timedelta(hours=utc_hour, minutes=minute)

    # add the reminder
    reminders.add_reminder(reminder.Reminder(username, modulus))
    return bottle.template('page', validation='', username=username, time=time)


@bottle.route('/about')
def list():
    return bottle.template('about')


@bottle.get('/postpone')
def postpone():
    username = bottle.request.query.username
    if not username:
        return bottle.template(
                'postpone', duration=POSTPONE_DURATION, success=False,
                username=username)
    utc_now = datetime.datetime.utcnow()
    modulus = datetime.timedelta(hours=utc_now.hour, 
                                 minutes=utc_now.minute + POSTPONE_DURATION)
    reminders.add_temporary_reminder(reminder.Reminder(username, modulus))
    return bottle.template(
            'postpone', duration=POSTPONE_DURATION, success=True,
            username=username)
