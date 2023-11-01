from astropy.io import fits
import matplotlib.pyplot as plt
data, header = fits.getdata('m51.fits', header=True)
hdu = fits.open('m51.fits')

size = data.shape
print('size = ', size)

# print(hdu[0].header)
print(header)


# plt.imshow(data);
# print(hdu[0].data[33])
