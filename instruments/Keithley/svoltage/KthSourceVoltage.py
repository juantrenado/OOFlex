# -*- coding: utf-8 -*-

from OOFlex.instruments.SourceVoltage import SourceVoltage

class KthSourceVoltage( SourceVoltage ):
  """Parent class to control Keithley source voltage
  """
  def __init__( self, interface ):
    super( KthSourceVoltage, self ).__init__()
    self.interface = interface
    self.channels = None
    self.channel = None

  def setChannel( self, channel ):
    if channel in self.channels:
      self.channel = "smu" + channel.lower()
    else:
      raise Exception( "Invalid channel name" )

  def setVoltage( self, value ):
    self.voltage = str( value )
    self.interface.write( self.channel + '.source.levelv = ' + self.voltage )
    
  def setCurrentLimit( self, value ):
    self.current = str( value )
    self.interface.write( self.channel + ".source.limiti = " + self.current )

  def setON( self ):
    self.interface.write( self.channel + '.source.output = ' + self.channel + '.OUTPUT_ON' )

  def setOFF( self ):
   self.interface.write( self.channel + '.source.output = ' + self.channel + '.OUTPUT_OFF' )
   
    
if __name__ == "__main__":
  pass
