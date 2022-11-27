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
    img_rescale = exposure.rescale_intensity(img, in_range=(np.nanmin(img), np.nanmax(img)))
    return img_rescale

filename = 'wv2_RGB_clip_contrast_low_spatial_resolution.tif'  #RGB low spatial resolution tif image
with rasterio.open(filename) as src: #reads 1rd dimension
    band_red = src.read(1)
with rasterio.open(filename) as src: #reads 2rd dimension
    band_green = src.read(2)
with rasterio.open(filename) as src: #reads 3th dimesion
    band_blue = src.read(3)

filename = 'wv2_pan_clip_contrast_high_spatial_resolution.tif' #PAN high spatial resolution tif image
with rasterio.open(filename) as src: #reads 1rd dimension
    band_pan = src.read(1)

# filename = 'nan_anh_spot.tif'  #RGB low spatial resolution tif image
# with rasterio.open(filename) as src: #reads 1rd dimension
#     band_red = src.read(2)
# with rasterio.open(filename) as src: #reads 2rd dimension
#     band_green = src.read(1)
# with rasterio.open(filename) as src: #reads 3th dimesion
#     band_blue = src.read(3)

# filename = 'nan_anh_pan_resized.tif' #PAN high spatial resolution tif image
# with rasterio.open(filename) as src: #reads 1rd dimension
#     band_pan = src.read(1)



red_sharp = np.multiply( np.true_divide(band_red.astype(float), band_red.astype(float) + band_green.astype(float) + band_blue.astype(float))   , band_pan.astype(float) )
green_sharp = np.multiply( np.true_divide(band_green.astype(float), band_red.astype(float) + band_green.astype(float) + band_blue.astype(float))   , band_pan.astype(float) )
blue_sharp = np.multiply( np.true_divide(band_blue.astype(float), band_red.astype(float) + band_green.astype(float) + band_blue.astype(float))   , band_pan.astype(float) )

sharpenedBrovey = create_composite(red_sharp,green_sharp,blue_sharp)
unSharpenedBrovey = create_composite(band_red,band_green,band_blue)

# fig = plt.imshow(red_sharp)
# plt.show()
# fig1 = plt.imshow(band_red)
# plt.show()

# fig = plt.imshow(green_sharp)
# plt.show()
# fig1 = plt.imshow(band_green)
# plt.show()

# fig = plt.imshow(blue_sharp)
# plt.show()
# fig1 = plt.imshow(band_blue)
# plt.show()

fig = plt.imshow(sharpenedBrovey)
plt.show()
fig1 = plt.imshow(unSharpenedBrovey)
plt.show()











