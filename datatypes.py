#Lists
#mutable ??
my_list = [10, 20, 30, 40, 50]
for i in my_list:
  print (i)

#Tuples
#immutable ??
my_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in my_tup:
  print(i)

#Dict
#key-value pairing
#'hash-table'
my_dict = {'name': 'Steve', 'age': '2', 'color': 'green'}
for key,val in my_dict.items():
  print("My {} is {}".format(key,val))

#Set
#Iterates randomly through the list, not listing duplicates
#Unordered
my_set = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50}
for i in my_set:
  print(i)
