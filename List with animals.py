animal = ["Bird", "Fox", "Cat", "Rat","Alligator"]
animal.append("giraffe")
moreAnimal = ["monkey", "ant eater", "red panda"]

animal.extend(moreAnimal)

animal.insert(4, "Snake")

animal.pop(3)

animal.remove("Snake")

for counter in animal:
    print(counter)
