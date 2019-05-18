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
	#os.system('python view_ipcam.py 0')
	os.system('python ' + localfun + ' 0')


@rumps.clicked('Front Camera')
def print_something(_):
	#os.system('python view_ipcam.py 1')
	os.system('python ' + localfun + ' 1')

# SOCKETS
@rumps.clicked('Kettle')
def print_something(_):
    #os.system('python view_ipcam.py 1')
    os.system('node ToggleKettle.js')

@rumps.clicked('Coffee')
def print_something(_):
    #os.system('python view_ipcam.py 1')
    os.system('node ToggleCoffeeMaker.js')

@rumps.clicked('Desk Lamp')
def print_something(_):
    #os.system('python view_ipcam.py 1')
    os.system('node ToggleDeskLamp.js')

@rumps.clicked('Dining Lamp')
def print_something(_):
    #os.system('python view_ipcam.py 1')
    os.system('node ToggleDiningLamp.js')

@rumps.clicked('Desk Twinkle')
def print_something(_):
    #os.system('python view_ipcam.py 1')
    os.system('node ToggleFairyLights.js')

@rumps.clicked('Office Fan')
def print_something(_):
    #os.system('python view_ipcam.py 1')
    os.system('node ToggleFan.js')

@rumps.clicked('Living Lamp')
def print_something(_):
    #os.system('python view_ipcam.py 1')
    os.system('node ToggleLivingRoomLamp.js')

@rumps.clicked('Living Speakers')
def print_something(_):
    #os.system('python view_ipcam.py 1')
    os.system('node ToggleSpeakers.js')


@rumps.clicked('Quit')
def clean_up_before_quit(_):
    print('execute clean up code')
    rumps.quit_application()


app = rumps.App('IPC', menu=['Back Camera', 'Front Camera', 'Kettle', 'Coffee', 'Desk Lamp', 'Dining Lamp', 'Desk Twinkle', 'Office Fan', 'Living Lamp', 'Living Speakers', 'Quit'], quit_button=None)
app.run()


