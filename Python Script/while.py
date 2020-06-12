from random import choice

questions= ["Why are you late :", "What are you doing :", "Where are you going :"]

questions=choice(questions)
answer=input(questions).strip()

while answer !="dont disturb":
    answer=input("why")

print("Ok")
