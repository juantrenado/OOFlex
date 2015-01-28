# -*- coding: utf-8 -*-

import ConfigParser

from OOFlex.interface.GpibInterface import GpibInterface
from OOFlex.interface.UsbInterface import UsbInterface
from OOFlex.interface.EthernetInterface import EthernetInterface

from OOFlex.instruments.Agilent.scopes.AgMSOX3034A import AgMSOX3034A
from OOFlex.instruments.Agilent.scopes.AgMSO9404A import AgMSO9404A
from OOFlex.instruments.Agilent.svoltage.AgE3631A import AgE3631A
from OOFlex.instruments.Keithley.svoltage.Kth2611A import Kth2611A
from OOFlex.instruments.Keithley.svoltage.Kth2612 import Kth2612
from OOFlex.instruments.Tektronix.scopes.TkTDS3054B import TkTDS3054B

class InterfaceFactory( object ):
  """Factory class to build up classes for instrumentation interface
  """
  
  __connMap = { 'gpib': GpibInterface,
                'tcp' : EthernetInterface,
                'usb' : UsbInterface }

  __instrMap = {  "AgE3631A" : AgE3631A, 
                  "Kth2611A" : Kth2611A, 
                  "Kth2612" : Kth2612, 
                  "AgMSOX3034A" : AgMSOX3034A, 
                  "AgMSO9404A" : AgMSO9404A, 
                  "TkTDS3054B" :  TkTDS3054B }


  def __init__( self, iniFile ):
    self.__iniFile = iniFile
    self.__setup = self.__parser()

  @property
  def setup( self ):
    return self.__setup

  @property
  def iniFile( self ):
    return self.__iniFile

  def __parser( self ):
    setup = {}
    config = ConfigParser.RawConfigParser()
    config.read( self.__iniFile )
    for section in config.sections():
      setup[ section ] = {}
      for item in config.items( section ):
        setup[ section ][ item[ 0 ] ] = item[ 1 ] 
    return setup

  def __buildInterface( self, ifAddr ):
    fields = ifAddr.split( "://" )
    if len( fields ) != 2:
      raise Exception( "OOps. Something happened. The interface address seems bogus (%s)" % ifAddr )
    ifType = fields[ 0 ]
    try:
      ifClass = InterfaceFactory.__connMap[ ifType ]
    except KeyError:
      raise Exception( "Hmm... Don't know how to build an %s interface" % ifType )
    ifAddr = fields[ 1 ].split( ":" )
    if ifType == 'gpib' and len( ifAddr ) == 1:
      ifAddr.append( '0' )
    if len( ifAddr ) != 2:
      raise Exception( "Hmm... Address seems invalid %s" % fields[ 1 ] )
    return ifClass( *ifAddr )
    
  def getDevice( self, instr ):
    if instr not in self.__setup.keys():
      raise Exception( "Hmm... Instrument invalid %s" % instr )
    iface = self.__buildInterface( self.__setup[ instr ][ "address" ] )
    instr = InterfaceFactory.__instrMap[ self.__setup[ instr ][ "device" ] ]
    return instr( iface )

if __name__ == "__main__":
  factory = InterfaceFactory( "setup.ini" )
  device = factory.getDevice( "Bigscope" )
  print device.getId()
