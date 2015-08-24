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
	#make("1o00")

	# poincare B
	#make("1o10")
	
	# poincare C
	make("1o30")
	
	# poincare D
	#make("2o00")
	
	

def make(particle):

	print "making {}".format(particle)

	filename = "poincaredata/{}.mat".format(particle)

	matplotlib.rc('text', usetex=True)
	matplotlib.rc('ps', usedistiller='xpdf')
	matplotlib.rcParams["text.latex.preamble"].append(r'\mathchardef\mhyphen="2D')

	fig1 = plt.figure(figsize=(10./2.5,8./2.5))
	
	gs = gridspec.GridSpec(1,1, hspace=.5,bottom=0.15,left=0.18,right=0.94,top=0.96)

	ax_poincare = plt.subplot(gs[0])
	
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

	print "Starting export..."
	if not exists("output/"):
		mkdir("output")
	#pp = matplotlib.backends.backend_pdf.PdfPages('output/poincare.pdf')
	#pp.savefig(fig1)
	#pp.close()
	#ax.set_frame_on(False)
	#plt.subplots_adjust(left=0.2, right=.96, top=.96, bottom=0.2)

	plt.savefig('output/only_poincare{}.png'.format(particle),dpi=600)


	#plt.show()
	print "Done!"



if __name__ == '__main__':
	main()