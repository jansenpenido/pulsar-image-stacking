"""
Pulsar Image Stacking
---------------------
Author: Jansen Penido <jansen.penido@gmail.com>
"""

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt


# Stack the images using 'mean'
def mean_fits(fitsArray):
    datasetsArray = []

    # Load FITS files
    for fitsFile in fitsArray:
        hdulist = fits.open(fitsFile)
        datasetsArray.append(hdulist[0].data)

    # Calculate the mean for each pixel
    datasets = np.array(datasetsArray)
    meanMatrix = datasets.mean(axis = 0)

    # Return the stacked image
    return meanMatrix


if __name__ == '__main__':
    # Stack image
    data  = mean_fits(['data/image0.fits', 'data/image1.fits', 'data/image2.fits', 'data/image3.fits'])

    # Plot the pulsar image
    plt.imshow(data.T, cmap=plt.cm.viridis)
    plt.colorbar()
    plt.show()
