## Game of Threes## 
num = int(input("please give a number."))
print(num)
steps = int(0)
while num != 1:
  if num % 3 == 2:
    num += 1
  elif num % 3 == 1:
    num += -1
  num /= 3
  steps += 1
  print(str(num) + "in " + str(steps) + " steps!")
