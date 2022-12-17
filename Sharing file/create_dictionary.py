
import pickle
import json
import socket


## to populate a dictionary from a loop

# Creating an empty Dictionary
dic3 = {}
print("Empty Dictionary: ")
print(dic3)
print(type(dic3))

# Creating a Dictionary with dict() method
dic3 = dict({1: 'Queen', 2: 'of', 3: 'UK'})
print("\nDictionary with the use of dic3(): ")
print(dic3)
print(type(dic3))

# Creating a Dictionary with each item as a Pair
Dict = dict([(1, 'Queen'), (2, 'of')])
print("\nDictionary with each item as a pair: ")
print(Dict)

# serliazation and deserilization
# "wb" argument opens the file in binary mode

with open("test.pickle", "wb") as outfile:
    pickle.dump(dic3, outfile)
print("Written dictionary", dic3)

# to recover and deserialization
with open("test.pickle", "rb") as infile:
    dic3_recover = pickle.load(infile)
print("Reconstructed object", dic3_recover)

# to check the process
if dic3 == dic3_recover:
    print("Reconstruction  processed successfully")

## serilization of Dic
with open("test.pickle", "wb") as outfile:
    pickle.dump(Dict, outfile)
print("Written dictionary", Dict)

# to recover and deserialization
with open("test.pickle", "rb") as infile:
    dict_recover = pickle.load(infile)
print("Reconstructed object", dict_recover)

# to check the process
if Dict == dict_recover:
    print("Reconstruction processed of Dict successfully")
