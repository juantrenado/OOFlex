# -*- coding: utf-8 -*-

import gpib
from OOFlex.interface.Interface import Interface

class GpibInterface( Interface ):
  """Gpib Interface class
  """
  
  #For GPIB, address has the form of gpib://gpibAdress(:systemDevice)
  def __init__( self, address, device ):
    super( GpibInterface, self ).__init__()
    self.__address = int( address )
    self.__device = int( device )
    self.__setConnection()
    
  def __setConnection( self ):
    self.__interface = gpib.dev( self.__device, self.__address ) 

  @property
  def address( self ):
    return self.__address
  
  @property
  def device( self ):
    return self.__device
    
  def write( self, buf ):
    gpib.write( self.__interface, buf ) 
    
  def read( self, length = 512 ):
    data = gpib.read( self.__interface, length )
    return data

if __name__ == "__main__":
  pass
