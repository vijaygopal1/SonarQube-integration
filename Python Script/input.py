# Ask user age

age = input("Enter age? :")


# Ask user name

name =input("Enter Name? :")


# Ask user city
city= input ("Enter city?:")

#Ask interest

interest=input ("What's interest?:")

# Create output Text

string = "Your name is {} Your age is {} You live in {} and Your interest is {}"
output =string.format(name,age ,city,interest)

#Print outPut in screen

print(output)
