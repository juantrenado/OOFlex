# -*- coding: utf-8 -*-

import pylab
import numpy as np
from scipy import optimize


####  Esto está por terminar!!!! ####

class Fit( object ):

  __funcMap = { 'gauss' : self.gauss }

  def __init__( self, function ):
    self.fitFunction = set
  
  def setFit( self, n, bins, fitfunc, *args, **kwargs ):
    """fitCutini and fitCutEnd as kwargs"""
    if kwargs.__contains__( "fitCutini" ):
      fitCutini = kwargs[ "fitCutini" ]
    else:
      fitCutini = 0
    if kwargs.__contains__( "fitCutend" ):
      fitCutend = kwargs[ "fitCutend" ]
    else:
      fitCutend = -1
    
    bin_centres = ( bins[ :-1 ] + bins[ 1: ] ) / 2
    p0 = list( args )
    p1, success = optimize.leastsq( self.errorFunction, p0[ : ], args = ( bin_centres[ fitCutini : fitCutend ], n[ fitCutini : fitCutend ] ) )
    pylab.plot( bin_centres[ fitCutini : fitCutend ], fitfunc( p1, bin_centres[ fitCutini : fitCutend ] ), 'r-' )
    return p1, success, bin_centres
  
  def errorFunction( self, fitfunc, p, x, y ):
    return fitfunc( p, x ) - y

  def gauss( self, p, x ):
    if p[ 2 ] > 0
      return p[ 0 ] * np.exp( -( x - p[ 1 ] )**2/( 2 * p[ 2 ]**2 ) )
    else:
      raise Exception( "Negative Sigma argument" )


