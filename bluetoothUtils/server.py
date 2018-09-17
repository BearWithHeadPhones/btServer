from bluetooth import *
import threading
from interface import btMessage_pb2
import anim.animations
from anim.AnimationRunner import Loop,OneTime


class BTServer (threading.Thread):
   def __init__(self, notificationQueue, animationRunner):
      threading.Thread.__init__(self)
      #self.daemon = True
      self.notificationQueue = notificationQueue
      self.animationRunner = animationRunner
      self.server_sock = None
      self.client_sock = None
      self.BUFFER = 1024

   def closeSockets(self):
       print "closing sockets"

       self.server_sock.close()
       if self.client_sock :
           self.client_sock.close()

   def receiveAlllData(self):
       data = b''
       partcount = 0
       while True:
           part = self.client_sock.recv(self.BUFFER)
           data += part
           try:
               deserializedMessage = btMessage_pb2.BTMessage()
               deserializedMessage.ParseFromString(bytes(data))
               return deserializedMessage
           except :
               print "exception trying next:" + str(partcount)
               pass


   def run(self):

    while True:
          self.server_sock = BluetoothSocket(RFCOMM)
          self.server_sock .bind(("", PORT_ANY))
          self.server_sock.listen(1)
          port = self.server_sock.getsockname()[1]
          uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
          advertise_service(self.server_sock, "BTServer",
                             service_id=uuid,
                             service_classes=[uuid, SERIAL_PORT_CLASS],
                             profiles=[SERIAL_PORT_PROFILE],
                             #                   protocols = [ OBEX_UUID ]
                             )
          print "waiting for connection"
          self.animationRunner.animate(OneTime(anim.animations.pairing))
          self.client_sock, client_info = self.server_sock.accept()
          print "Accepted connection from ", client_info
          self.animationRunner.animate(OneTime(anim.animations.paired))
          while True:
              try :
                  self.notificationQueue.put(self.receiveAlllData())
              except:

                  self.client_sock.close()
                  self.server_sock.close()
                  break

