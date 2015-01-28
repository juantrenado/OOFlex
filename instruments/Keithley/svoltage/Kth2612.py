# -*- coding: utf-8 -*-

from OOFlex.instruments.Keithley.svoltage.KthSourceVoltage import KthSourceVoltage

class Kth2612( KthSourceVoltage ):
  """Class to control the Keithley 2612 source voltage using gpib
  """
  def __init__( self, interface ):
    super( Kth2612, self ).__init__( interface )
    self.channels = [ "A", "B" ]
    self.initSourceVoltage()
    
if __name__ == "__main__":
  pass
