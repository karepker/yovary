#! /usr/bin/env python3

# contains class encapsulating data structure that holds reminders


__copyright__ = 'Yovary'
__author__ = 'karepker@gmail.com (Kar Epker)'


import datetime
import sortedcontainers


class Reminders:
    """Holds reminders and controls insertion and sending of them."""

    def __init__(self):
        self.reminders = sortedcontainers.SortedList()
        self.temporary_reminders = sortedcontainers.SortedList()

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

    def add_temporary_reminder(self, reminder):
        reminder.set_temporary()  # should already be set, but just in case
        self.reminders.add(reminder)

    def get_seconds_until_next_reminder(self):
        # return an arbitrarily high sleep number
        if not self.reminders:
            return 600

        time_until_next_notification = (self.reminders[0].next_notification - 
                datetime.datetime.utcnow())
        seconds_until_next = time_until_next_notification.total_seconds()
        now = datetime.datetime.utcnow()
        return seconds_until_next

    def serialize_to_file(self, filename):
        with open(filename, 'w') as out_file:
            for reminder in self.reminders:
                print("writing reminder")
                out_file.write(reminder.json_serialize())


reminders = Reminders()
