# -*- coding: utf-8 -*-

from OOFlex.files.File import File
import sys

class CSVReader( File ):
  """Parent class of CSVRead and CSVWrite subclasses
  """
  def __init__( self, name ):
    super( CSVReader, self ).__init__( name )
    self.__file = None
    self.__header = None
    self.__numLines = None
    self.__data = {}

  @property
  def data( self ):
    return self.__data
    
  @property
  def header( self ):
    return self.__header

  def __open( self ):
    try:
      self.__file = open( self.name, "r" )
    except IOError:
      raise Exception( "Hmmm... check file name %s" % self.__name )

  def __getHeader( self ):
    self.__file.seek( 0 )
    self.__header = self.__file.readline().split( "\t" )
    for label in self.__header:
      self.data[ label ] = []
  
  def cleanData( self ):
    raise Exception( "Write the method for clean data" )
    """
    ***Example of cleanData implementation***
    def cleanData( self, data ):
      keys = [ key for key in self.header if "Valid Flag" in key ]
      currents = [ key for key in self.header if "Current" in key ]
      for key in keys:
        for it in range( len( data[ key ] )-1, -1, -1 ):
          if data[ key ][ it ] > 1:
            for llave in currents + keys:
              del data[ llave ][ it ]   
      return data
    """
    
  def getData( self ):
    self.__open()
    self.__getHeader()
    lines = self.__file.readlines()
    for line in lines:
      line = line.split( "\t" )
      for label, datum in zip( self.__header, line ):
        if "Measure" in label:
          self.__data[ label ].append( datum )
        else:
          self.__data[ label ].append( float( datum ) )
      self.__file.close()
    return self.__data

          
if __name__ == "__main__":
  reader = CSVRead( sys.argv[ 1 ] )
  reader.getData()
  print reader.data
