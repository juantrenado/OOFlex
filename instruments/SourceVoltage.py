# -*- coding: utf-8 -*-

class SourceVoltage( object ):
  """Parent class for source voltage instrumentation
  """

  def __init__( self ):
    self.__voltage = 0.0
    self.__current = 0.001
  
  @property
  def voltage( self ):
    return self.__voltage
   
  @voltage.setter
  def voltage( self, value ):
    self.__voltage = value

  @property
  def current( self ):
    return self.__current

  @current.setter
  def current( self, value ):
    self.__current = value

  def initSourceVoltage( self ):
    for channel in self.channels:
      self.setChannel( channel )
      self.setCurrentLimit( self.current )
      self.setVoltage( self.voltage )
      self.setOFF()

  def setChannel( self, channel ):
    raise Exception( "Implement the set channel function" )
        
  def setVoltage( self, value ):
    raise Exception( "Implement the set voltage function" )
    
  def setCurrentLimit( self, value ):
    raise Exception( "Implement the set current limit function" )

  def setON( self ):
    raise Exception( "Implement the setON function" )

  def setOFF( self ):
    raise Exception( "Implement the setOFF function" )

  def readVoltage( self ):
    raise Exception( "Implement the read voltage function" )

  def readCurrent( self ):
    raise Exception( "Implement the read current function function" )

if __name__ == "__main__":
  pass
