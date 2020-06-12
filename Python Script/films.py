movies={
    "Bigil":[18,5],
    "Enpt":[11,12],
    "Master":[20,1],
    }

while True:
    choice=input("Enter movie name :")

    if choice in movies:
        age=int(input("Enter age :")

    if age >=movies[choice][0]:

    num_seats = movies[choice][1]

    if num_seats > 0:
         print("Ennjoy movie")
         movies[choice][1]=movies[choice][1]-1

    else:
        print("We are sold")

    else:
        print("Too young")

   else:
       print("No movie")
