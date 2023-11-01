from astropy.table import Table
from scipy import stats
import numpy as np
from imexam.imexamine import Imexamine

def full_width_star(coo, image, form='Moffat1D'):
    '''
    This function permits to estimate the FWHM of the one-dim gaussian/Moffat psf of a star in an image
    given the pixel coordinate of the star
    
    For each detected sources, this function returns the FWHM according to the desired functional form
    
    Parameters:
        coo : (Array) (X,Y) coordinates in pixels of the star for which the FWHM is going to be computed    
        image : (2D array) Data array of the image
        form = 'Moffat1D' : (String) The functional form used for the estimate of the FWHM
        Possible choices 1) 'Moffat1D' 2) ' Gaussian'
        
    '''
    #
    plots=Imexamine()
    plots.set_data(image.data)
    #
    if form == 'Moffat1D':
        try:
            m1 = plots.line_fit(coo[0], coo[1], form='Moffat1D', genplot=False).alpha_0.value
            m2 = plots.line_fit(coo[0], coo[1], form='Moffat1D', genplot=False).gamma_0.value
            g = lambda x, y : y * 2 * np.sqrt(2**(1/x) - 1)#in case of Moffat1D form
            return g(m1, m2)
        except:
            pass
    elif form == 'Gaussian1D':
        try:
            m1 = plots.line_fit(coo[0], coo[1], form='Gaussian1D', genplot=False).stddev_0.value
            g = lambda x : x * np.sqrt(8.0 * np.log(2.))# - in case of Gaussian1D form 
            return g(m1)
        except:
            pass
    else:
        print('Wrong selection of the functional form')
        
def full_width_table(table, image, form='Moffat1D'):
    '''
    This function permits to estimate the FWHM of the one-dim gaussian psf of the sources in a catalogue
    given a file and a table of sources (obtained from a source detection algorithm - in this case DAOStarFinder)
    
    For each detected sources, this function returns the FWHM according to the desired functional form
    
    Parameters:
        table : (Astropy Table) coordinates in pixels of the stars for which the FWHM is going to be computed    
        image : (2D array) Data array of the image
        form = 'Moffat1D' : (String) The functional form used for the estimate of the FWHM
        Possible choices 1) 'Moffat1D' 2) ' Gaussian'
    '''
    a=table['xcentroid']
    b=table['ycentroid']
    c=[i for i in range(0, len(b))]
    t=Table([c, a, b])
    t=t[np.where((t['xcentroid']>0) & (t['ycentroid']>0))]
    #
    if len(t)>1000:
        step = int(len(t)/1000)
    else:
        step=int(1)
    t=t[0:-1:step]
    #
    plots=Imexamine()
    plots.set_data(image.data)
    #
    result1=[]
    result2=[]
    for item in t:
        if form == 'Moffat1D':
            try:
                result1.append(plots.line_fit(item[1], item[2], form='Moffat1D', genplot=False).alpha_0.value)
                result2.append(plots.line_fit(item[1], item[2], form='Moffat1D', genplot=False).gamma_0.value)
            except:
                pass
        elif form == 'Gaussian1D':
            try:
                result1.append(plots.line_fit(item[1], item[2], form='Gaussian1D', genplot=False).stddev_0.value)
            except:
                pass
    #
    m1, s1 = stats.norm.fit(result1)
    try:
        m2, s2 = stats.norm.fit(result2)
    except:
        pass
    #
    if form == 'Moffat1D':
        g = lambda x, y : y * 2 * np.sqrt(2**(1/x) - 1)#in case of Moffat1D form
        return g(m1, m2)
    elif form == 'Gaussian1D':
        g = lambda x : x * np.sqrt(8.0 * np.log(2.))# - in case of Gaussian1D form 
        return g(m1)
    else:
        print('Wrong selection of the functional form')

def vfit(params, mv, data, mverr, airmass):
    '''
    This function allows to estimate the coefficients of the V-band zero-point equation through a linear model fit
    It gives in output an objective function that will be then minimized by the "minimize" function later on
    
    Parameters:
        params: the paramaters of the model.
        mv: (array) instrumental magnitudes
        data: (2D array) magnitudes and their errors of the standard stars
        mverr: (array) uncertainties on the isntrumental magnitudes
  '''
    V = data[0]
    VR = data[1]
    cv1 = 0.13
    cv2 = params['cb2']
    cv3 = params['cb3']
    model =  (V  +  cv1 * airmass - cv2 * VR - cv3 )
    return (mv - model )/ mverr

def bfit(params, mb, data, mberr, airmass):
    '''
    This function allows to estimate the coefficients of the B-band zero-point equation through a linear model fit
    It gives in output an objective function that will be then minimized by the "minimize" function later on
    
    Parameters:
        params: the paramaters of the model. 
        mb: (array) instrumental magnitudes
        data: (2D array) magnitudes and their errors of the standard stars
        mberr: (array) uncertainties on the isntrumental magnitudes
    
    '''
    V = data[0]
    BV = data[1]
    B = BV + V
    cb1 = 0.25
    cb2 = params['cb2']
    cb3 = params['cb3']
    model =  (B  +  cb1 * airmass - cb2 * BV - cb3 )
    return (mb - model )/ mberr

def rfit(params, mr, data, mrerr, airmass):
    '''
    This function allows to estimate the coefficients of the R-band zero-point equation through a linear model fit
    It gives in output an objective function that will be then minimized by the "minimize" function later on

    Parameters:
        params: the paramaters of the model.
        mr: (array) instrumental magnitudes
        data: (2D array) magnitudes and their errors of the standard stars
        mrerr: (array) uncertainties on the isntrumental magnitudes
    
    '''
    V = data[0]
    VR = data[1]
    R = V - VR
    cr1 = 0.09
    cr2 = params['cb2']
    cr3 = params['cb3']
    model =  (R  +  cr1 * airmass - cr2 * VR - cr3 )
    return (mr - model )/ mrerr