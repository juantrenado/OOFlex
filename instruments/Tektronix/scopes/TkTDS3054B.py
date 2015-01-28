# -*- coding: utf-8 -*-

from OOFlex.instruments.Tektronix.scopes.TektronixScope import TektronixScope

class TkTDS3054B( TektronixScope ):
  """Class to control the Agilent scopes by gpib
  """
  
  def __init__( self, interface ):
    super( TkTDS3054B, self ).__init__( interface )
    self.__preamble = { "xincr" : 0, "pt_off" : 0, "xzero" : 0, "ymult" : 0, "yzero" : 0, "yoff" : 0 }

  @property
  def preamble( self ):
    return self.__preamble
  
  def obtainPreamble( self ):
    self.interface.write( "WFMPre?" )
    preamble = self.interface.read().split( ";" )
    self.__preamble[ "yoff" ]   = float( preamble[ -2 ] )
    self.__preamble[ "yzero" ]  = float( preamble[ -3 ] )
    self.__preamble[ "ymult" ]  = float( preamble[ -4 ] )
    self.__preamble[ "xzero" ]  = float( preamble[ -6 ] )
    self.__preamble[ "pt_off" ] = float( preamble[ -7 ] )
    self.__preamble[ "xincr" ]  = float( preamble[ -8 ] )

  def readWaveformBIN( self ):
    nr_pt = "10000"
    byt_nr = "2"
    self.interface.write( "WFMPre:ENCdg BIN" )
    self.interface.write( "WFMPre:BYT_Or MSB" )
    self.interface.write( "WFMPre:BN_Fmt RP" )
    self.interface.write( "WFMPre:BYT_Nr " + byt_nr )
    self.interface.write( "WFMPre:NR_Pt " + nr_pt )
    self.interface.write( "DATa:STARt " + "1" )
    self.interface.write( "DATa:STOP " + nr_pt )
    self.interface.write( "DATa:ENCdg RIBinary" )
    self.interface.write( "CURVe?" )
    data = self.interface.read( int( byt_nr ) * int( nr_pt ) + 6 )  #The scope in binary sends 6 bytes of trash
                                                                    # at the begining of the message.
    return data[ 6: ], nr_pt, byt_nr

  def readWaveformASC( self ):
    nr_pt = "10000"
    byt_nr = "2"
    self.interface.write( "WFMPre:ENCdg ASC" )
    self.interface.write( "WFMPre:NR_Pt " + nr_pt )
    self.interface.write( "WFMPre:BYT_Nr " + byt_nr )
    self.interface.write( "DATa:STARt " + "1" )
    self.interface.write( "DATa:STOP " + nr_pt )
    self.interface.write( " CURVe?" )
    data = self.interface.read()
    while data[ -1 ] != "\n":    
        data += self.interface.read()
    return data, nr_pt, byt_nr


if __name__ == "__main__":
  pass 

