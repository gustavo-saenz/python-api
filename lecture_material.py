import random
from operator import concat
from os import remove
from selectors import SelectSelector
from sys import intern
from xml.sax.handler import property_interning_dict

#print("Hello World!, really?")
ex_var = 5
float_1 = 1.03
int_1 = 4
bool_1 = True
int_1 = 6
#print(int_1)
# I need to make sure I do this correctly
exponentiation = 4 ** 4
floor_division = 16 // 5
modulo = 7 % 3 # returns the remainder of the result, but not the result
add_assign = 5
add_assign += 7 # This is how I increment the value of the variable. This applies for all the math operators
twoint = 5 + 7
#print("I am very happy with my modulo value: ",modulo)
diffint = 5 - 2
division = 5 / 3
mult = 4 * 5
expon = 3 ** 8
floordiv = 10 // 3
newmod = 17 % 5
letsround = round((23456/343),3)
#print("This is my operation rounded: ",letsround)

grocerytotal = 16.68 + 6.98 + 16.78 + 15.26 + 3 + 4.39
#print("Your shopping subtotal is ",grocerytotal)

# These are ways to print characters from a string variable in a sliced way
tavo = "Just do it!"
#print(tavo[-1])
#print(tavo[5:7]) # print from the begining and stop on a specific character
#print(tavo[8:]) # print from a specific character to the end
#print(tavo[:4]) # print a specific range of characters form the string
newvar = "Don't " + tavo[5:]
#print("This is my new variable ",newvar)
# the function type() gives you the type of variable used
# the function str() converts whatever value to the string data type
#print("The weirdest escape character is c:\ because it is just extremely annoying, like the \\")
#print("*******\n *****\n  ***\n   *")
# fullname = input("What is your name? ")
# quest = input("What is your quest? ")
# color = input("What is your favorite color? ")
# print("Hi "+fullname+". Your quest "+quest+" unfortunately is not available in "+color+" color")


def rectangular_prism(l=1, w=1, h=1):
    return l*w*h


# length = int(input("Provide the lenght of the prism: "))
# width = int(input("Provide the widht of the prism: "))
# height = int(input("Provide the height of the prism: "))
# print("The volume of your rectangular prism is: " + str(rectangular_prism(length,width,height)) + "m3")

# celsius = 0

# def farenheit(c=0):
#     return round((1.8 * c + 32),1)


# celsius = int(input("Provide your Celsius temperature: "))
# print(str(celsius) + " Celsius correspond to " + str(farenheit(celsius)) + " Farenheit")

gallons = random.randint(10,25)
miles = random.randint(200,400)


def mgp():
    return miles // gallons


# print("Driving "+ str(miles) + " miles with a tank of " + str(gallons) + " gallons gives you a consumption of " + str(mgp()) + " mpg")

def calculate_grade(sc):
    if sc >= 90:
        return "A"
    else:
        if sc >= 80:
            return "B"
        else:
            if sc >= 70:
                return "C"
            else:
                if sc >= 60:
                    return "D"
                else:
                    return "F"

# score = int(input("Please provide the student's score: "))
# print("The student's grade is " + calculate_grade(score)+ " according to his score of " + str(score))
def generate_roman(num):
    if num < 1:
        print("The value is lower than 1")
    elif num == 1:
        print("The roman numeral of " + str(num) + " is I")
    elif num == 2:
        print("The roman numeral of " + str(num) + " is II")
    elif num == 3:
        print("The roman numeral of " + str(num) + " is III")
    elif num == 4:
        print("The roman numeral of " + str(num) + " is IV")
    elif num == 5:
        print("The roman numeral of " + str(num) + " is V")
    elif num == 6:
        print("The roman numeral of " + str(num) + " is VI")
    elif num == 7:
        print("The roman numeral of " + str(num) + " is VII")
    elif num == 8:
        print("The roman numeral of " + str(num) + " is VIII")
    elif num == 9:
        print("The roman numeral of " + str(num) + " is IX")
    elif num == 10:
        print("The roman numeral of " + str(num) + " is X")
    else:
        print("The number is higher than 10")


#roman = random.randint(1,10)
#generate_roman(int(roman))


def mycounter(maxnum=10):
    print("Counter initiated from " + str(maxnum))
    while maxnum > 0:
        print(maxnum)
        maxnum -= 1

#counter = int(input("Enter the number to initiate the counter: "))
#mycounter(counter)

def numbersum(num=10):
    addnum = num
    while addnum > 0:
        addnum -= 1
        num += addnum
    return num

#summa = int(input("Enter a number: "))
#print("The sum of " + str(summa) + " is :" + (str(numbersum(summa))))

#reite = str(input("What do you want me to repeat?"))
#for letter in reite:
#    print(letter)

def wordounter(inword):
    cont = 0
    for i in inword:
        cont+=1
    return cont


#myword = input("Enter a sentence that needs word counting: ")
#print("Your sentence \"" + myword + "\" contains " + str(wordounter(myword)) + " letters")

#range = range(1,51,1)
#for i in range:
#    if i % 3 == 0 and i % 5 == 0:
#        print("FizzBuzz")
#    elif i % 3 == 0:
#        print("Fizz")
#    elif i % 5 == 0:
#        print("Buzz")
#    else:
#        print(str(i))

#mixed_case = "A Song of Ice and Fire"
#print("Is it ALL upper case? " + str(mixed_case.isupper()))
#print("Is it ALL lower case? " + str(mixed_case.islower()))
#print("This is how it looks in upper case: " + str(mixed_case.upper()))
#print("This is how it looks in lower case: " + str(mixed_case.lower()))
#print("Is this text a title case? " + str(mixed_case.istitle()))
#title_case = mixed_case.title()
#print("This is how the text should look as title case: " + title_case)
#print(mixed_case.startswith("A"))
#rint(mixed_case.endswith("e"))
#words = mixed_case.split()
#print(words)
#print ("".join(words).isalpha())

#the_string = "North Dakota."
#print(the_string.rjust(17))
#print(the_string.ljust(17,"*"))
#center_plus = the_string.center(16,"+")
#print(center_plus)
#print(the_string.lstrip("North"))
#print(center_plus.rstrip("+"))
#print(center_plus.strip("+"))
#print(the_string.replace("North","South"))

#normal_string = input("Enter a string that needs to be reversed: ")
#reverse_string = ""
#cont = len(normal_string)
#for i in range(len(normal_string) -1, -1, -1):
#    reverse_string += normal_string[i]
#print("The reversed string looks like this: " + reverse_string)

def word_counter(text):
    wordcount = 0
    for i in text:
        if i == " ":
            wordcount+=1
    return wordcount+1

#wordcount = input("Enter the text: ")
#print("This text contains " + str(word_counter(wordcount)) + " words")

#mylist = [1, 2.456, True, "hola", [1, 2, 3]]
#textlist = list("Veamos")
#isethere = "e" in textlist
#isanotthere = "a" not in textlist

#print(textlist)
#print(isethere)
#print(isanotthere)

#mylist =[[0, 2], [4, 6], [8, 10], [12, 14]]
#print(mylist[0])
#print(mylist[3][1])
#textlist = ["chair", "table", "desk", "lamp", "bed"]
#print(textlist[-5])
#oncate = "Most people own at least {} {}.".format(mylist[0][1], textlist[0])
#print(concate)
#thirdlist = [0.98, 8.76, 6.54, 4.32]
#print(thirdlist[1:])
#print(thirdlist[1:3])
#print(thirdlist[:2])

#arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
#del(arctic_animals[4])
#arctic_animals.remove("elephant")
#arctic_animals.append("arctic fox")
#print(arctic_animals)
#rctic_animals.insert(2, "snowy owl")
#rint(arctic_animals)
#rctic_animals.sort()
#rint(arctic_animals)
#rint(arctic_animals.index("reindeer"))
#arctic_pop = arctic_animals.pop()
#print(arctic_pop)

#technology = {"pc": "hp", "Console": "Play Station 5", "TV": "LG", "headset": "plantronics", "mobile": "iphone"}
#print(technology["TV"])
#print("mobile" in technology)
#print("headsets" not in technology)
#songs = {"Queen": "Bohemian Rhapsody",
#         "Bee Gees": "Stayin' Alive",
#         "U2": "One",
#         "Michael Jackson": "Billie Jean",
#         "The Beatles": "Hey Jude",
#         "Bob Dylan": "Like A Rolling Stone"}
#print(len(songs))
#for key in songs.keys():
#    print(key)
#print(songs.values())
#for key, value in songs.items():
#    print(key, value)
#print(songs.get("Promise of the Real", "This key doesn't exist on this dictionary"))
#lettersdict = {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant")
#for key, value in lettersdict.items():
#    print(key, value)
#fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
#print(fast_food_items.pop("McDonald's"))
#fast_food_items.popitem()
#print(fast_food_items)

#internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
#another_one = {"shroud": "Twitch"}
#internet_celebrities.update(another_one)
#newcelebs = internet_celebrities.copy()
#internet_celebrities.clear()
#print(internet_celebrities)
#print(newcelebs)


