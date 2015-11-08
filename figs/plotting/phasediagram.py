import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as colormaps
import matplotlib.backends.backend_pdf
import time
import scipy.io
from os.path import exists
from os import mkdir
import h5py
from itertools import cycle
import matplotlib.gridspec as gridspec
import re

all_markers = ( 'o','s', 'v', '^', '<', '>', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','1', '2', '3', '4', '8','.', ',')
all_colors = map( lambda x:[k/255. for k in x], ((228,26,28), (55,126,184), (77,175,74), (152,78,163), (255,127,0), (255,255,51), (166,86,40), (247,129,191), (153,153,153) ))

class MyLogFormatter(matplotlib.ticker.LogFormatterMathtext):
    def __call__(self, x, pos=None):
        # call the original LogFormatter
        rv = matplotlib.ticker.LogFormatterMathtext.__call__(self, x, pos)

        # check if we really use TeX
        if matplotlib.rcParams["text.usetex"]:
            # if we have the string ^{- there is a negative exponent
            # where the minus sign is replaced by the short hyphen \mathchardef\mhyphen="2D'
            rv = re.sub(r'\^\{-', r'^{\mhyphen', rv)

        return rv

def main():

	matplotlib.rc('text', usetex=True)
	matplotlib.rc('ps', usedistiller='xpdf')
	matplotlib.rcParams["text.latex.preamble"].append(r'\mathchardef\mhyphen="2D')


	outputfile_name = r'data\oblatephasediagram.h5'
	output_file = h5py.File(outputfile_name, 'r')

	d = np.array(output_file['/d'][:,:])
	four = np.array(output_file['/fourfixedpoints'][:,:])
	two = np.array(output_file['/twofixedpoints'][:,:])
	t = np.array(output_file['/tumblingstable'][:,:])

	fig1 = plt.figure(1, figsize=(10/2.54, 8/2.54))
	gs = gridspec.GridSpec(1, 1, bottom=0.15, left=0.2,hspace=0.05,wspace=0.21,top=.95,right=.9)
	
	ax = plt.subplot(gs[0])
	t=np.vstack(( t,np.array([0.245,3.72])) )
	ax.loglog(d[:,0],d[:,1], color='black',lw=1)
	ax.loglog(four[:,0],four[:,1], color='black',lw=1)
	ax.loglog(two[:,0],two[:,1], color='black',lw=1)
	ax.loglog(t[:,0],t[:,1], color='black',lw=1)
	ax.loglog(0.245,3.72,marker='o',ms=7,color='#E41A1C')


	ax.annotate("",
		xy=(1./32, 4e-1), xycoords='data',
		xytext=(1./30, 1), textcoords='data',
                arrowprops=dict(arrowstyle="->", #linestyle="dashed",
                	color="black",
                	shrinkA=5, shrinkB=5,
                	patchA=None,
                	patchB=None,
                	connectionstyle="arc3,rad=0.1",
                	),
                )


	ax.set_xlim(1./40,1)
	ax.set_ylim(0.1,80)
	ax.set_xlabel(r'$\lambda$')
	ax.set_ylabel(r'$\textrm{Re}_s$')

	print "Starting export..."
#	if not exists("output/"):
#		mkdir("output")
	pp = matplotlib.backends.backend_pdf.PdfPages('../phasediagram.pdf')
	pp.savefig(fig1)
	pp.close()




	plt.show()
	print "Done!"

if __name__ == '__main__':
	main()