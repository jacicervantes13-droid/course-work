text = """"
a b c a a b
"""

print(text.split())

word_count = {}

for word in text.split():
     if word in word_count:
       word_count[word] += 1 
     else:
      word_count[word] = 1 

print(word_count)

def bark():
   print("Woof woof!")
   print("I'm a dog!")
  

bark()
bark()

for x in range(15):
  bark()

def hello():
  print("Hello Jaci!!")

hello()

def hello(name):
  print(f"Hello {name}!")

hello("Fernando ;)")

def add_numbers(num1,num2,num3):
   print(num1 + num2 + num3)

add_numbers(5,20,23)


def dog_info(age, name):
   print(f'Hi my name is {name} and i am {age} years old')

dog_info(4, "blue")

def double(number):
   return number * 2 

print(double(5))

new_number = double(5)

print(new_number)

def uppercase(text):
   return text.upper()

print(uppercase("jaci"))









