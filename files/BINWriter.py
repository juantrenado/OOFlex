# -*- coding: utf-8 -*-

from OOFlex.files.File import File
import struct

class BINWriter( File ):
  """Child Class of File to handle binary data
  """
  def __init__( self, name ):
    super( BINWriter, self ).__init__( name, "wb" )
    self.__numExper = None
    self._pointsMeasurement = 0
    self._bytesPoint = 0

  def addData( self, data ):
    addedData = self.data + data
    self.data = addedData

  def bytesPerPoint( self, value ):
    self._bytesPoint = int( value )
    
  def pointsPerMeasurement( self, value ):
    self._pointsMeasurement = int( value )

  def __packData( self ):
    """ File format
      6 doubles (8bytes per double): xincr, pt_off, xzero, ymult, yzero, yoff
      1 short (2bytes): Number of measurements.
      1 short: Points per measurement.
      1 short: Bytes per point.
      The rest is the data, short per point. This can be configured in the scope to acquiere using 1 or 2 bytes per point.

      The equations to recover the data:
        Xn = xzero + xincr * ( n - pt_off )
        Yn = yzero + ymult * ( yn - yoff )
    """
    packedData = str( struct.pack( 6 * 'd' , self.header[ "xincr" ], self.header[ "pt_off" ], self.header[ "xzero" ], self.header[ "ymult" ], self.header[ "yzero" ], self.header[ "yoff" ] ) ) + str( struct.pack( 'h', len( self.data ) / ( self._pointsMeasurement * self._bytesPoint ) ) ) + str( struct.pack( 'h', self._pointsMeasurement ) ) + str( struct.pack( 'h', self._bytesPoint ) ) + self.data
    return packedData    
  
  def writeData( self ):
    data = self.__packData()
    self.dataFile.write( data )
    
        
if __name__ == "__main__":
  pass
