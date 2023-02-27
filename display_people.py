from select import select

from main import People

our_people = People.select()
for People in our_people:
    print(People.name, People.phonenumber, People.email, People.country, People.gender, People.religion,
          People.password)
