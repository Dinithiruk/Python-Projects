name='tom'
age=23
print("Happy birthday "+ name +". You are now " + str(age))

carModel="Benz"
quote="The best model in the world is "+ carModel
print(quote)
print("Convert to lower case : "+ quote.lower())
print( quote.islower())                      # cant convert boolto str 
print("Convert to upper case : "+quote.upper())
print(quote.isupper())                       # cant convert boolto str 
print(len(quote))
print(quote[0])# to find value with index , here 3rd index is the space 
print(quote.index("b"))# to find index with value 
print(quote.replace("model","brand"))
