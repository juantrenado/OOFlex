# -*- coding: utf-8 -*-

from OOFlex.files.File import File
import sys
import struct

class BINReader( File ):
  """Child class to read binary files
  """
  def __init__( self, name ):
    super( BINReader, self ).__init__( name, "rb" )
    self.measurements = None
    self.points = None
    self.bytesPerPoint = None

  def readData( self ):
    bindata = self.dataFile.read()
    header = [ fields for fields in struct.unpack( 6 * 'd', bindata[ :48 ] ) ]
    self._setHeader( header )
    self.measurements = struct.unpack( 'h', bindata[ 48 : 50 ] )[ 0 ]
    self.points = struct.unpack( 'h', bindata[ 50 : 52 ] )[ 0 ]
    self.bytesPerPoint = struct.unpack( 'h', bindata[ 52 : 54 ] )[ 0 ]
    data = list( struct.unpack( self.measurements * self.points * 'h', bindata[ 54 : ] ) )
    waveforms = []
    for i in range( self.measurements ):
      waveforms.append( data[ i * self.points : ( i + 1 ) * self.points ] )
    self.data = waveforms       

  def _setHeader( self, data ):
    self.header = { "xincr" : data[ 0 ], "pt_off" : data[ 1 ], "xzero" : data[ 2 ], "ymult" : data[ 3 ], "yzero" : data[ 4 ], "yoff" : data[ 5 ] }
 

if __name__ == "__main__":
  pass
