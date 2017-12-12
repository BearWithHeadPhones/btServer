#!/usr/bin/env python

import time
import subprocess

from neopixel import *


# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
# Intialize the library (must be called once before other functions).
strip.begin()

def colorWipe(strip, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(strip.numPixels()):
                strip.setPixelColor(i, color)
                time.sleep(wait_ms/1000.0)
                strip.show()
                #time.sleep(wait_ms/1000.0)


def pairing (parent):
    while False == parent.stopped():
        colorWipe(strip,Color(0,0,1))
        colorWipe(strip,Color(0,0,0))




def paired (parent):
     colorWipe(strip,Color(0,1,0))

from bluetoothUtils import server
from controller import reqController
import Queue
from interface import btMessage_pb2, Led_pb2
from anim import AnimationRunner

class Handler():
    def __init__(self, predicateFunc, runFunc):
           self.predicateFunc = predicateFunc
           self.runFunc = runFunc

    def predicate(self, item):
        return self.predicateFunc(item)

    def run(self, item):
        return self.runFunc(item)                


def pred(item):
    return  item != "green" and item.type == btMessage_pb2.BTMessage.LED

def run(item) :
    print item
    strip.setPixelColor(item.led.index, Color(item.led.red, item.led.green, item.led.blue))
    strip.show()
    print "ustawiam: " + str(item.led)


def predGreen(item):
    return  item == "green"

def runGreen(item) :
    colorWipe(strip, Color(0, 255, 0))
    print "usatwiam: green"



mask =[0,0,0,0,0,0,0,0]

def predINT(item):
    print "pred"
    return True

def runINT(item):
    if mask[item] == 0 :
        print "zmieniam"
        strip.setPixelColor(item, Color(255, 255, 255))
        mask[item] = 1
    else :
        strip.setPixelColor(item, Color(0, 0, 0))
        mask[item] = 0
    strip.show()


colorWipe(strip, Color(0, 0, 0))
animRunner = AnimationRunner.AnimationRunner()



time.sleep(5000/1000.0)


colorLedHandler =  Handler(pred,run)
greenLedHandler =  Handler(predGreen,runGreen)
intLedHandler =  Handler(predINT,runINT)

handlers = []
handlers.append(colorLedHandler)

sdptoolregisterrfcomm = subprocess.Popen("sudo sdptool add sp", shell=True)
sdptoolregisterrfcomm.wait()

print "registered sp"
notifQueue = Queue.Queue()
bt_server = server.BTServer(notifQueue, animRunner)
req_Controller = reqController.ReqController(notifQueue,handlers)

req_Controller.start()
bt_server.start()



