"""
Pulsar Image Stacking
---------------------
Author: Jansen Penido <jansen.penido@gmail.com>
"""

import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits


def median_fits(fitsArray):
    pixelsArray = []
   
    # Start the clock
    start = time.perf_counter()
  
    # Load FITS
    for fitsFile in fitsArray:
        hdulist = fits.open(fitsFile)
        pixelsArray.append(hdulist[0].data)
       
    # Calculate the median for each pixel
    pixelsNumpyArray = np.array(pixelsArray)
    medianMatrix = np.median(pixelsNumpyArray, axis=0)
  
    # Stop the clock
    seconds = time.perf_counter() - start

    # Get memory usage in kB
    memoryUsage = sys.getsizeof(pixelsNumpyArray) / 1024
  
    # Return the stacked image, the time spent on the stacking process (in seconds) 
    #  and memory usage
    return (medianMatrix, seconds, memoryUsage)


if __name__ == '__main__':
    # Stack image using the median of each pixel
    result = median_fits(['data/image{}.fits'.format(str(i)) for i in range(11)])
    print(result[0][100, 100], result[1], result[2])

    # Plot the pulsar image
    plt.imshow(result[0].T, cmap=plt.cm.viridis)
    plt.colorbar()
    plt.show()
