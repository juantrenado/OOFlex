# -*- coding: utf-8 -*-

from OOFlex.instruments.Agilent.scopes.AgilentScope import AgilentScope

class AgMSOX3034A( AgilentScope ):
  """Class to control the Agilent scopes by usb
  """
  
  def __init__( self, interface ):
    super( AgMSOX3034, self ).__init__( interface )

    
if __name__ == "__main__":
  pass
