# -*- coding: utf-8 -*-

import sys
import pylab
import numpy as np
from scipy import optimize
from OOFlex.csvfiles.CSVReader import CSVReader


class Reader( CSVReader ):

  def __init__( self, name ):
    super( Reader, self ).__init__( name )
    
  def cleanData( self, data ):
    keys = [ key for key in self.header if "Valid Flag" in key ]
    currents = [ key for key in self.header if "Current" in key ]
    for key in keys:
      for it in range( len( data[ key ] )-1, -1, -1 ):
        if data[ key ][ it ] > 1:
          for llave in currents + keys:
            del data[ llave ][ it ]   
    return data


fitfunc = lambda p, x: p[ 0 ] * np.exp( -( x - p[ 1 ] )**2/( 2 * p[ 2 ]**2 ) ) if p[ 2 ] > 0  else 5000 # Target function
errfunc = lambda p, x, y: fitfunc( p, x ) - y # Distance to the target function

def plot_parameters():
  pylab.rcParams[ 'lines.linewidth' ] = 4
  pylab.rcParams[ 'lines.markeredgewidth' ] = 2
  pylab.rcParams[ 'lines.markersize' ] = 5
  pylab.rcParams[ 'font.size' ] = 20
  pylab.rcParams[ 'font.weight' ] = 'semibold'
  pylab.rcParams[ 'axes.linewidth' ] = 2
  pylab.rcParams[ 'axes.titlesize' ] = 30
  pylab.rcParams[ 'axes.labelsize' ] = 27
  pylab.rcParams[ 'axes.labelweight' ] = 'semibold'
  pylab.rcParams[ 'ytick.major.pad' ] = 10
  pylab.rcParams[ 'xtick.major.pad' ] = 10
  pylab.rcParams[ 'legend.fontsize' ] = 15
  pylab.rcParams[ 'grid.linewidth' ] = 1.5


def arg2dict( arguments ):
  ficheros = {}
  for fd in arguments:
    print fd
    voltage = fd.split( "-" )[ 2 ].replace( ".csv", "" )
    threshold = int( fd.split( "-" )[ 1 ].replace( "th", "" ) )
    if voltage not in ficheros.keys():
      ficheros[ voltage ] = {}
    if threshold not in ficheros[ voltage ].keys():
      ficheros[ voltage ][ threshold ] = []
    ficheros[ voltage ][ threshold ].append( fd )
  return ficheros


def fit( n, bins, a, X0, sigma, fitCutini = 0, fitCutend = -1 ):
  bin_centres = ( bins[ :-1 ] + bins[ 1: ] ) / 2
  p0 = [ a, X0, sigma ] # Initial guess for the parameters
  p1, success = optimize.leastsq( errfunc, p0[ : ], args = ( bin_centres[ fitCutini : fitCutend ], n[ fitCutini : fitCutend ] ) )
  x = np.linspace( bin_centres[ fitCutini ], bin_centres[ fitCutend ], 100 )
  pylab.plot( x, fitfunc( p1, x ), 'r-' )
  return p1, success, bin_centres


def cutTimes( dataEnergy, dataTime, mean, sigma ):
  print mean, sigma
  for it in range( len( dataEnergy )-1, -1, -1 ):
    if 1e9 * dataEnergy[ it ] < mean - sigma or 1e9 * dataEnergy[ it ] > mean + sigma:
      del dataTime[ it ]
  return dataTime


ficheros = arg2dict( sys.argv[ 1: ] )
fig = pylab.figure( 1, ( 18, 15 ) )
plot_parameters()
for voltage in ficheros.keys():
  thresholds = sorted( ficheros[ voltage ].keys() )
  for threshold in thresholds:
    for fileName in ficheros[ voltage ][ threshold ]:
      reader = Reader( fileName )
      data = reader.getData()
      data = reader.cleanData( data )

      ax = fig.add_subplot( 211 )
      print data.keys()
      n, bins, patches = pylab.hist( 1e9 * np.array( data[ "+ WIDTH1Current" ] ), 80, histtype = "step", linewidth = 3 )
      maxValue = np.where( n == n.max() )[ 0 ][ 0 ]
#      maxValue = max( n[ 20 : ] )
#      maxValue_index = list( n ).index( maxValue )
      p1, success, bin_centres = fit( n, bins, 100, bins[ maxValue ], 5, maxValue - 20, maxValue + 10 )
      pylab.xlabel( "Width (ns)" )
      pylab.ylabel( "Counts" )
      print p1, success
      pylab.grid()
#      ydata = fitfunc( p1, bin_centres )

      ax = fig.add_subplot( 212 )
      dataTimes = cutTimes( data[ "+ WIDTH1Current" ], data[ "TIME(31Current" ], p1[ 1 ], p1[ 2 ] )
      meanValue = 1e9 * np.median( dataTimes )
      print "MeanValue:", meanValue
      n, bins, patches = pylab.hist( 1e9 * np.array( dataTimes ), 100, [ meanValue - 5 , meanValue + 5 ], histtype = "step", linewidth = 3 )
      maxValue = np.where( n == n.max() )[ 0 ][ 0 ]
      p1, success, bin_centres = fit( n, bins, 100, bins[ maxValue ], 1, maxValue - 12, maxValue + 10  )
      print p1, success
#      ydata = fitfunc( p1, bin_centres )
#      pylab.plot( bin_centres, ydata, 'r-', linewidth = 3 )

      pylab.xlabel( "Delay (ns)" )
      pylab.ylabel( "Counts" )
      pylab.text( 0.5, 0.7 ,"SPTR: %.0f(ps)" %( p1[ 2 ] * 1e3 ), transform = ax.transAxes)
      pylab.grid()
      
      print "SPTR: %.0f(ps)" %( p1[ 2 ] * 1e3 )
      pylab.tight_layout()      
      pylab.savefig( fileName.replace( ".csv", ".png" ) )
  pylab.show()

