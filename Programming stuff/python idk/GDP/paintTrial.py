import numpy as np

import matplotlib.pyplot as plt

from PIL import Image

import scipy.ndimage

# Function to downsample an image by a scale factor
def downsample_image(image_np, scale_factor):
    # Apply scipy's zoom function to resize the image
    downsampled_image = scipy.ndimage.zoom(image_np, (scale_factor, scale_factor, 1), order=1)
    return downsampled_image

image_path = "GDP/ripCube.jpg"  # Replace with your image path
image = Image.open(image_path)

# Convert image to NumPy array
image_np = downsample_image( np.array(image), 0.5 )

plt.figure(1)
plt.imshow( image_np )
plt.show(block=False)

pallet = np.array([ [ 255, 200, 0 ],[ 255, 200, 100 ], [ 150, 200, 210 ], [ 0, 0, 0 ], [255,255,255], [90,90,90], [200,200,200], [200,100,50] ])

outputImageIndxs = []

flatImage = np.transpose(np.array([image_np[:,:,0].flatten(), image_np[:,:,1].flatten(), image_np[:,:,2].flatten()]))

for pixel in flatImage:
    shortestDist = 10000
    shortestCol  = 0
    for colourIndx in range(0, pallet.shape[0]):
        newDist = np.sqrt(np.sum((pallet[colourIndx]-pixel)**2))

        if ( newDist < shortestDist ):
            shortestDist = newDist
            shortestCol = colourIndx


    outputImageIndxs.append( shortestCol )

outputImageIndout = np.reshape( pallet[outputImageIndxs], image_np.shape)

plt.figure(2)
plt.imshow( outputImageIndout )
plt.show(block=False)


""