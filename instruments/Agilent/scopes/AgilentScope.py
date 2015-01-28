# -*- coding: utf-8 -*-

class AgilentScope( object ):
  """Class to control the Agilent scopes by usb
  """
  def __init__( self, interface ):
    self.interface = interface
    
  def getId( self ):
    self.interface.write( "*IDN?\n" )
    return self.interface.read()
    
  def clearDisplay( self ):
    self.interface.write( "CDISplay\n" )

  def adquisition( self ):
    self.interface.write( ":MEASure:RESults?\n" )
    data = self.interface.read()
    return data

  def single( self ):  
    self.interface.write( ":SINGle\n" )
    
  def stop( self ):
    self.interface.write( ":STOP\n" )
  
  def run( self ):
    self.interface.write( ":RUN\n" )  

  def write( self , cadena ):
    self.interface.write( cadena )
    
  def read( self ):
    data = self.interface.read()
    return data

if __name__ == "__main__":
 
  scope = AgilentScope( 0x0957, 0x17a4 )
  print scope.adquisition()
