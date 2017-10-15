string = input()
string = string[::-1]
q = int(input())

for i in range(q):
  suffix = input()
  suffix = suffix[::-1]
  # temp = string
  # print(string)
  # print(suffix[0])
  count = 0
  for str in string:
    if len(suffix) == 0:
      break;
    if str == suffix[0]:
      count = count + 1
      suffix = suffix[1:]
  print(count)