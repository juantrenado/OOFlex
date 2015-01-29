# -*- coding: utf-8 -*-

from OOFlex.files.File import File

class CSVWriter( File ):
  """Parent class of CSVRead and CSVWrite subclasses
  """
  def __init__( self, name, rawdata, flag  ):
    super( CSVWriter, self ).__init__( name, "w" )
    self.__file = None
    self.__flag = flag
    self.__header = [ "MEDMeasure", "MEDCurrent", "MEDValid Flag", "MEDMin", "MEDMax", "MEDMean", "MEDStd.Dev", "MEDNum.Meas" ]
    self.__numExper = None
    self.__data = rawdata
    self.__setNumExper()
    self.__setHeader()
    self.__processRawData()

  @property
  def numExper( self ):
    return self._numExper
    
  def __setNumExper( self ):
    if not self.__flag:
      lengthHeader = len( self.__header ) - 1
    else:
      lengthHeader = len( self.__header )
    self.__numExper = len( self.__data[ 0 ].split( "," ) ) / lengthHeader

  def __setHeader( self ):
    finalHeader = []
    keys = []
    if not self.__flag:
      header = [ head for head in self.__header if "Flag" not in head ]
    else:
      header = self.__header
    experiment = self.__data[ 0 ].split( "," )
    for it in range( self.__numExper ):
      keys.append( experiment[ len( header )*it ][ : experiment[ len( header )*it ].index( "(" ) ].upper() )
    for it, key in zip( range( len( keys ) ), keys ):
      repeats = str( keys[ : it + 1 ].count( key ) )
      headerCopy = [ value.replace( "MED", key + repeats ) for value in header ]      
      finalHeader += headerCopy
    self.__header = finalHeader

  def __processRawData( self ):
    for it in range( len( self.__data ) ):
      self.__data[ it ] = self.__data[ it ].replace( ",", "\t" )
    return self.__data
  
  def writeHeader( self ):
    self.__file.write( "\t".join( self.__header ) + "\n" )

  def writeData( self ):
    self.__file.writelines( self.__data )
    
  def closeCSV( self ):
    self.__file.close()
    
        
if __name__ == "__main__":
  pass
