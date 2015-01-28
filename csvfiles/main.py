# -*- coding: utf-8 -*-

import time
from OOFlex.interface.InterfaceFactory import InterfaceFactory
from OOFlex.measurement.Measure import Measure
from OOFlex.csvfiles.CSVWrite import CSVWrite

factory = InterfaceFactory( "setup.ini" )
scope = factory.getDevice( "scope" )
measure = Measure( 10 )
while len( measure.meas ) < measure.numMeas:      
    medida = scope.adquisition()
    if measure.checkMeasure( medida ):
      measure.addMeas( medida )
      time.sleep( 0.01 )
testFile = CSVWrite( "data.csv", measure.meas, False )
testFile.writeHeader()
testFile.writeData()
testFile.closeCSV()

