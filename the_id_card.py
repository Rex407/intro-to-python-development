print("please enter the following information: ")

print()

# ask for the basic information
first = input("first name: ")
last = input("last name: ")
email = input("email address: ")
phone = input("phone number: ")
job_title = input("job title: ")
id_number = input("ID number: ")

# ask for the aditional information
hair_color = input("hair color")
eye_color = input("Eye color: ")
month = input("starting month: ")
training = input("completed additional training? ")

# now print out the ID card
print("\nThe ID card is:")
print("----------------------------------------")
print(f"{last.upper()}, {first.capitalize()}")
print(job_title.title())
print(f"ID: {id_number}")
print()
print(email.lower())
print(phone)
print()

print(f"Hair: {hair_color:15} Eyes: {eye_color}")
print(f"month: {month:14} training: {training}")
print("---------------------------------------------")