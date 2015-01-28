# -*- coding: utf-8 -*-

from OOFlex.instruments.SourceVoltage import SourceVoltage

class AgE3631A( SourceVoltage ):
  """Class to control the Agilent source voltage using gpib
  """

  def __init__( self, interface ):
    super( AgE3631A, self ).__init__()
    self.channels = [ "P6", "P25", "N25" ]
    self.interface = interface
    self.initSourceVoltage()

  def setChannel( self, channel ):
    self.interface.write( 'INST ' + channel + 'V' )
    
  def setVoltage( self, value ):
    self.voltage = value
    self.interface.write( 'VOLT ' + str( self.voltage ) )
    
  def setCurrentLimit( self, value ):
    self.current = value
    self.interface.write( 'CURR ' + str( self.current ) )

  def setON( self ):
    self.interface.write( 'OUTP ON' )

  def setOFF( self ):
    self.interface.write( 'OUTP OFF' )

  def readVoltage( self ):
    pass

  def readCurrent( self ):
    pass
    
if __name__ == "__main__":
  pass
