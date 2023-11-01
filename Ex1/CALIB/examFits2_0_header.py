from astropy.io import fits

header = fits.getheader(
    'EFOSC.2000-10-27T09:32:22.516.fits')

print(header)
