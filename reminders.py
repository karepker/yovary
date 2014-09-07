#! /usr/bin/env python3

# contains class encapsulating data structure that holds reminders


__copyright__ = 'Yovary'
__author__ = 'karepker@gmail.com (Kar Epker)'


import datetime
import logging
import sortedcontainers
import threading


class Reminders:
    """Holds reminders and controls insertion and sending of them."""

    def __init__(self):
        self.reminders = sortedcontainers.SortedList()
        self.reminders_lock = threading.Lock()
        self.temporary_reminders = sortedcontainers.SortedList()

    def send_reminders(self):
        self.reminders_lock.acquire()
        # send reminders until a reminder does not need to be sent
        while self.reminders and self.reminders[0].send_reminder():
            first_reminder = self.reminders[0]
            del self.reminders[0]
            self.reminders.add(first_reminder)
        self.reminders_lock.release()

    def add_reminder(self, reminder):
        # iterate through the list and remove other instance of username
        pruned_reminders = sortedcontainers.SortedList()
        self.reminders_lock.acquire()
        for candidate in self.reminders:
            # filter reminders with the same username
            if candidate.username != reminder.username:
                pruned_reminders.append(candidate)

        pruned_reminders.add(reminder)
        self.reminders = pruned_reminders
        self.reminders_lock.release()

    def add_temporary_reminder(self, reminder):
        reminder.set_temporary()  # should already be set, but just in case
        self.reminders_lock.acquire()
        self.reminders.add(reminder)
        self.reminders_lock.release()

    def get_seconds_until_next_reminder(self):
        self.reminders_lock.acquire()
        # return an arbitrarily high sleep number
        if not self.reminders:
            self.reminders_lock.release()
            return 600

        time_until_next_notification = (self.reminders[0].next_notification - 
                datetime.datetime.utcnow())
        self.reminders_lock.release()
        seconds_until_next = time_until_next_notification.total_seconds()
        now = datetime.datetime.utcnow()
        return seconds_until_next

    def serialize_to_file(self, filename):
        self.reminders_lock.acquire()
        with open(filename, 'w') as out_file:
            logging.info('Saving %d reminders' % (len(self.reminders)))
            for reminder in self.reminders:
                out_file.write(reminder.json_serialize())
                out_file.write('\n')
        self.reminders_lock.release()


reminders = Reminders()
