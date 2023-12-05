fruits = ["Peaches","Apples","Pears"]
years = [3,"1998", 2.5,879,"1944"]

print("Apples" in fruits)
print("Apples" in fruits)

print(fruits.count("Apples"))


print(fruits,years)

#--------add an item to the list--------
fruits.append("Mango")
print(fruits)

#--------combine the 2 lists together --------
fruits.extend(years)
print(fruits)

#-------remove a fruit by name-----
fruits.remove("Peaches")
print(fruits)

#-------remove a fruit by index-----
fruits.pop(1)
print(fruits)

#-------remove a fruit by index reversing -----
fruits.pop(-1)
print(fruits)


#sort numbers
numbers = [2,231,5,556,7654,6.5]
numbers.sort()
print(numbers)