# -*- coding: utf-8 -*-

from OOFlex.instruments.Keithley.svoltage.KthSourceVoltage import KthSourceVoltage

class Kth2611A( KthSourceVoltage ):
  """Class to control the Keithley 2611A source voltage using gpib
  """
  def __init__( self, interface ):
    super( Kth2611A, self ).__init__( interface )
    self.channels = [ "A" ] 
    self.initSourceVoltage()
    
if __name__ == "__main__":
  pass
