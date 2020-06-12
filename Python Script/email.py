#Ask email

email=input("enter email?:").strip()

# slice username
user=email[:email.index("@")]

#slice domain

domain=email[email.index("@")+1:]

#Output

output="Your email is {} & domain is {}".format(user,domain)
print(output)


