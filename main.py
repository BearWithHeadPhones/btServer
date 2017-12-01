from bluetooth import *
from threading import Thread
import time

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
                strip.show()
                time.sleep(wait_ms/1000.0)











































from bluetoothUtils import server
from controller import reqController
import Queue
from interface import btMessage_pb2, Color_pb2

class Handler():
    def __init__(self, predicateFunc, runFunc):
           self.predicateFunc = predicateFunc
           self.runFunc = runFunc

    def predicate(self, item):
        return self.predicateFunc(item)

    def run(self, item):
        return self.runFunc(item)                


def pred(item):
    return  item.type == btMessage_pb2.BTMessage.COLOR

def run(item) :
    colorWipe(strip, Color(item.color.red, item.color.green, item.color.blue))
    print "usatwiam: " + str(item.color)

redLedHandler =  Handler(pred,run)


handlers = []
handlers.append(redLedHandler)

notifQueue = Queue.Queue()
bt_server = server.BTServer(notifQueue)
req_Controller = reqController.ReqController(notifQueue,handlers)
req_Controller.start()
bt_server.start()


