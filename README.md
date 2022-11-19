# brovey-pan-sharpening

This program use brovey transform to pan-sharpening tif image.
Step to run:
- install python3 
- install numpy, rasterio, matplotlib, scikit-image package
- replace filename in line 15 at brovey.py with your low spatial resolution RGB tif image
- replace filename in line 23 at brovey.py with your high spatial resolution Pan tif image
- run python .\brovey.py

# Important Note: This code only work with 3 bands Red (band 1) Green (band 2) Blue (band 3) low spatial resolution RGB tif image. The Pan tif image and RGB tif image must be same size. Use Adobe Photoshop to resize tif image to same size, use ENVI 4.8 to make appropriate RGB and PAN tif image
