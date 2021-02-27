#importing the homework txt file with names and numbers
file_hw = open("homework.txt", "r")

#reading from the file
content = file_hw.readlines()
#variable for my name
name = "De'Amber"
#variable for storing sum
num_sum = 0

#Use a for loop to iterate through each line in the file
for line in content:
    #Checking for my name
    if name == "De'Amber":
        #Use a for loop to check for the integer on each line
        for num in line:
            if num.isdigit() == True:
                num_sum += int(num)
print(f"The total is: {num_sum}")
