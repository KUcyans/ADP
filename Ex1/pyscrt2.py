import numpy as np
import astropy.io.fits as fits

rawData, header = fits.getdata('m51.fits', header=True)

with fits.open('m51.fits') as pHDU:
    data = pHDU[0].data
