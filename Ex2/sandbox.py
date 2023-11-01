import os
import dfitspy
from astropy.io import fits 
import numpy as np

dirCALIB = 'M67/CALIB/'
biasFileList = open('bias.list', 'r')
biasData = []
fileNames = biasFileList.read().splitlines()
for fileName in fileNames:
    ##method : getdata()
#    biasFits = fits.getdata(dirCALIB + fileName, dtype = 'f')
#    biasData.append(biasFits[0].data)
    ##method : open()
    biasFits = fits.open(dirCALIB + fileName)
    biasData.append(biasFits[0].data.astype(float))
    '''
    biasFits : a HDU
    biasFits[0] : the primary HDU
    biasFits[0].data : (only) data from the PHDU, it is a 2D data
    '''
biasFileList.close()

print(biasData)