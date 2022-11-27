import numpy as np
import rasterio
import matplotlib.pyplot as plt
from skimage import exposure

def create_composite(red_band, green_band, blue_band):
    img_dim = red_band.shape
    img = np.zeros((img_dim[0], img_dim[1], 3), dtype=np.float64)
    img[:,:,0] = red_band
    img[:,:,1] = green_band
    img[:,:,2] = blue_band
    img_rescale = exposure.rescale_intensity(img, in_range=(0, 255))
    
    return img_rescale

filename = 'nan_anh_spot.tif'
with rasterio.open(filename) as src: #reads 1rd dimension
    band_green = src.read(1)
with rasterio.open(filename) as src: #reads 2rd dimension
    band_red = src.read(2)
with rasterio.open(filename) as src: #reads 3th dimesion123
    band_nir = src.read(3)

red = band_red.astype(float)
green = (3*band_green.astype(float) + band_nir.astype(float))/4
blue = (3*band_green.astype(float) - band_nir.astype(float))/4

xs_mtn = create_composite(red,green,blue)

fig1 = plt.imshow(xs_mtn)
plt.show()


