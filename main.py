# Introduction of object-oriented programming: objects
# Plant: type, color, season <--- Middle: water, sunlight <--- Human: name, age, schedule ----> Work: type, salary, time

import Animal1
import Animal2
import Animal3
# Python Objects

pet = Animal1.Dog("Fito", 36)
sisterPet = Animal1.Dog("Scooby", 32)
brotherPet = Animal1.Dog("Sparky", 23)

catPet = Animal2.Cat("Garfield", 89)

# Output
print(pet.name, pet.age)
print(pet)
pet.myFunc("Bark")

print(pet, catPet)

birdPet = Animal3.Bird("Polly", 79)
print(pet, catPet, birdPet)

# * The long way * #
    #name = 'Fito'

# pet =  Dog()
# print(pet.name)
# pet.name = 'Scooby-Doo'
# print(pet.name)