#! /usr/bin/env python3

# Contains the debug routes for the application.


__copyright__ = 'Yovary'
__author__ = 'karepker@gmail.com (Kar Epker)'

import bottle

from reminders import reminders


@bottle.get('/list')
def list():
    return bottle.template('list', reminders=reminders)
