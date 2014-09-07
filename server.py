#! /usr/bin/env python3

# contains class encapsulating server functionality


__copyright__ = 'Yovary'
__author__ = 'karepker@gmail.com (Kar Epker)'


import bottle
import threading


class Server:
    """Encapsulates functionality for the server and threads that depend on
    it."""

    def __init__(self, host='127.0.0.1', port='8080', debug=False):
        self.host = host
        self.port = port
        self.debug = debug
        self.running_lock = threading.Lock()
        self._running = False

    def run(self, *threads):
        self.running = True
        for thread in threads:
            thread.start()

        try:
            bottle.run(host=self.host, port=self.port, debug=self.debug)
            
        finally:
            self.running = False
            for thread in threads:
                thread.join()

    @property
    def running(self):
        self.running_lock.acquire()
        server_running = self._running
        self.running_lock.release()
        return server_running

    @running.setter
    def running(self, value):
        self.running_lock.acquire()
        self._running = value
        self.running_lock.release()
