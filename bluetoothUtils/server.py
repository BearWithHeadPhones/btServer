from bluetooth import *
import threading
from interface import btMessage_pb2


class BTServer (threading.Thread):
   def __init__(self, notificationQueue):
      threading.Thread.__init__(self)
      #self.daemon = True
      self.notificationQueue = notificationQueue

   def run(self):

    while True:
          server_sock = BluetoothSocket(RFCOMM)
          server_sock.bind(("", PORT_ANY))
          server_sock.listen(1)
          port = server_sock.getsockname()[1]
          uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
          advertise_service(server_sock, "BTServer",
                             service_id=uuid,
                             service_classes=[uuid, SERIAL_PORT_CLASS],
                             profiles=[SERIAL_PORT_PROFILE],
                             #                   protocols = [ OBEX_UUID ]
                             )
          print "waiting for connection"
          client_sock, client_info = server_sock.accept()
          print "Accepted connection from ", client_info
          while True:
              global serializedMessage

              try :
                serializedMessage = client_sock.recv(1024)
              except:
                  break
                  clien_sock.close()
                  server_sock.close()

              deserializedMessage = btMessage_pb2.BTMessage()
              deserializedMessage.ParseFromString(serializedMessage)
              self.notificationQueue.put(deserializedMessage)



