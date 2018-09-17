import threading
from interface import btMessage_pb2
from anim import AnimationRunner, animations
import functools


class Handler():
    def __init__(self, predicateFunc, runFunc):
           self.predicateFunc = predicateFunc
           self.runFunc = runFunc

    def predicate(self, item):
        return self.predicateFunc(item)

    def getFunction(self):
        return self.runFunc



def pred(item):
    return item.type == btMessage_pb2.BTMessage.ANIM and item.animation.animName == "fire"

def anim(item):
    return AnimationRunner.Loop(animations.fire)

def pred2(item):
    return item.type == btMessage_pb2.BTMessage.ANIM and item.animation.animName == "clear"

def anim2(item):
    return AnimationRunner.OneTime(animations.clear)


def predSetPixel(item):
    return item.type == btMessage_pb2.BTMessage.LED

def setPixel(item):
    return AnimationRunner.OneTime(functools.partial(animations.setPixel,item))

def predStrobo(item):
    return item.type == btMessage_pb2.BTMessage.ANIM and item.animation.animName == "strobo"

def animStrobo(item):
    return AnimationRunner.Loop(animations.strobo)

def predPulse(item):
    return item.type == btMessage_pb2.BTMessage.ANIM and item.animation.animName == "pulse"

def animPulse(item):
    return AnimationRunner.Loop(animations.pulse)

def predStripe(item):
    return item.type == btMessage_pb2.BTMessage.STRIPE

def animStripe(item):
    return AnimationRunner.OneTime(functools.partial(animations.stripe,item))

def getHandlers():
    handlers = []
    handlers.append(Handler(pred ,anim))
    handlers.append(Handler(pred2, anim2))
    handlers.append(Handler(predSetPixel,setPixel))
    handlers.append(Handler(predStrobo, animStrobo))
    handlers.append(Handler(predPulse, animPulse))
    handlers.append(Handler(predStripe, animStripe))
    return handlers


class ReqController (threading.Thread):
   def __init__(self, notificationQueue, handlers, animationRunner):
      threading.Thread.__init__(self)
      self.notificationQueue = notificationQueue
      self.handlers = handlers
      self.animationRunner = animationRunner
   def run(self):
      while True:
          print "reqController"
          item = self.notificationQueue.get()
          for handler in self.handlers :
              if handler.predicate(item) :
                  self.animationRunner.animate((handler.getFunction()(item)))
          self.notificationQueue.task_done()
