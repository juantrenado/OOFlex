# -*- coding: utf-8 -*-

import sys
import time
import subprocess
from OOFlex.Core.Conf import Conf

class FlexTOT( object ):
  """Class to configure and control the FlexTOT board
  """
  def __init__( self, flexId, confRange, firmware = "FlexTOTdemo.rbf" ):
    
    self._flexId = flexId
    self._firmware = self.__setFirmware( firmware )
    self._confFile = self.__setConfFile( confRange )
    self._exePath = Conf().exePath
    self.__loadFirmware()
    self.__loadConfiguration()
        
  def __setConfFile( self, confRange ):
    return Conf().confPath + "/" + self._flexId + "/" + self._flexId + "_"+ confRange + ".conf"
  
  def __setFirmware( self, firmware ):
    return Conf().firmwarePath + "/" + firmware

  def __loadFirmware ( self ):
    process = subprocess.Popen( [ self._exePath, self._flexId, "-f", self._firmware ], shell = False, stdout=subprocess.PIPE )
    print process.communicate()[ 0 ]
    time.sleep( 0.3 )
    
  def __loadConfiguration( self ):
    process = subprocess.Popen( [ self._exePath, self._flexId, "-l", self._confFile ], shell = False, stdout=subprocess.PIPE )
    print process.communicate()[ 0 ]
    time.sleep( 0.3 )    

  def setIr( self, value ):
    process = subprocess.Popen( [ self._exePath, self._flexId, "-ir", str( value ) ], shell = False, stdout=subprocess.PIPE )
    print process.communicate()[ 0 ]
    time.sleep( 0.3 )    
  
  def setPa( self, value ):
    process = subprocess.Popen( [ self._exePath, self._flexId, "-pa", str( value ) ], shell = False, stdout=subprocess.PIPE )
    print process.communicate()[ 0 ]
    time.sleep( 0.3 )    

  def setTimeThreshold( self, channel, value ):
    confFile = open( self._confFile )
    for confLine in confFile.readlines():
      if "-ch" + str( channel ) in confLine:
        break
    confFile.close()
    confLine = confLine.split( " " )
    confLine[ -2 ] = str( value )
    process = subprocess.Popen( [ self._exePath, self._flexId ] + confLine, shell = False, stdout=subprocess.PIPE )
    print process.communicate()[ 0 ]
    time.sleep( 0.3 )    
  
if __name__ == "__main__":
  pass

