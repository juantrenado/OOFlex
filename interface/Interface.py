# -*- coding: utf-8 -*-

class Interface( object ):
  """Interface parent class
  """
  def read( self ):
    raise Exception( "Inplement the read function you moron!" )
  
  def write( self, buf ):
    raise Exception( "Inplement the write function you moron!" )

     
if __name__ == "__main__":
  pass
