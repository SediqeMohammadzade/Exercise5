import math
def daraje2():
    while True:
          a = int(input("Enter a:"))
          b = int(input("Enter b:"))
          c = int(input("Enter c:"))

          Delta = (b**2) - (4*a*c)

          if Delta > 0:
             answer1 = (-b +math.sqrt(Delta)) / (2*a)
             answer2 = (-b -math.sqrt(Delta)) / (2*a)
             print(answer1,answer2)

          elif Delta == 0:
               answer = -b / (2*a)
               print(answer)
          else:
               print("There is no answer")

daraje2()