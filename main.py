# -*- coding: utf-8 -*-

import time
from OOFlex.boards.FlexTOT import FlexTOT
from OOFlex.interface.InterfaceFactory import InterfaceFactory
from OOFlex.measurement.Measure import Measure
from OOFlex.measurement.WriteCSV import WriteCSV


factory = InterfaceFactory( "setup.ini" )
agilent =  factory.getDevice( "lowVoltage" )
agilent.setChannel( "P6" )
agilent.setVoltage( 5 )
agilent.setCurrentLimit( 0.300 )
agilent.setON()
time.sleep( 1 )

confRange = "low"
flexID = "FLEX0202" 
flextot = FlexTOT( flexID, confRange )
time.sleep( 0.3 )


keithley2612 = factory.getDevice( "highVoltage" )
keithley2612.setChannel( "A" )
keithley2612.setVoltage( 69.0 )
keithley2612.setCurrentLimit( 0.001 )
keithley2612.setON()

scope = factory.getDevice( "scope" )
measure = Measure( 5000 )
for th in range( 62, 50, -1 ):
  measure.resetMeas()
  flextot.setTimeThreshold( 14, th )
  while len( measure.meas ) < measure.numMeas:      
      medida = scope.adquisition()
      if measure.checkMeasure( medida ):
        measure.addMeas( medida )
        time.sleep( 0.01 )
      if len( measure.meas ) % 100 == 0:
        print len( measure.meas )     
  testFile = WriteCSV( "data-th" + str( th ) + ".csv", measure.meas, False )
  testFile.processMeasures()
  testFile.writeHeader()
  testFile.writeData()
  testFile.closeCSV()

