#! /usr/bin/env python3

# Starts the production version of the bottle server and helper threads.


__copyright__ = 'Yovary'
__author__ = 'karepker@gmail.com (Kar Epker)'


import production_routes
import server
import server_tasks
import threading

from reminders import reminders

# start bottle, start notifying thread
prod_server = server.Server(host='0.0.0.0', port=80, debug=False)
message_send_thread = threading.Thread(
            target=server_tasks.send_reminders, args=(prod_server,),
            name='send thread')
message_save_thread = threading.Thread(
            target=server_tasks.save_reminders, args=(prod_server,reminders,),
            name='save thread')
prod_server.run(message_send_thread, message_save_thread)
