# Code by Tajrina Promela
# Date 16th September 2022, 7:20 PM
# Code Generator in Python

s = []

def code_generator(string):
   for i in range(len(string)):
      if string[i] == 'A' or string[i] == 'a':
         string = string.replace('A', 'C')
         string = string.replace('a', 'c')
         s.append(string[i])
         continue

      elif string[i] == 'G' or string[i] == 'g':
         string = string.replace('G', 'D')
         string = string.replace('g', 'd')
         s.append(string[i])
         continue

      elif string[i] == 'C' or string[i] == 'c':
         string = string.replace('C', 'A')
         string = string.replace('c', 'a')
         s.append(string[i])
         continue

      elif string[i] == 'D' or string[i] == 'd':
         string = string.replace('D', 'G')
         string = string.replace('d', 'g')
         s.append(string[i])
         continue

      elif string[i] == 'F' or string[i] == 'f':
         string = string.replace('F', 'U')
         string = string.replace('f', 'u')
         s.append(string[i])
         continue

      elif string[i] == 'H' or string[i] == 'h':
         string = string.replace('H', 'I')
         string = string.replace('h', 'i')
         s.append(string[i])
         continue

      s.append(string[i])

code_generator(input("Enter a string: "))

str = ''.join(s)
print(str)