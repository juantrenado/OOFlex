# -*- coding: utf-8 -*-

class File( object ):
  """Parent class to handle CSV and BIN files
  """
  def __init__( self, name, mode ):
    self.__dataFile = None
    self.__name = name
    self.__bufferLength = 10000
    self.__header = ""
    self.__data = ""
    self.__open( mode )

  @property
  def dataFile( self ):
    return self.__dataFile

  @dataFile.setter
  def dataFile( self, dataFile ):
      self.__dataFile = dataFile

  @property
  def name( self ):
    return self.__name
  
  @property
  def header( self ):
    return self.__header

  @header.setter
  def header( self, header ):
    self.__header = header

  @property
  def data( self ):
    return self.__data

  @data.setter
  def data( self, data ):
    self.__data = data

  def __open( self, mode ):
    try:
      self.dataFile = open( self.name, mode )
    except IOError:
      raise Exception( "Hmmm... sth happened in the file creation process " )

  def close( self ):
    try:
      self.dataFile.close()
    except IOError:
      raise Exception( "Hmmm... sth happened in the closing file process")


if __name__ == "__main__":
  pass
  
    
