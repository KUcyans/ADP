import os
import astropy.io.fits as fits
import dfitspy
##========================================= dirs
dirEx3 = '/Users/yhjo/Desktop/AstronomicalDataProcessing/Exercise/Ex3/'
dirSTD = '/Users/yhjo/Desktop/AstronomicalDataProcessing/Exercise/Ex3/STANDARD'
dirErr = '/Users/yhjo/Desktop/AstronomicalDataProcessing/Exercise/Ex3/PSError'
dirPC = '/Users/yhjo/Desktop/AstronomicalDataProcessing/Exercise/Ex3/PhotoCalibration'
filters =['V#641','R#642','B#639']
fileNames = {'V#641':'EFOSC.2001-01-03T08:55:18.187.fits',
             'R#642':'EFOSC.2001-01-03T08:56:03.899.fits',
             'B#639':'EFOSC.2001-01-03T08:54:27.270.fits'}
stdName = ['PG-1323-086', 'PG-1323-086 B', 'PG-1323-086 C']
extCoeff = [0.13, 0.09, 0.25]
##========================================= 
'''
@getAirmass()
get airmass values from header of the .fits file of the standard stars in V, R, B filters
'''
def seeFits():
    prevDir = os.getcwd()
    os.chdir(dirSTD)
    fitsFiles = [m for m in os.listdir() if m.endswith('.fits')]
    for f in fitsFiles:
        header = fits.getheader(f)
        print(header)
    # stdFiles = dfitspy.dfitsort(fitsFiles)
    # dfitspy.dfitsort_view(stdFiles)
    os.chdir(prevDir)
    
def getAirmass(filter):
    prevDir = os.getcwd()
    os.chdir(dirSTD)
    fileName = fileNames[filter]
    am = fits.getheader(fileName)['HIERARCH ESO TEL AIRM START']
    os.chdir(prevDir)
    return am
#==================================================================
'''
@getCcdMagErr()
@returns the pair (magnitude, error)
'''
def getCcdMagErr(filter,stdStar):
    prevDir = os.getcwd()
    os.chdir(dirPC)
    iStd = stdName.index(stdStar)
    magFile = filter+'.magnitudes'
    if os.path.exists(magFile):
        with open(magFile, 'r') as file:
            lines = file.read().splitlines() # each line is from each stdstar
            values = lines[iStd].split(',')
            mag = float(values[0])
            err = float(values[1])
    os.chdir(prevDir)
    # print('magerr : ', mag)
    return [mag,err]
#==================================================================
'''
@getInstMagnitudes()
@returns the instrumental magnitude
'''
def getInstMagnitudes(filter,stdStar):
    prevDir = os.getcwd()
    os.chdir(dirPC)
    i = filters.index(filter)
    magInst = getCcdMagErr(filter,stdStar)[0] - extCoeff[i]*getAirmass(filter)
    os.chdir(prevDir)
    return magInst

#==================================================================     main
for i in range(len(filters)):
    print('=========================',filters[i],'=========================')
    print('airmass : ', getAirmass(filters[i]))
    for j in range(len(stdName)):
        print('-----------------',stdName[j],'-----------------')
        ccdMag = getCcdMagErr(filters[i],stdName[j])[0]
        instMag = getInstMagnitudes(filters[i],stdName[j])
        print('ccdMag : ', ccdMag) 
        print('instMag : ', instMag)
    print()
    seeFits()