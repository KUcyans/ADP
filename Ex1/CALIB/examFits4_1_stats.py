import dfitspy
from astropy.io import fits
import numpy as np

extractedData = open('bias.list', 'r')
#-------- data struct for fits 2D data
imageData = []
fileNames = extractedData.read().splitlines()
for fileName in fileNames:
    hdu_list = fits.open(fileName)
    imageData.append(hdu_list[0].data)
extractedData.close()

#--------check the shape if it is 2D
# print('imageData[0].shape : ', imageData[0].shape)
# print('imageData[124].shape : ', imageData[124].shape)

"""
@function __cropStat__
@arg __lowerLim__ : the lower limit of the region
@arg __upperLim__ : the upper limit of the region
is a function that generate mean and stdev of cropped region
the cropped region is decided by two args:  lowerLim and upperLim
so the region is square
""" 
def cropStat(lowerLim, upperLim):
    #-------- data struct for data of cutout imageData
    cropImageData = []
    for i in range(len(imageData)):
        imageDataItem = imageData[i]
        cropImageData.append(imageDataItem[lowerLim:upperLim, lowerLim:upperLim])
    #--------check the shape if it is 2D
    # print('cropImageData[0].shape : ', cropImageData[0].shape)
    # print('cropImageData[124].shape : ', cropImageData[124].shape)

    #--------statistics output
    return cropImageData

"""
@function __diff__
@arg __first__
@arg __later__
calculates difference between two values
"""
def diff(first, later):
    return "{:.3%}".format((first-later)/first)

"""
@function __printStat__
@arg __lowerLim1__
@arg __upperLim1__
@arg __lowerLim2__
@arg __upperLim2__
"""
def printStat(lowerLim1, upperLim1, lowerLim2, upperLim2):
    region1 = cropStat(lowerLim1, upperLim1)
    region2 = cropStat(lowerLim2, upperLim2)
    print('lower limit1 : ', lowerLim1, 'upper limit1 : ', upperLim1, '\t', 'lower limit2 : ', lowerLim2, 'upper limit2 : ', upperLim2)
    print('mean1\t\t', 'stdev1\t\t\t','mean2\t\t', 'stdev2\t\t\t', 'diff mean\t\t', 'diff stdev')

    for i in range(len(region1)):
        print(np.mean(region1[i]),'\t', np.std(region1[i]), '\t', np.mean(region2[i]),'\t', np.std(region2[i]), '\t', diff(np.mean(region1[i]), np.mean(region2[i])), '\t', diff(np.std(region1[i]), np.std(region2[i])))
    print()


printStat(250,750,400,600)


