# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
# import astroalign as aa



# --------------------- #
# B I A S   F R A M E S #
# --------------------- #
'''
Open one of your bias frames (doesn't matter which; I chose the first one).
All of the biases, darks, flats, and science images exist in their own
folders in the same directory as my code. In order to access these files,
I have to add "<folder name>/" before the file name, so Python knows
where to look for them.
'''
bias1 = fits.open('bias/Autosave Image -0001Bias.fit')

# Get the array representing the bias image
image_bias1 = bias1[0].data

'''
Save the shape of the bias array in a variable (same for all biases).
The np.shape() function returns a list of two numbers, corresponding
to the dimensions of the array (N x M).
'''
bias_shape = np.shape(image_bias1)
N = bias_shape[0]
M = bias_shape[1]

'''
Create an array of empty arrays of zeros to hold all of your bias
frame arrays. Its length should be equal to the number of bias frames
(so it can hold them all). You also must set the shape of each of the
empty arrays with the syntax below, using the shape we saved above.
'''
image_biases = np.zeros((2, N, M))

'''
Open bias 1 (again; don't have to do it twice, but I
want to map out the steps for you)
'''
bias1 = fits.open('bias/Autosave Image -0001Bias.fit')

'''
Replace one of the empty arrays (index 0) in our image_biases array
with the data from bias 1. Don't be alarmed by the colons here,
they just indicate that you want to add elements that span the entire
shape of the array
'''
image_biases[0,:,:] = bias1[0].data

# Open bias 2
bias2 = fits.open('bias/Autosave Image -0002Bias.fit')

'''
Replace the other empty array (index 2) in image_biases with the
data from bias 2
'''
image_biases[1,:,:] = bias2[0].data

'''
Now that the image_biases array is filled with the data from all
two of our bias frames, we take the median (average) value of each
element in both arrays, leaving one averaged array representing the
fully processed bias frame.

Adding axis=0 to the median() function lets us average on a
pixel-by-pixel basis, rather than averaging every value in the
array(s) into one number.
'''
bias = np.median(image_biases, axis=0)

'''
Save your processed bias frame to a new fits file. I like to save all
my processed files to their own folder called "processed", so I've
created one in the same directory as my code and added it to the save
address in the writeto() function below. I'll be doing this for all
our processed files for each step.
'''
hdu = fits.PrimaryHDU(bias)
hdul = fits.HDUList([hdu])
hdul.writeto('processed/bias_processed.fits')

'''
From here, many of the same steps are repeated, so the
descriptions will get less detailed for the most part.
If you get confused, refer to this section again.
'''



# --------------------- #
# D A R K   F R A M E S #
# --------------------- #

# Open one of your dark frames (again, doesn't matter which)
dark1 = fits.open('dark/Autosave Image -0001Dark_120s.fit')

# Get the array representing the bias image
image_dark1 = dark1[0].data

# Save shape of image array to variable(s)
dark_shape = np.shape(image_dark1)
N = dark_shape[0]
M = dark_shape[1]

'''
Pull the exposure time for the dark frames from the header
(even though its in the file name, it might not always be)
'''
head = dark1[0].header
t_dark = head['EXPOSURE']

# Make an array of zero-arrays to fill with data arrays
image_darks = np.zeros((2, N, M))

# Open dark 1 (again)
dark1 = fits.open('dark/Autosave Image -0001Dark_120s.fit')

# Replace first empty array in image_darks with data from dark 1
image_darks[0,:,:] = dark1[0].data

# Open dark 2
dark2 = fits.open('dark/Autosave Image -0002Dark_120s.fit')

# Replace second empty array in image_darks with data from dark 2
image_darks[1,:,:] = dark2[0].data

'''
Now that the image_darks array is filled with our data, we can
process our darks. I'll do this step by step here, but you can
do it all in one line if you want to.

First, we'll get the median dark array, same way we did with
the biases.
'''
dark_avg = np.median(image_darks, axis=0)

# Next, we subtract the processed bias from the dark average
dark_sub = dark_avg - bias

# Finally, we divide this difference by the dark exposure time
dark = dark_sub / t_dark

# Save your processed dark frame to a new fits file
hdu = fits.PrimaryHDU(dark)
hdul = fits.HDUList([hdu])
hdul.writeto('processed/dark_processed.fits')




# --------------------- #
# F L A T   F R A M E S #
# --------------------- #

# Open one of your flat frames for each filter
flat1_B = fits.open('flat/Autosave Image -0001Flat_B_1s.fit')
flat1_V = fits.open('flat/Autosave Image -0001Flat_V_1s.fit')
flat1_R = fits.open('flat/Autosave Image -0001Flat_R_1s.fit')
flat1_Ha = fits.open('flat/Autosave Image -0001Flat_Ha_1s.fit')

# Get the array representing the flat image for each filter
image_flat1_B = flat1_B[0].data
image_flat1_V = flat1_V[0].data
image_flat1_R = flat1_R[0].data
image_flat1_Ha = flat1_Ha[0].data

#Save shape of image arrays to variable(s)
flat_shape_B = np.shape(image_flat1_B)
flat_shape_V = np.shape(image_flat1_V)
flat_shape_R = np.shape(image_flat1_R)
flat_shape_Ha = np.shape(image_flat1_Ha)

N_B, M_B = flat_shape_B[0], flat_shape_B[1]
N_V, M_V = flat_shape_V[0], flat_shape_V[1]
N_R, M_R = flat_shape_R[0], flat_shape_R[1]
N_Ha, M_Ha = flat_shape_Ha[0], flat_shape_Ha[1]

'''
Pull the exposure time for the flat frames from the header
(even though its in the file name, it might not always be)
'''
head = flat1_B[0].header
t_flat_B = head['EXPOSURE']

head = flat1_V[0].header
t_flat_V = head['EXPOSURE']

head = flat1_R[0].header
t_flat_R = head['EXPOSURE']

head = flat1_Ha[0].header
t_flat_Ha = head['EXPOSURE']

# Make arrays of zero-arrays to fill with data arrays for each filter
image_flats_B = np.zeros((2, N_B, M_B))
image_flats_V = np.zeros((2, N_V, M_V))
image_flats_R = np.zeros((2, N_R, M_R))
image_flats_Ha = np.zeros((2, N_Ha, M_Ha))

# Open flat 1 for each filter (again)
flat1_B = fits.open('flat/Autosave Image -0001Flat_B_1s.fit')
flat1_V = fits.open('flat/Autosave Image -0001Flat_V_1s.fit')
flat1_R = fits.open('flat/Autosave Image -0001Flat_R_1s.fit')
flat1_Ha = fits.open('flat/Autosave Image -0001Flat_Ha_1s.fit')

'''
Replace first empty array in image_flats_<filter> with data from
flat 1 for each filter
'''
image_flats_B[0,:,:] = flat1_B[0].data
image_flats_V[0,:,:] = flat1_V[0].data
image_flats_R[0,:,:] = flat1_R[0].data
image_flats_Ha[0,:,:] = flat1_Ha[0].data

# Open flat 2 for each filter
flat2_B = fits.open('flat/Autosave Image -0002Flat_B_1s.fit')
flat2_V = fits.open('flat/Autosave Image -0002Flat_V_1s.fit')
flat2_R = fits.open('flat/Autosave Image -0002Flat_R_1s.fit')
flat2_Ha = fits.open('flat/Autosave Image -0002Flat_Ha_1s.fit')

'''
Replace second empty array in image_flats_<filter> with data from
flat 2 for each filter
'''
image_flats_B[1,:,:] = flat2_B[0].data
image_flats_V[1,:,:] = flat2_V[0].data
image_flats_R[1,:,:] = flat2_R[0].data
image_flats_Ha[1,:,:] = flat2_Ha[0].data

'''
Now that the image_flats_<filter> arrays are filled with our data,
we can process our flats. I'll do this step by step here, but you can
do it all in one line if you want to.

We'll continue editing the values in image_flats_<filter>, as we won't
take the average until after we've done some calculations. First, we'll
subtract off the processed bias, as well as the product of the
processed dark and the flat exposure time.
'''

image_flats_B[0] = image_flats_B[0] - bias - dark*t_flat_B
image_flats_B[1] = image_flats_B[1] - bias - dark*t_flat_B

image_flats_V[0] = image_flats_V[0] - bias - dark*t_flat_V
image_flats_V[1] = image_flats_V[1] - bias - dark*t_flat_V

image_flats_R[0] = image_flats_R[0] - bias - dark*t_flat_R
image_flats_R[1] = image_flats_R[1] - bias - dark*t_flat_R

image_flats_Ha[0] = image_flats_Ha[0] - bias - dark*t_flat_Ha
image_flats_Ha[1] = image_flats_Ha[1] - bias - dark*t_flat_Ha

'''
Next, we'll divide each array by its median array to normalize
each pixel (notice that the median function here is now taking
the average of a single array, not averaging the pixels of many.)
'''
image_flats_B[0] = image_flats_B[0] / np.median(image_flats_B[0], axis=0)
image_flats_B[1] = image_flats_B[1] / np.median(image_flats_B[1], axis=0)

image_flats_V[0] = image_flats_V[0] / np.median(image_flats_V[0], axis=0)
image_flats_V[1] = image_flats_V[1] / np.median(image_flats_V[1], axis=0)

image_flats_R[0] = image_flats_R[0] / np.median(image_flats_R[0], axis=0)
image_flats_R[1] = image_flats_R[1] / np.median(image_flats_R[1], axis=0)

image_flats_Ha[0] = image_flats_Ha[0] / np.median(image_flats_Ha[0], axis=0)
image_flats_Ha[1] = image_flats_Ha[1] / np.median(image_flats_Ha[1], axis=0)

'''
Finally, we take the median of the arrays we calculated above
for each filter.
'''
flat_B = np.median(image_flats_B, axis=0)
flat_V = np.median(image_flats_V, axis=0)
flat_R = np.median(image_flats_R, axis=0)
flat_Ha = np.median(image_flats_Ha, axis=0)

# Save your processed flat frames to new fits files
hdu = fits.PrimaryHDU(flat_B)
hdul = fits.HDUList([hdu])
hdul.writeto('processed/flatB_processed.fits')

hdu = fits.PrimaryHDU(flat_V)
hdul = fits.HDUList([hdu])
hdul.writeto('processed/flatV_processed.fits')

hdu = fits.PrimaryHDU(flat_R)
hdul = fits.HDUList([hdu])
hdul.writeto('processed/flatR_processed.fits')

hdu = fits.PrimaryHDU(flat_Ha)
hdul = fits.HDUList([hdu])
hdul.writeto('processed/flatHa_processed.fits')



# --------------------------- #
# S C I E N C E   F R A M E S #
# --------------------------- #

# Open one of your science frames for each filter
science1_B = fits.open('science/Autosave Image -0001WPG_B_300s.fit')
science1_V = fits.open('science/Autosave Image -0001WPG_V_300s.fit')
science1_R = fits.open('science/Autosave Image -0001WPG_R_300s.fit')
science1_Ha = fits.open('science/Autosave Image -0001WPG_Ha_300s.fit')

# Get the array representing the flat image for each filter
image_science1_B = science1_B[0].data
image_science1_V = science1_V[0].data
image_science1_R = science1_R[0].data
image_science1_Ha = science1_Ha[0].data

#Save shape of image arrays to variable(s)
science_shape_B = np.shape(image_science1_B)
science_shape_V = np.shape(image_science1_V)
science_shape_R = np.shape(image_science1_R)
science_shape_Ha = np.shape(image_science1_Ha)

N_B, M_B = science_shape_B[0], science_shape_B[1]
N_V, M_V = science_shape_V[0], science_shape_V[1]
N_R, M_R = science_shape_R[0], science_shape_R[1]
N_Ha, M_Ha = science_shape_Ha[0], science_shape_Ha[1]

'''
Pull the exposure time for the flat frames from the header
(even though its in the file name, it might not always be)
'''
head = science1_B[0].header
t_science_B = head['EXPOSURE']

head = science1_V[0].header
t_science_V = head['EXPOSURE']

head = science1_R[0].header
t_science_R = head['EXPOSURE']

head = science1_Ha[0].header
t_science_Ha = head['EXPOSURE']

'''
Unlike the biases, darks, and flats, we only have one observation in each
filter for science images. This means that (1) our zero-arrays will only
have one entry, (2) we'll only "open & replace" once, and (3) when we take
the median of our final array, we'll be taking the median of just one
array, so nothing will change.

To account for this, I've changed the zero-array's size, added and
commented out the extra steps for point (2), and still went ahead and
took the final median for consistency's sake. If we had more than one
science image, you could follow the same logic (other than the final
calculations) from the previous steps pretty closely, or fill in the
gaps yourself.
'''

# Make arrays of zero-arrays to fill with data arrays for each filter
image_sciences_B = np.zeros((1, N_B, M_B))
image_sciences_V = np.zeros((1, N_V, M_V))
image_sciences_R = np.zeros((1, N_R, M_R))
image_sciences_Ha = np.zeros((1, N_Ha, M_Ha))

# Open flat 1 for each filter (again)
science1_B = fits.open('science/Autosave Image -0001WPG_B_300s.fit')
science1_V = fits.open('science/Autosave Image -0001WPG_V_300s.fit')
science1_R = fits.open('science/Autosave Image -0001WPG_R_300s.fit')
science1_Ha = fits.open('science/Autosave Image -0001WPG_Ha_300s.fit')

'''
Replace first empty array in image_flats_<filter> with data from
flat 1 for each filter
'''
image_sciences_B[0,:,:] = science1_B[0].data
image_sciences_V[0,:,:] = science1_V[0].data
image_sciences_R[0,:,:] = science1_R[0].data
image_sciences_Ha[0,:,:] = science1_Ha[0].data

# # Open flat 2 for each filter
# science2_B = fits.open('science/Autosave Image -0002WPG_B_300s.fit')
# science2_V = fits.open('science/Autosave Image -0002WPG_V_300s.fit')
# science2_R = fits.open('science/Autosave Image -0002WPG_R_300s.fit')
# science2_Ha = fits.open('science/Autosave Image -0002WPG_Ha_300s.fit')
#
# '''
# Replace second empty array in image_flats_<filter> with data from
# flat 2 for each filter
# '''
# image_sciences_B[1,:,:] = science2_B[0].data
# image_sciences_V[1,:,:] = science2_V[0].data
# image_sciences_R[1,:,:] = science2_R[0].data
# image_sciences_Ha[1,:,:] = science2_Ha[0].data

'''
Now that the image_sciences_<filter> arrays are filled with our data,
we can process our flats. Again, I'll do this step by step here, but you can
do it all in one line if you want to.

We'll continue editing the values in image_sciences_<filter>, as we won't
take the average until after we've done some calculations. First, we'll
subtract the processed bias and the product of the processed dark and the
science exposure time for the filter.
'''
image_sciences_B[0] = image_sciences_B[0] - bias - dark*t_science_B
#image_sciences_B[1] = image_sciences_B[1] - bias - dark*t_science_B

image_sciences_V[0] = image_sciences_V[0] - bias - dark*t_science_V
#image_sciences_V[1] = image_sciences_V[1] - bias - dark*t_science_V

image_sciences_R[0] = image_sciences_R[0] - bias - dark*t_science_R
#image_sciences_R[1] = image_sciences_R[1] - bias - dark*t_science_R

image_sciences_Ha[0] = image_sciences_Ha[0] - bias - dark*t_science_Ha
#image_sciences_Ha[1] = image_sciences_Ha[1] - bias - dark*t_science_Ha


# Next, we'll divide them by the processed flat frame for each filter.
image_sciences_B[0] = image_sciences_B[0] / flat_B
#image_sciences_B[1] = image_sciences_B[1] / flat_B

image_sciences_V[0] = image_sciences_V[0]  / flat_V
#image_sciences_V[1] = image_sciences_V[1]  / flat_V

image_sciences_R[0] = image_sciences_R[0]  / flat_R
#image_sciences_R[1] = image_sciences_R[1]  / flat_R

image_sciences_Ha[0] = image_sciences_Ha[0]  / flat_Ha
#image_sciences_Ha[1] = image_sciences_Ha[1]  / flat_Ha

'''
Finally, we'll take the median of the arrays we calculated
above for each filter. This step is a good one to specifically
title your files with the name of the object you're imaging;
calibration images can usually be used for any of the targets
you take in a single night, but these final science images are
just for a single target. Since we're imaging the Whirlpool galaxy
here, I'll add the prefix "WPG".
'''
science_B = np.median(image_sciences_B, axis=0)
science_V = np.median(image_sciences_V, axis=0)
science_R = np.median(image_sciences_R, axis=0)
science_Ha = np.median(image_sciences_Ha, axis=0)

# Save your processed science frames to new fits files
hdu = fits.PrimaryHDU(science_B)
hdul = fits.HDUList([hdu])
hdul.writeto('processed/WPG_scienceB_processed.fits')

hdu = fits.PrimaryHDU(science_V)
hdul = fits.HDUList([hdu])
hdul.writeto('processed/WPG_scienceV_processed.fits')

hdu = fits.PrimaryHDU(science_R)
hdul = fits.HDUList([hdu])
hdul.writeto('processed/WPG_scienceR_processed.fits')

hdu = fits.PrimaryHDU(science_Ha)
hdul = fits.HDUList([hdu])
hdul.writeto('processed/WPG_scienceHa_processed.fits')

'''
There you have it! Those images are now ready for science with
tools like AstroImageJ or prettification with editing software
like GIMP.
'''
