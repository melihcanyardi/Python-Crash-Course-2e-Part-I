num_people = input("How many people are there in your dinner group? ")
num_people = int(num_people)

if num_people > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")
