# *args and **kwargs lesson/understanding*

# *args = not sure how many arguments passed to function,
# allows an arbitrary number of arguments to your function.

def print_everything(*args):
  for count, thing in enumerate(args):
    print( '{0}. {1}'.format(count, thing))

print_everything('apple', 'banana', 'cabbage')
#output
#0. apple
#1. banana
#2. cabbage

#kwargs= allows handling named arguments not defined in advance

def table_things(**kwargs):
    for name, value in kwargs.items():
        print( '{0} = {1}'.format(name, value))

table_things(apple = 'fruit', cabbage = 'vegetable')

#output
#apple = fruit
#cabbage = vegetable

#Can use these along with name arguments too.
#Explicit arguments get values first,
#then everything else passed to *args and **kwargs.
#Named arguments come first in the list.
#For example:
# def table_things(titlestring, **kwargs)

#Can also use both in same function definition,
#but *args must occur before **kwargs
#Can also use * and ** syntax when calling a function.
#For example:
def print_three_things(a, b, c):
    print( 'a = {0}, b = {1}, c = {2}'.format(a,b,c,))

mylist = ['aardvark', 'baboon', 'cat']
print_three_things(*mylist)
#Output
#a = aardvark, b = baboon, c = cat
