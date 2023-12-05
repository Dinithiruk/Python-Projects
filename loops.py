#------------------list loop -----------
fruit_list = ["Apples","Papaya","Mango"]

for fruits in fruit_list:
    print("Would you like {} ? ".format(fruits))

#------------------range loop-----------
for number in range(1,11):
    print("Number {}".format(number))

# ------------------While loop-----------
temp_farenheit = 40

while temp_farenheit >32:
    print("The water is {} degree.".format(temp_farenheit))
    temp_farenheit -= 1

# ------------------ loop controls(BREAK CONTINUE PASS)-----------
# Break
while temp_farenheit >32:
    print("The water is {} degree.".format(temp_farenheit))
    temp_farenheit -= 1
    if temp_farenheit == 33:
        break

#continue
for number in range(1,11):
    if number == 7:
        print("We re skipping number 7 ")
        continue
    print("This is the number {}".format(number))

#pass
for number in range(1,11):
    if number == 3 :
        pass
    else:
        print("This number is {}".format(number))

