import random

# This Script will take two numbers and apply Gauss's equasion to them.


gauss_list = []

def num_input(input_text):
    try:
        input1 = input(input_text)
        if input1.upper() == "RANDOM":
            gauss_list.append(random.randint(0,1000000))
        elif int(input1) > 0 and int(input1) <= 1000000:
            gauss_list.append(int(input1))

        else:
            print("Invalid Input, Please enter a number between 0 and 1M")
            print("Or Type 'Random' for a random number\n")
            num_input(input_text)
    except:
        print("Invalid Input, Please enter a number between 0 and 1M")
        print("Or Type 'Random' for a random number\n")
        num_input(input_text)


# class Methods:
#     def __init__(self, list):
#         self.list = list

# def gauss_m(list): #uses guass method to add all intigers in range
#     gm = ((max(self.list)-min(self.list)+1)*(max(self.list)+ min(self.list))/2)
#     print(int(gm))
#
# def stand_m(list):
#     sm = 0  # calculates all intigers using a loop
#     for i in range(min(self.list),(max(self.list)+1)):
#         sm += i
#     print(int(sm))




def gauss_m(list): #uses guass method to add all intigers in range
    gm = ((max(list)-min(list)+1)*(max(list)+ min(list))/2)
    print(int(gm))
    return gm

def stand_m(list):
    sm = 0  # calculates all intigers using a loop
    for i in range(min(list),(max(list)+1)):
        sm += i
    print(int(sm))
    return sm

# Start program sequance
#
print("Carl Fredrich Gauss was an 18th centurey German mathmation.")
print(" Who was known for making significat contributions to Physics")
print(" astronomy, and algebra.\n")
print("However, He was also known for skrewing around in school and ")
print("Upsetting his teachers. One day, his teacher decided to disipline ")
print("the Young Gauss by making him add up every intiger between 1-100.\n")
pause1 = input("(press enter to continue)")
print("But his teacher soon realized that he was dealing with a protagy")
print("when the young Gauss finished the assinment within seconds to the ")
print("astonishment of His teacher. \n")
pause2 = input("(press enter to continue)")
print("Gauss realzied that in order to add all the intigers between two ")
print("intigers, a person only needs to add the first intiger to the last,")
print("then multiply by the number of intigers between the two, and divide ")
print("that by two.\n")
pause3 = input("(press enter to continue)")
print("This program will test this algorithm using modern computing. ")
print("We will take two intigers between 1 and 1,000,000 and add every intiger")
print("in the range. We will do this using Gauss's method, and by using ")
print("python to add all the intigers the conventional way.\n")
pause4 = input("(press enter to continue)")

#  requests two numbers from user and puts them in the list
num_input("Enter the first number in the range or type 'random' for a random \n integer between 1 and 1,000,000:  ")
num_input("Enter the second number in the range or type 'random' for a random \n integer between 1 and 1,000,000:  ")

print(f" The two numbers are: {gauss_list}")
# method2 = Methods(gauss_list)
# method1 = Methods(gauss_list)
# method2.stand_m()
# method2.gauss_m()
method1 = int(gauss_m(gauss_list))
method2 = int(stand_m(gauss_list))

print("==================================================")
print(f"The answer using the Gauss method is: {method2}")
print(f"the answer using the looping method is: {method1}")

if method1 == method2:
    print("The two answers are equal, Gauss's method is still valid!!!!")
else:
    print("Congratulations, you disproved Gauss, you managed to break \n the fabric of space and time and opened an interdimentional portal! \n Bow to your new Alien Overloards!!")
