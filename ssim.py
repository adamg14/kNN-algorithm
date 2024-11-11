from PIL import Image
import numpy as np

# using the algorithm for SSIM in the documentation on mathsworks - https://www.mathworks.com/help/images/ref/ssim.html
image_one = Image.open("./Images/Student_Train/0.jpg")
image_two = Image.open("./Images/Student_Train/1.jpg")
image_one_pixels = list(image_one.getdata())
image_two_pixels = list(image_two.getdata())

# how do i get the average of the rgb tuples instead of flattening the array - maybe this affects the results
# need to make sure that they are the same size!!!
image_one_pixels_flat = np.array(image_one_pixels).flatten()
image_two_pixels_flat = np.array(image_two_pixels).flatten()

# work out the average of the two images
# if they were the same size - as they should - it could be in the same loop
sum_one = 0
for i in range(len(image_one_pixels_flat)):
    sum_one += int(image_one_pixels_flat[i])

sum_two = 0
for i in range(len(image_two_pixels_flat)):
    sum_two += int(image_two_pixels_flat[i])

local_average_x = sum_one / int(len(image_one_pixels_flat))
local_average_y = sum_two / int(len(image_two_pixels_flat))

# work out the standard deviation of two numpy
standard_deviation_x = np.std(image_one_pixels_flat)
standard_deviation_y = np.std(image_two_pixels_flat)

# working out the cross covariance of the two arrays - i think this is just working out the correlation between them
cross_covariance = np.correlate(image_one_pixels_flat, image_two_pixels_flat)

# need to fill these in with the formulas
# and need to multiply them together to work out the SSIM
# assume that alpha, beta and gamma are all one - this could cause errors
alpha = 1
beta = 1
gamma = 1
# the regulaisation constants needed for the formulae
# dynamic range of the images
dynamic_range = 255
C1 = (0.01*dynamic_range)**2
C2 = (0.03*dynamic_range)**2
C3 = C2/2

l_x_y = (2 * local_average_x * local_average_y + C1) /(standard_deviation_x**2 + standard_deviation_y**2 + C1)
c_x_y = (2 * local_average_x * local_average_y + C2) /(standard_deviation_x**2 + standard_deviation_y**2 + C2)
s_x_y = (2 * local_average_x * local_average_y + C3) /(standard_deviation_x**2 + standard_deviation_y**2 + C3)

SSIM_value = ((l_x_y)**alpha) * ((c_x_y)**beta) * ((s_x_y)**gamma)
print(SSIM_value)

import sewar
import matplotlib.image as im
import cv2
# this is the bigger image so i need to reshape it
# THIS SHOULD BE BETWEEN 0 AND 1 - I DONT KNOW WHY I GOT 19!!!
training_img = im.imread("./Images/Student_Train/0.jpg")
test_img = im.imread("./Images/Student_Train/1.jpg")
test_img1 = Image.open("./Images/Student_Train/1.jpg")
test_img_size = test_img1.size
resized_training_img = cv2.resize(training_img, test_img_size)
print("this is the sewar value for ssim ", sewar.msssim(test_img, resized_training_img))