from main import People

try:
    people_name = input("Enter Name \n")
    people_phonenumber = input("Enter Phone Number \n")
    people_email = input("Enter Email \n")
    people_country = input("Enter Country \n")
    people_gender = input("Enter Gender \n")
    people_religion = input("Enter Religion \n")
    people_password = input("Enter Password \n")

    People.create(name=people_name, phonenumber=people_phonenumber, email=people_email, country=people_country,
                  gender=people_gender, religion=people_religion, password=people_password)
    print("User created successfully")

except'':
    print("Failed to create user, try again")
