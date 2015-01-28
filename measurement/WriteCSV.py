# -*- coding: utf-8 -*-



class WriteCSV( object ):
  def __init__( self, name, measures, flag ):
    self._name = name
    self._flag = flag
    self._header = [ "MEDMeasure", "MEDCurrent", "MEDValid Flag", "MEDMin", "MEDMax", "MEDMean", "MEDStd.Dev", "MEDNum.Meas" ]
    self._numExper = None
    self.measures = measures
    self.csvfile = open( self._name, "w" )
    self.__setNumExper()
    self.__setHeader()
    
         
  @property
  def name( self ):
    return self._name
  
  @property
  def numExper( self ):
    return self._numExper

  def __setNumExper( self ):
    if not self._flag:
      lengthHeader = len( self._header ) - 1
    else:
      lengthHeader = len( self._header )
    self._numExper = len( self.measures[ 0 ].split( "," ) ) / lengthHeader

  def __setHeader( self ):
    finalHeader=[]
    keys = []
    if not self._flag:
      header = [ head for head in self._header if "Flag" not in head ]
    else:
      header = self._header
    experiment = self.measures[ 0 ].split( "," )
    for it in range( self._numExper ):
      keys.append( experiment[ len( header )*it ][ : -3 ].upper() )
    for it, key in zip( range( len( keys ) ), keys ):
      repeats = str( keys[ : it + 1 ].count( key ) )
      headerCopy = [ value.replace( "MED", key + repeats ) for value in header ]      
      finalHeader += headerCopy
    self._header = finalHeader
  
  def processMeasures( self ):
    for it in range( len( self.measures ) ):
      self.measures[ it ] = self.measures[ it ].replace( ",", "\t" )
    return self.measures   
  
  def writeHeader( self ):
    self.csvfile.write( "\t".join( self._header ) + "\n" )

  def writeData( self ):
    self.csvfile.writelines( self.measures )
    
  def closeCSV( self ):
    self.csvfile.close()
    
    
if __name__ == "__main__":
  pass
  
    
