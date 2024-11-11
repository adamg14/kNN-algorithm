result = [
    [(10, "dog"), (10, "dog"), (20, "cat")],
    [(20, "female"), (25, "male"), (26, "female")]
]

for array in result:
    classifier_dictionary = {
        "Female": 0,
        "Male": 0,
        "Primate": 0,
        "Rodent": 0,
        "Food": 0
    }
    for element in array:
        if element[1] == "dog":
            classifier_dictionary["dog"] += 1
        elif element[1] == "female":
            classifier_dictionary["female"] += 1
        elif element[1] == "cat":
            classifier_dictionary["cat"] += 1
        else:
            classifier_dictionary["male"] += 1
    print(max(classifier_dictionary, key=classifier_dictionary.get))
