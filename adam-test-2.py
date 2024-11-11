import argparse
import csv
import os
import PIL
import matplotlib.image as Im
import sewar

def read_csv_file(filename):
    lines = []
    with open(filename, newline='') as infile:
        reader = csv.reader(infile)
        for line in reader:
            lines.append(line)
    return lines

# need to store a 2 dimensional array to store the results of the similarity
similarity_results = []
# ignore the first row
# need to add a .. in the for the answer file in the template folder to get to the root directory
training_data = read_csv_file('training_data.csv')
training_data_array = []
for row in training_data[1:]:
    image = row[0]
    image_class = row[1]
    tuple = (image, image_class)
    training_data_array.append(tuple)

testing_data = read_csv_file('testing_data.csv')
testing_data_array = []
for row in testing_data[1:]:
    image = row[0]
    tuple = (image, image_class)
    testing_data_array.append(tuple)

print(testing_data_array[120][0])
# f string in python 3.6 and above
training_data_length = len(training_data_array)
testing_data_length = len(testing_data_array)
# need to store a 2 dimensional array to store the results of the similarity - think about how i am going to sort this list
similarity_results = []

for i in range(testing_data_length):
    similarity_results.append([])

# i hope that this works for sorting the 2d list by the similarity, remove reverse if it is the wrong way round
# similarity_results.sort(key= lambda row: (row[0]), reverse=True)
i = 0
j = 0
for i in range(testing_data_length):
    for j in range(training_data_length):
        test_image = testing_data_array[i][0]
        training_image = training_data_array[j][0]
        training_class = training_data_array[j][1]
        # .. to get to the root directory to read the images
        test_img = Im.imread(f"{test_image}")
        train_img = Im.imread(f"{training_image}")
        # need to resize the train_img to make sure that we can compare it
        # get the size of the test image
        test_img1 = PIL.Image.open(f"{test_image}")
        train_img1 = PIL.Image.open(f"{training_image}")
        
        test_img2 = test_img1.size
        new_image = train_img1.resize((test_img2[0], test_img2[1]))

        # save the resized image
        new_image.save('resizedimage.jpg')
        train_img2 = Im.imread("resizedimage.jpg")
        # can now compare the two images
        similarity_measure_1 = sewar.mse(test_img, train_img2)
        result_tuple = (similarity_measure_1, training_class)
        similarity_results[i].append(result_tuple)
        if similarity_measure_1 < 1800:
            print(similarity_measure_1, training_class)
    print("new image")


# similarity results
k = 10
sorted_similarity_measure = []
# sort the comparison images by closeness
for array in similarity_results:
    sort_array = sorted(array)
    k_length_array = sort_array[:k]
    sorted_similarity_measure.append(k_length_array)

# for array in sorted_similarity_measure:
#     print(array)

# now we have an array - we need to do a voting system for which is the most common neighbour
for array in sorted_similarity_measure:
    classifier_dictionary = {
        "Female": 0,
        "Male": 0,
        "Primate": 0,
        "Rodent": 0,
        "Food": 0
    }
    for element in array:
        if element[1] == "Primate":
            classifier_dictionary["Primate"] += 1
        elif element[1] == "Female":
            classifier_dictionary["Female"] += 1
        elif element[1] == "Rodent":
            classifier_dictionary["Rodent"] += 1
        elif element[1] == "Food":
            classifier_dictionary["Food"] += 1
        else:
            classifier_dictionary["Male"] += 1
    print("k-NEAREST-NEIGHBOURS", max(classifier_dictionary, key=classifier_dictionary.get))