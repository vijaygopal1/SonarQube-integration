#Adding Names to List

active_user=["Vj", "Kg", "Aj", "Ct"]

#Check for condition & Print result

while True:
    print("Hey, Welcome to travis")
    name=input("Enter Name :")

    if name in active_user:
        print("Hello {}".format(name))
        remove=input("Would you like to be removed (y/n)?:").lower()

    if remove=="y":
        print(active_user)
        active_user.remove(name)
        print(active_user)
    elif:
        print("I dont have you yet {}".format(name))
        add=input("Would you like to get added (y/n)? :").lower

    if add=="y":
        print(active_user)
        active_user.append(name)
        print(active_user)

    elif add=="n":
        print("No problem, great day!")
