

import pickle
import json
import socket


"""
## example 1
## for a defined dictionary

dic1={1: "Queen", 2: "London", 3:"UK"}
dic2={'name': "Queen", 'city': "London", 'country':"UK"}

print(dic1)
print(dic2["country"])

# convert dic1 to json 
print(type(dic1))

# convert into JSON:
jdic1 = json.dumps(dic1)

# result is a JSON string:
print(jdic1)
print(type(jdic1))
"""

## example 2
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

"""
## serlization and deserilization process
## covnerting the dictionary to be transmitted

dic4 = {"name": "Queen!", "city": "London"}
# serialization
# "wb" argument opens the file in binary mode
with open("test.pickle", "wb") as outfile:
    pickle.dump(dic4, outfile)
print("Written dictionary", dic4)

# to recover and deserialization
with open("test.pickle", "rb") as infile:
    dic4_recover = pickle.load(infile)
print("Reconstructed object", dic4_recover)

# to check the process
if dic4 == dic4_recover:
    print("Reconstruction  processed successfully")
"""

## serliazation and deserilization for example 3
# serialization
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