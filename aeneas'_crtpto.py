import numpy as np
from math import cos, radians, ceil

r = float(input())
dict = {}     #store the angles
array = np.zeros([26, 26])       #map the distance between letters
for i in range(26):
  letter, angle = input().split()
  letter = ord(letter) - 65
  angle = float(angle)
  dict[letter] = angle

sentence = input()

# print(dict)

for i in range(26):
  for j in range(i+1, 26):
    array[i][j] = (2 * r * r * (1 - cos(radians(dict[i] - dict[j])))) ** 0.5
    array[j][i] = array[i][j]

# print(array)
# sentence_letters = ''
# last_i = 8     #letter 'I', for test
last_i = -1
distance = 0.0
for i in sentence:
  if i.isalpha():
    # sentence_letters += i.upper()
    i = ord(i.upper()) - 65
    # print(i)
    if (last_i == -1):
      last_i = i
    distance += array[last_i][i]
    last_i = i

# print(array[8][8])
distance += r
print(ceil(distance))
    
# print(sentence_letters)

