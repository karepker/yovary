#! /usr/bin/env python3

# Starts the production version of the bottle server and helper threads.


__copyright__ = 'Yovary'
__author__ = 'karepker@gmail.com (Kar Epker)'


import debug_routes
import logging
import production_routes
import server
import server_tasks
import threading

from reminders import reminders

logging.basicConfig(level=logging.DEBUG)

debug_server = server.Server(host='localhost', port=8080, debug=True)
message_send_thread = threading.Thread(
            target=server_tasks.send_reminders, args=(debug_server,),
            name='send thread')
message_save_thread = threading.Thread(
            target=server_tasks.save_reminders, args=(debug_server,reminders,),
            name='save thread')
debug_server.run(message_send_thread, message_save_thread)
