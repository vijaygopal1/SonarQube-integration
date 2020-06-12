name_lists= [ "Vj", "Aj" , "Ct" , "Rs" ]


while True:
    print("Welcome To Travis")
    name=input("Enter your Name :").strip()

if name in name_lists:
    print("Authorised")
else:
    print("Un-Authorised")
    
