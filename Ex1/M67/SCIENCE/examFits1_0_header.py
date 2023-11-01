from astropy.io import fits

header = fits.getheader(
    'EFOSC.2001-01-02T05:01:30.597.fits')

print(header[0])
