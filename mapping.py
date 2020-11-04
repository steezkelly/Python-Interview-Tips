#Python map
#Takes a function and an iterable, returns a map object,
#also an iterator, which applies the function to all elements
#in the iterable.
#NOTE: You can pass more than one iterable to map() function
#Can also convert map object to sequence objects, such as list
#tuple, etc.
#SYNTAX: map(function, iterable)
#keyword(map(passes each item of iterable to function,
#iterable which is to be mapped.))

#function to double value passed to it
def doubler(x):
  return x * 2

#creating a list
my_list = [1, 3, 5, 2, 4]

#map function takes the function doubler and the iterable
#my_list
#map will pass each element of my_list to doubler function
result = map(doubler, my_list)

#prints a list containing the doubled values
print(result)

#converting map object to set
#result here is the final answer we got in the above code
#result = [2, 6, 10, 4, 8]

#print ("Converting to set")
#answer1 = set(result)
#print(answer1)
