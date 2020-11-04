#Fizz Buzz

for num in range(1,101):
  if num % 5 == 0 and num % 3 == 0:
    print ("FizzBuzz")
  elif num % 3 == 0:
    print ("Fizz")
  elif num % 5 == 0:
    print ("Buzz")
  else:
    print (num)

#Fibonacci Sequence
#a, b = 0, 1
#for i in range(0, 10):
#    print (a)
#    a,b = b, a + b

#Fibonacci Generator
def fib(num):
    a,b = 0,1
    for i in range(0, num):
        yield "{}: {}".format(i+1, a)
        a,b = b, a+b

for item in fib(10):
    print(item)


#Doubles, i.e. 1, 2, 4, 8, 16, 32, 64, 128, 256
#a = 0
#b = 1
#for i in range(0, 10):
#    print(a)
#    a = b
#    b = a + b
