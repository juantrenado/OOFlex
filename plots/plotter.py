# -*- coding: utf-8 -*-

from OOFlex.files.BINReader import BINReader
    
import argparse
import numpy
import pylab
import time
import sys


def data2wave( data, preamble ):
  ywave = []
  xwave = []
  for i in range( len( data ) ):
    ywave.append( preamble[ "yzero" ] + preamble[ "ymult" ] * ( float( data[ i ] ) - preamble[ "yoff" ] ) )
    xwave.append( preamble[ "xzero" ] + preamble[ "xincr" ] * ( i - preamble[ "pt_off" ] ) )
  return xwave, ywave

def plot_parameters( plots ):
  pylab.rcParams[ 'lines.linewidth' ] = 2
  pylab.rcParams[ 'lines.markeredgewidth' ] = 2
  pylab.rcParams[ 'lines.markersize' ] = 5
  pylab.rcParams[ 'font.size' ] = 21 - plots/2
  pylab.rcParams[ 'font.weight' ] = 'semibold'
  pylab.rcParams[ 'axes.linewidth' ] = 2
  pylab.rcParams[ 'axes.titlesize' ] = 25 - plots/2
  pylab.rcParams[ 'axes.labelsize' ] = 22 - plots/2
  pylab.rcParams[ 'axes.labelweight' ] = 'semibold'
  pylab.rcParams[ 'ytick.major.pad' ] = 10 - plots/4
  pylab.rcParams[ 'xtick.major.pad' ] = 10 - plots/4
  pylab.rcParams[ 'legend.fontsize' ] = 21 - plots/1.5
  pylab.rcParams[ 'grid.linewidth' ] = 1.5

def plotdata( xdata, ydata, cont ):
  pylab.plot( xdata, ydata, "-", label = "waveform" + str( cont ) )
  pylab.ticklabel_format( style = 'sci', scilimits = ( 0, 0 ) )
  pylab.xlabel( "Time [s]" )
  pylab.ylabel( "Signal [V]" )
  pylab.legend( loc = 1 )
  pylab.grid()


def parseador():
  parser = argparse.ArgumentParser( description = "Plot data in scatter format from a binary file" )
  parser.add_argument( "filename", help = "binary file name" )
  parser.add_argument( "-p", "--plots", type = int, default = 1, choices = range( 1, 37 ), help = "number of plots per canvas. Allowed values are 1 to 36", metavar = ""  )
  parser.add_argument( "-c", "--canvas", nargs = 2, type = int, default = [ 1 , 1 ], choices = range( 1, 5 ), help = "number of columns and rows per canvas. Allowed values are 1 to 4", metavar = "" )
  args = parser.parse_args()
  if args.plots > args.canvas[ 0 ] * args.canvas[ 1 ]:
    rows = 1
    columns = 1
    while rows**2 < args.plots:
      rows += 1
    args.canvas=[ rows, int( numpy.ceil( args.plots/float( rows ) ) ) ]
  print args  
  return args


if __name__ == "__main__":
  args = parseador() 
  binreader = BINReader( args.filename )
  binreader.readData()
  data = binreader.data
  header = binreader.header
  binreader.close()

  fig = pylab.figure( 1, ( 25, 15 ) )
  plot_parameters( args.plots )
  for i in range( args.plots ):
    ax = fig.add_subplot( args.canvas[ 0 ], args.canvas[ 1 ], i + 1 )
    xwave, ywave = data2wave( data[ i ], header )
    plotdata( xwave, ywave, i)
pylab.tight_layout()
pylab.show()
