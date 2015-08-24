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

import matplotlib.gridspec as gridspec
from itertools import cycle
from matplotlib.patches import Ellipse

def main():

	# poincare A
	make("1o00")

	# poincare B
	make("1o10")
	
	# poincare C
	make("1o30")
	
	# poincare D
	make("2o00")
	
	

def make(particle):

	print "making {}".format(particle)

	filename = "poincaredata/{}.mat".format(particle)
	series_files=["poincaredata/series/{}_{}.mat".format(particle,k) for k in xrange(1,4)]

	matplotlib.rc('text', usetex=True)
	matplotlib.rc('ps', usedistiller='xpdf')
	matplotlib.rcParams["text.latex.preamble"].append(r'\mathchardef\mhyphen="2D')

	fig1 = plt.figure(figsize=(12./2.5, 16./2.5))
	
	gs = gridspec.GridSpec(6+6+1,1, hspace=.5,bottom=0.1,left=0.18,right=0.94,top=0.95)

	ax_poincare = plt.subplot(gs[0:6, 0])
	ax_series = [plt.subplot(gs[(7+2*k):(9+2*k), 0]) for k in xrange(3)]
	
	# plot poincare map
	ax = ax_poincare
	data = scipy.io.loadmat(filename)

	for points in data['poincare_points'][0,:]:
		n_zs = points[:,0]
		psis = points[:,1]

		ax.scatter(n_zs, psis,s=.1, facecolor='#222222', lw = 0)

	ax.set_ylim([-1,1])		
	ax.set_xlim([-np.pi/2., np.pi/2.])

	ax.set_yticks([])
	ax.set_xticks([])
	#ax.set_title(r'$\kappa={:.2f}$'.format(kappa))

	ax.set_ylabel("$n_z$")
	ax.set_yticks([-1,0,1])
	ax.yaxis.set_label_coords(-.1, 0.5)

	ax.set_xticks([-np.pi/2.,0,np.pi/2.])
	ax.set_xticklabels(['$-\\displaystyle\\frac{\\pi}{2}$','$0$','$\\displaystyle\\frac{\\pi}{2}$'])
	ax.set_xlabel("$\\psi$")
	ax.xaxis.set_label_coords(.5, -.1)

	pos = ax.get_position().get_points()
	aspect_ratio = 2.1
	pointsize = .05
	
	colors=['#E41A1C', '#377EB8', '#4DAF4A', '#984EA3', '#FF7F00', '#FFFF33']
	for (series_k, filename) in enumerate(series_files):
		print filename
		datafile = h5py.File(filename, 'r')
		psis = datafile['/poincare_psi'][0,:]
		zs = datafile['/poincare_nz'][0,:]
		ts = datafile['/t'][:].transpose()
		nzs = datafile['/n_z'][:].transpose()
		for k in range(psis.shape[0]):
			x = psis[k];
			y = zs[k];
			ax.add_artist(Ellipse(xy=(x,y), width=pointsize, height=pointsize,facecolor=colors[series_k], linewidth=0.2))	


		#ax_series[series_k].plot(ts, nzs)
		ax_series[series_k].plot(ts, nzs, color=colors[series_k])
		ax_series[series_k].set_ylim(-1.1,1.1)
		ax_series[series_k].set_xlim(0,ts[-1])
		ax_series[series_k].set_ylabel('$n_z$',rotation=0)
		ax_series[series_k].set_xticks([])
		ax_series[series_k].set_yticks([-1,0,1])
		
	ax_series[2].set_xlabel('$t$')
	ax_series[2].set_xticks([0,ts[-1]])
		
	#ax.add_artist(Ellipse(xy=(0,.35), width=pointsize, height=pointsize*aspect_ratio,facecolor='#800000', linewidth=0.5))	
	#ax.text(.03, .22, r'(a)')


	print "Starting export..."
	if not exists("output/"):
		mkdir("output")
	#pp = matplotlib.backends.backend_pdf.PdfPages('output/poincare.pdf')
	#pp.savefig(fig1)
	#pp.close()
	#ax.set_frame_on(False)
	#plt.subplots_adjust(left=0.2, right=.96, top=.96, bottom=0.2)

	plt.savefig('output/poincare{}.png'.format(particle),dpi=300)


	#plt.show()
	print "Done!"



if __name__ == '__main__':
	main()