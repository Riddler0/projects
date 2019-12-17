from util import entropy, information_gain, partition_classes
import numpy as np 
import ast

class DecisionTree(object):
    def __init__(self):
        # Initializing the tree as an empty dictionary or list, as preferred
        #self.tree = []
        self.tree = {}

    def learn(self, X, y):
        # TODO: Train the decision tree (self.tree) using the the sample X and labels y
        # You will have to make use of the functions in utils.py to train the tree
        
        # One possible way of implementing the tree:
        #    Each node in self.tree could be in the form of a dictionary:
        #       https://docs.python.org/2/library/stdtypes.html#mapping-types-dict
        #    For example, a non-leaf node with two children can have a 'left' key and  a 
        #    'right' key. You can add more keys which might help in classification
        #    (eg. split attribute and split value)

        def checkEqual(lst):
            return lst[1:] == lst[:-1]

        if checkEqual(y):
            one_count = 0
            zero_count = 0

            for i in y:
                if i == 0:
                    zero_count += 1
                elif i == 1:
                    one_count += 1

            if one_count > zero_count:
                self.tree['leaf'] = [1] * len(y)

            else:
                self.tree['leaf'] = [0] * len(y)

            return self.tree

        elif len(X) <= 50:
            one_count = 0
            zero_count = 0

            for i in y:
                if i == 0:
                    zero_count += 1
                elif i == 1:
                    one_count += 1

            if one_count > zero_count:
                self.tree['leaf'] = [1] * len(y)

            else:
                self.tree['leaf'] = [0] * len(y)

            return self.tree

        elif len(y) <= 5:
            one_count = 0
            zero_count = 0

            for i in y:
                if i == 0:
                    zero_count += 1
                elif i == 1:
                    one_count += 1

            if one_count > zero_count:
                self.tree['leaf'] = [1] * len(y)

            else:
                self.tree['leaf'] = [0] * len(y)

            return self.tree 

        elif checkEqual(X):

            one_count = 0
            zero_count = 0

            for i in y:
                if i == 0:
                    zero_count += 1
                elif i == 1:
                    one_count += 1

            if one_count > zero_count:
                self.tree['leaf'] = [1] * len(y)

            else:
                self.tree['leaf'] = [0] * len(y)

            return self.tree 

        else:
            num_cols = len(X[0])
            split_attrib = 0
            split_val = 0
            info_gained = 0

            for column in range(num_cols):

                possible_values = []
                for j in X:
                    possible_values.append(j[column])

                possible_values.sort()

                quartiles = []
                quartiles = np.append(possible_values[0], [possible_values[len(possible_values) // 4], possible_values[len(possible_values) // 2], possible_values[(len(possible_values) * 2) // 3], possible_values[len(possible_values) - 1]])

                for value in quartiles:
                    if value != 0:

                        xl, xr, yl, yr = partition_classes(X, y, column, value)
                        info_2 = information_gain(y, [yl, yr])

                        if info_2 >= info_gained:
                            info_gained = info_2
                            split_attrib = column
                            split_val = value 
                    else:
                        continue

            nxl, nxr, nyl, nyr = partition_classes(X, y, split_attrib, split_val)
            self.tree['right'] = DecisionTree()
            self.tree['right'].learn(nxr, nyr)
            self.tree['left'] = DecisionTree()
            self.tree['left'].learn(nxl, nyl)
            self.tree['split_val'] = split_val
            self.tree['split_attrib'] = split_attrib

    def classify(self, record):
        # TODO: classify the record using self.tree and return the predicted label
        if 'leaf' not in self.tree.keys():
            if record[self.tree['split_attrib']] <= self.tree['split_val']:
                return self.tree['left'].classify(record)
            elif record[self.tree['split_attrib']] > self.tree['split_val']:
                return self.tree['right'].classify(record)
        else:
            try:
                return self.tree['leaf'][0]
            except:
                return self.tree['leaf']
