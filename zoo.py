zoo = ("dog", "elephant", "bobcat", "giraffe", "lion", "eagle", "panda", "bear", "gorilla", "kangaroo")

print(zoo.index("elephant"))

animal_to_find = "gorilla"



if animal_to_find in zoo:
    print(f"{animal_to_find} is found in the zoo")


(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = zoo


print(first_animal)
print(second_animal)
print(third_animal)


zoo_list = list(zoo)

zoo_list.extend(['koala','llama','hawk'])


zoo = tuple(zoo_list)

print(zoo)


