#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Rumps menu bar item for security ipcam selection

AS
"""

import rumps
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    # try:
    #     # PyInstaller creates a temp folder and stores path in _MEIPASS
    #     base_path = sys._MEIPASS
    # except Exception:
    #     base_path = os.path.abspath(".")
    #base_path = '~/code/mbipcam/'

    # comment this line & uncomment above is bundling with pyinstaller
    base_path = os.path.dirname(__file__)

    return os.path.join(base_path, relative_path)

rumps.debug_mode(True)

localfun = resource_path('view_ipcam.py')

# CAMERAS
@rumps.clicked('Back Camera')
def print_something(_):
	os.system('python ' + localfun + ' 0')


@rumps.clicked('Front Camera')
def print_something(_):
	os.system('python ' + localfun + ' 1')

# SOCKETS
@rumps.clicked('Coffee')
def print_something(_):
    os.system('node ' + resource_path('ToggleCoffeeMaker.js'))


@rumps.clicked('Quit')
def clean_up_before_quit(_):
    print('execute clean up code')
    rumps.quit_application()


app = rumps.App('IPC', menu=['Back Camera', 'Front Camera', 'Coffee', 'Quit'], quit_button=None)
app.run()


