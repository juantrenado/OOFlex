# -*- coding: utf-8 -*-

import time

class Measure( object ):
  """Class to obtain 'n' number of measures with AgilentScope
  """
  def __init__( self, numMeas ):
    self.__numMeas = numMeas
    self.__previousMeas = "THISWILLNEVERMATCH"
    self.__meas = []
    
  @property  
  def meas( self ):
    return self.__meas
  
  def checkMeasure( self, value ):
    if value != self.__previousMeas:
      self.__previousMeas = value
      return True
    time.sleep( 0.01 )
    return False
    
  def addMeas( self, value ):
    if "\n" not in value:
      value += "\n"
    self.__meas.append( value )
    
  def resetMeas( self ):
    self.__meas = []  
    
  @property
  def numMeas( self ):
    return self.__numMeas
   
    
if __name__ == "__main__":
  pass
