from PIL import Image
import image_similarity_measures
import argparse
import csv
import os
import image_similarity_measures
import sewar
from skimage import metrics
import matplotlib.image as Im

# primate image: Images/Student_Train/6_img_1553496488736.jpg
primate_image = Image.open("Images/Student_Train/6_img_1553496488736.jpg")
new_image = primate_image.resize((256, 256))
# save the new image with the new size - need to check if this works for resaving images later - it does work but there is a little deviation
# when resizing the same image 0 -> 0.001. doesnt really make a difference - what happens if both images need to be resized? - doubt
new_image.save('resizedimage.jpg')

img1 = Im.imread("Images/Student_Train/generated.photos_v3_0004655.jpg")
img2 = Im.imread("Images/Student_Train/generated.photos_v3_0027474.jpg")
img3_male = Im.imread("Images/Student_Train/generated.photos_v3_0028666.jpg")
img4_primate = Im.imread("resizedimage.jpg")

print("same image primate", sewar.mse(img4_primate, img4_primate))
# get the size of the girl in picture to d
female_image = Image.open("Images/Student_Train/generated.photos_v3_0004655.jpg")
print(female_image.size)

mean_squared_error = metrics.mean_squared_error(img1, img1)
mean_squared_error1 = sewar.mse(img1, img1)
print("same image ", mean_squared_error1)
print("female and female difference", sewar.mse(img1, img2))
print("female and male difference ", sewar.mse(img1, img3_male))
print("primate and female difference", sewar.mse(img1, img4_primate))







file = open("training_data.csv")
file1 = open("testing_data.csv")
csvreader = csv.reader(file)
csvreader1 = csv.reader(file1)
title1 = next(csvreader1)
title = next(csvreader)
training_data = []
for row in csvreader:
    training_data.append(row)



testing_data = []
for row in csvreader1:
    training_data.append(row)

# error here
count = 0
for row1 in training_data:
    for row in testing_data:
        count = count + 1
        print(row1, row)


# print(testing_data)

# image_similarity_measures.
# print(img1)
# img1.show()
# print(img1.format)




