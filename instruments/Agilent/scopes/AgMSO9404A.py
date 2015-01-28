# -*- coding: utf-8 -*-

from OOFlex.instruments.Agilent.scopes.AgilentScope import AgilentScope

class AgMSO9404A( AgilentScope ):
  """Class to control the Agilent scopes by usb
  """
  
  def __init__( self, interface ):
      super( AgMSO9404A, self ).__init__( interface )

if __name__ == "__main__":
  pass 

