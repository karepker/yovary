#! /usr/bin/env python3

# Contains functions for other server threads to use.


__copyright__ = 'Yovary'
__author__ = 'karepker@gmail.com (Kar Epker)'


import time

from production_routes import reminders


POSTPONE_DURATION = 15  # in minutes
SAVE_THREAD_SLEEP_TIME = 1 * 60  # one hour in seconds
SAVED_NOTIFICATIONS_FILE = '/tmp/saved_reminders.txt'
SEND_THREAD_MAX_SLEEP_TIME = 5  # in seconds


def send_reminders(server):
    while server.running:
        reminders.send_reminders()
        time_to_sleep = min(reminders.get_seconds_until_next_reminder(),
                            SEND_THREAD_MAX_SLEEP_TIME)
        if time_to_sleep > 1:
           time.sleep(time_to_sleep)   


def save_reminders(server, reminders):
    # write reminders to a file on a schedule
    while server.running:
        reminders.serialize_to_file(SAVED_NOTIFICATIONS_FILE)
        time.sleep(SAVE_THREAD_SLEEP_TIME)
