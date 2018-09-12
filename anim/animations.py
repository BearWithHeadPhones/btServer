from neopixel import *
import time
import random
import numpy as np
import math


# LED strip configuration:
LED_COUNT      = 140    # Number of LED pixels.
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

def colorWipe(strip, color, numOfPixels, wait_ms=200):
        """Wipe color across display a pixel at a time."""
        for i in range(numOfPixels):
                strip.setPixelColor(i, color)
                time.sleep(wait_ms/1000.0)
                strip.show()
                #time.sleep(wait_ms/1000.0)

def pairing (item = None):
    colorWipe(strip,Color(0,0,1),20)
    colorWipe(strip,Color(0,0,0),20)
    time.sleep(1)


def paired (item = None):
     colorWipe(strip,Color(0,1,0),20,0)



pixelMap = [False] * strip.numPixels()
def setPixel(item):
    if pixelMap[item.led.index] :
        strip.setPixelColor(item.led.index, Color(0, 0, 0))
    else:
        strip.setPixelColor(item.led.index, Color(item.led.red, item.led.green, item.led.blue))
    pixelMap[item.led.index] = not pixelMap[item.led.index]
    strip.show()

def fire(item = None):

        r = 255
        g = 96
        b =12


        for i in range(strip.numPixels()/2-1):
            flicker = random.randint(0, 100)
            rflick = r - flicker
            gflick = g - flicker
            bflick = b - flicker
            if rflick < 0 :
                rflick = 0
            if gflick < 0 :
                gflick = 0
            if bflick < 0 :
                bflick = 0

            strip.setPixelColor(i*2, Color(rflick,gflick,bflick))
            strip.setPixelColor(i*2+1 , Color(rflick, gflick, bflick))
            #strip.setPixelColor(i * 4 + 2, Color(rflick, gflick, bflick))
            #strip.setPixelColor(i * 4 + 3, Color(rflick, gflick, bflick))
        strip.show()
        time.sleep(random.randint(50,150) / 1000.0)

def clear(item = None):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()

def strobo(item = None):
    for i in range(strip.numPixels()/2):
        strip.setPixelColor(i*2, Color(255, 255, 255))
        strip.setPixelColor(i*2 +1, Color(0, 0, 0))
    strip.show()
    time.sleep(50 / 1000.0)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()
    time.sleep(50 / 1000.0)
    for i in range(strip.numPixels()/2):
        strip.setPixelColor(i * 2+1, Color(255, 255, 255))
        strip.setPixelColor(i * 2, Color(0, 0, 0))
    strip.show()
    time.sleep(50 / 1000.0)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()
    time.sleep(50 / 1000.0)


def setColorToEntireStrip(r,g,b, brightness):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i , Color(int(r * brightness), int(g * brightness), int(b * brightness)))

def pulse(item = None):
    for i in np.arange(1.5*math.pi, 3.5*math.pi, math.pi/50):
        setColorToEntireStrip(0,255,0,((math.sin(i))+1)/2)
        strip.show()
        time.sleep(10 / 1000.0)



