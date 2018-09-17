#!/usr/bin/env python

import subprocess
from bluetoothUtils import server
from controller import reqController
import Queue
from anim import AnimationRunner, animations
import signal
import sys

animRunner = AnimationRunner.AnimationRunner()
animRunner.animate(AnimationRunner.OneTime(animations.clear))

sdptoolregisterrfcomm = subprocess.Popen("sudo sdptool add sp", shell=True)
sdptoolregisterrfcomm.wait()

notifQueue = Queue.Queue()
bt_server = server.BTServer(notifQueue, animRunner)
req_Controller = reqController.ReqController(notifQueue,reqController.getHandlers(),animRunner)

req_Controller.start()
bt_server.start()

def signal_handler(sig, frame):
    bt_server.closeSockets()
    sys.exit(0)
signal.signal(
    signal.SIGINT, signal_handler)

signal.pause()
