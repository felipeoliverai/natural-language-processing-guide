import os

path = '/path/text.txt'

with open(path, "r") as file: 
  text = file.read()

print(text)
