# -*- coding: utf-8 -*-

import sys
import pylab
import numpy as np
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


def plot_parameters():
  pylab.rcParams[ 'lines.linewidth' ] = 4
  pylab.rcParams[ 'lines.markeredgewidth' ] = 2
  pylab.rcParams[ 'lines.markersize' ] = 5
  pylab.rcParams[ 'font.size' ] = 18
  pylab.rcParams[ 'font.weight' ] = 'semibold'
  pylab.rcParams[ 'axes.linewidth' ] = 2
  pylab.rcParams[ 'axes.titlesize' ] = 25
  pylab.rcParams[ 'axes.labelsize' ] = 22
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


def rowColums( value ):
  rows = 1
  while True:
    if rows**2 < value:
      rows += 1
    else:
      return rows


def plot1( x, y, rows, count ):
  fig = pylab.figure( 1, ( 35, 21 ) )
  plot_parameters()
  ax = fig.add_subplot( rows, rows, count )
  pylab.plot( 1e9 * np.array( x ), 1e9 * np.array( y ), "o", fillstyle = 'none', label = ( fileName.split( "-" )[ 0 ] + "-th" + str( threshold ) ) )
  pylab.legend( loc = 0 )
  pylab.ylabel( "Energy(ns)" )
  pylab.xlabel( "Time(ns)" )
  pylab.grid( True )


def plot2( x, rows, count ):
  fig = pylab.figure( 2, ( 35, 21 ) )
  plot_parameters()
  ax = fig.add_subplot( rows, rows, count )
  pylab.hist( 1e9 * np.array( x ), 50, histtype = "step", label = ( fileName.split( "-" )[ 0 ] + "-th" + str( threshold ) ), linewidth = 2 )
  pylab.legend( loc = 0 )
  pylab.xlabel( "Energy(ns)" )
  pylab.grid( True )

ficheros = arg2dict( sys.argv[ 1: ] )
rows = rowColums( len( sys.argv[ 1: ] ) / 2 )
count = 0
for voltage in ficheros.keys():
  thresholds = sorted( ficheros[ voltage ].keys() )
  for threshold in thresholds:
    count += 1
    for fileName in ficheros[ voltage ][ threshold ]:
      reader = Reader( fileName )
      data = reader.getData()
      data = reader.cleanData( data )
      currents = [ key for key in reader.header if "Current" in key ]
      plot1( data[ currents[ 0 ] ], data[ currents[ 1 ] ], rows, count )
      plot2( data[ currents[ 1 ] ], rows, count )
#pylab.show()
fig = pylab.figure( 1, ( 21, 18 ) )
pylab.tight_layout()
pylab.savefig( "phoswich.png" )
fig2 = pylab.figure( 2, ( 21, 18 ) )
pylab.tight_layout()
pylab.savefig( "hist.png" )


