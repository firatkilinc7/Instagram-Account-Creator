import random, linecache

def createFullName():
    line_names = random.randint(0,18208)#rand for names.txt rows
    line_surnames = random.randint(0,88798)#rand for surnames.txt rows
    randName = linecache.getline('./assets/names/names.txt', line_names)
    randSurname = linecache.getline('./assets/names/surnames.txt', line_surnames)
    fullName = randName.strip() + " " + randSurname
    return fullName

createFullName()















