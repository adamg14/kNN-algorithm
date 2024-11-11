# this file is for testing the k-fold task!
# we split the training data into k parts, and we have k rounds

def read_csv_file(filename):
    lines = []
    with open(filename, newline='') as infile:
        reader = csv.reader(infile)
        for line in reader:
            lines.append(line)
    return lines

# k will be inputted - take k to be 10 for example
k = 10

# maybe i need to do this with the my predictions includede maybe not
training_data = training_data = read_csv_file('testing_data.csv')
training_data_array = []
for row in training_data[1:]:
    training_data.append(training_data_array)

test_data_number = len(training_data_array)
# this is how many records we will have per split - a bit confusing
how_many_records_per_k = test_data_number/k
for i in range(k):
    new_testing_data = training_data[k]
    # then the rest of the training data remains the training data
    # then you need to train the testing data against the training data
    # then i need to keep the measure results for each round
    # then at then end do an average of the evaluation scores for each of the rounds and then this will give us a good value
    # for how the kNN algorithm will work on other data sets

# if a given image is not in the testing fold in a given round there is no need to write a class for it in that round