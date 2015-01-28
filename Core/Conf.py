# -*- coding: utf-8 -*-

class Conf( object ):

  def __init__( self ):
    self.__exePath = "/home/acomerma/FlexTOTdemo_sw/FlexTOT"
    self.__confPath = "/home/acomerma/FlexTOTdemo_python/FlexDemo/data/confs"
    self.__firmwarePath = "/home/acomerma/FlexTOTdemo_sw"
    self.__sourceVoltageExePath = "/home/acomerma/Escritorio/Control"

  @property
  def exePath( self ):
    return self.__exePath

  @property
  def confPath( self ):
    return self.__confPath

  @property
  def firmwarePath( self ):
    return self.__firmwarePath

  @property
  def sourceVoltageExePath( self ):
    return self.__sourceVoltageExePath

if __name__ == "__main__":
  pass
