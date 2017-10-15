num = int(input())
dict={}
heights=[]
count = 1;
for i in range(num):
  name, h = input().split()
  # print(type(name))
  # print(type(h))
  h = int(h)
  if h not in dict:
    dict[h] = (name)
  else:
    dict[h] += (' '+ name)
  if h not in heights:
    heights.append(h)

heights.sort()
for h in heights:
  names = dict[h].split()
  names.sort()
  # print(names)
  print(' '.join(names) + ' ' + str(count) + ' ' + str(count + len(names)-1))
  count = count + len(names)
 
      
