# -*- coding: utf-8 -*-

class CSVFile( object ):
  """Parent class of CSVRead and CSVWrite subclasses
  """
  def __init__( self, name ):
    self.__name = name
    self.__bufferLength = 10000
    
  @property
  def name( self ):
    return self.__name
  
if __name__ == "__main__":
  pass
  
    
