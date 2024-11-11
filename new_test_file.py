# i could do this with the pixels of the image to work out the jacard similarity
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list1 =  [9, 1, 2, 3, 5, 6]
print(my_list[:2])

intersection = 0
union = len(my_list) + len(my_list1)
for i in range(len(my_list)):
    if my_list[i] in my_list1:
        intersection += 1

print(intersection)
print(union)
print(intersection/union)

# try out methods for the cosine similarity
import math

list_of_pixels_1 = [(255, 255, 255), (255, 255, 255)]
list_of_pixels_2 = [(255, 255, 255), (255, 255, 255)]
# work out the average of the pixels on the screen
count_r1 = 0
count_g1 = 0
count_b1 = 0
count_r2 = 0
count_g2 = 0
count_b2 = 0
# calculate the average of all the pixels in the image
for pixel in list_of_pixels_1:
    count_r1 += pixel[0]
    count_g1 += pixel[1]
    count_b1 += pixel[2]

avg_r1 = count_r1 / len(list_of_pixels_1)
avg_g1 = count_g1 / len(list_of_pixels_1)
avg_b1 = count_b1 / len(list_of_pixels_1)

for pixel in list_of_pixels_2:
    count_r2 += pixel[0]
    count_g2 += pixel[1]
    count_b2 += pixel[2]

avg_r2 = count_r2 / len(list_of_pixels_1)
avg_g2 = count_g2 / len(list_of_pixels_1)
avg_b2 = count_b2 / len(list_of_pixels_1)

# the above works out the average of the pixels of the image
import math
# theta should be the angle between the two images
dot_product = (avg_r1 * avg_r2) + (avg_b1 * avg_b2) + (avg_g1 * avg_g2)
denominator = math.sqrt((avg_r1 * avg_g1 * avg_b1) ** 2) * math.sqrt((avg_r2 * avg_g2 * avg_b2) ** 2)
theta = math.acos(dot_product/denominator)
# i think that i might have done the formula wrong - this should be zero or one i think
print("THIS SHOULD BE THE VALUE OF THETA" + str(theta))

# second try of cosine similarity
# assume that we have a flattened array of pixels - this is going to be very large an inefficient - images should be of the same length
image_1 = [255, 255, 255]
image_2 = [255, 255, 255]
numerator = 0
denominator_1 = 0
denominator_2 = 0
for i in range(len(image_1)):
    numerator += (image_1[i] * image_2[i])
    denominator_1 += image_1[i] ** 2
    denominator_2 += image_2[i] ** 2

# something really wrong with this - maybe i need to map 0 - 255 to 0 - 1
# THERE IS SOMETHING VERY WRONG HERE - I AM GETTING THE SAME VALUE FOR EVERYTHING HERE
print(numerator)
denominator1 = math.sqrt(denominator_1)
denominator2 = math.sqrt(denominator_2)
denominator = denominator_1 * denominator_2
print(math.cos(numerator/denominator))

two_d_array = [(255, 255, 255), (255, 255, 255)]
# need to get it into a one d array

import numpy

# this works - this will be quite useful for cosine similarity - remember that jaccard doesn matter about placement
# i think it is better if we do not flatten the array for jaccard and just do it for cosine
one_d_array = numpy.array(two_d_array).flatten()
print(one_d_array[0])

# normal array
empty_array = numpy.empty(4)
print(empty_array)

# YES GREAT, IT LOOKS LIKE THE NONE KEY WORD WORKS!
row = [1, 2, None, 3, 4, None]
# none keyword in python used to
import csv

f = open('./adam_test_csvfile.csv', 'w')
writer = csv.writer(f)
writer.writerow(row)
f.close()