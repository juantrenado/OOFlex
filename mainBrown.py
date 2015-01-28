# -*- coding: utf-8 -*-

from OOFlex.interface.InterfaceFactory import InterfaceFactory
from OOFlex.files.BINWriter import BINWriter


factory = InterfaceFactory( "setupBrown.ini" )
tektronix =  factory.getDevice( "scope" )
tektronix.setChannel( 3 )

tektronix.obtainPreamble()

binwriter = BINWriter( "test.bin" )
binwriter.header = tektronix.preamble
for i in range( 100 ):
  waveform, points, bytesPoint = tektronix.readWaveformBIN()
  binwriter.addData( waveform )
binwriter.bytesPerPoint( bytesPoint )
binwriter.pointsPerMeasurement( points )

binwriter.writeData()
binwriter.close()
