import threading

class ReqController (threading.Thread):
   def __init__(self, notificationQueue, handlers):
      threading.Thread.__init__(self)
      self.notificationQueue = notificationQueue
      self.handlers = handlers
   def run(self):
      while True:
          print "reqController"
          item = self.notificationQueue.get()
          print item
          for handler in self.handlers :
              if handler.predicate(item) :
                  handler.run(item)
          self.notificationQueue.task_done()
