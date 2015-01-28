# -*- coding: utf-8 -*-

import usbtmc
from OOFlex.interface.Interface import Interface

class UsbInterface( Interface ):
  """Usb Interface class
  """

  #For USB, address has the form of usb://idVendor:idProduct
  def __init__( self, idVendor, idProduct ):
    super( UsbInterface, self ).__init__()
    self.__idVendor = int( idVendor, 16 )
    self.__idProduct = int( idProduct, 16 )
    self.__setConnection()
    
  def __setConnection( self ):
    self.interface = usbtmc.Instrument( self.__idVendor, self.__idProduct )    

  @property
  def ipProduct( self ):
    return self.__idProduct
  
  @property
  def idVendor( self ):
    return self.__idVendor

  def write( self, buf ):
    self.interface.write( buf )

  def read( self ):
    data = self.interface.read()
    return data

if __name__ == "__main__":
  pass
