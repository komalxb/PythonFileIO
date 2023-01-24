s = open('studentnames.txt', 'r')
temp = s.readline().rstrip('\n')
print temp
count = 1
while (temp != ""):
  temp = s.readline().rstrip('\n'))
  print(temp)
  count += 1
print(count) #prints number of students
s.close()
