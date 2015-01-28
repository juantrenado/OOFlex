# -*- coding: utf-8 -*-

import socket
from OOFlex.interface.Interface import Interface

class EthernetInterface( Interface ):
  """Ethernet Interface class
  """
  
  #For ETHERNET, address has the form of eth://address:port
  def __init__( self, ipAddress, port ):
    super( EthernetInterface, self ).__init__()
    self.__ipAddress = ipAddress
    self.__port = int( port )
    self.__setConnection()
  
  def __setConnection( self ):
    self.interface = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    self.interface.connect( ( self.__ipAddress, self.__port ) )
    
  @property
  def ipAddress( self ):
    return self.__ipAddress
  
  @property
  def port( self ):
    return self.__port

  def write( self, buf ):
    self.interface.send( buf )

  def read( self ):
    data = self.interface.recv( 1024 )
    return data

if __name__ == "__main__":
  pass
