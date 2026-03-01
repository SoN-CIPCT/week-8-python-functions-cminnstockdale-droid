# Week8-Functions
#Create one Python file homework8_<firstname_lastname>.py and perform the following exercise:
#1.	Create a function that accepts a list of sandwich ingredients.
#2.	The function should have one parameter that can collect as many arguments as the function call provides.
#3.	The function should print a summary of the sandwich being ordered.
#4.	Call the function two times with a different number of arguments. 


#Steps #1 & Steps #2
def make_sandwich(*ingredients):
    #step 3 is to print a sandwich order summary at the beginning of the list of ingredients
    print("\n Sandwich Order Summary:")
    
    for ingredient in ingredients:
        print(f"- {ingredient}")

    print("Enjoy your sandwich!\n")

# 4. Call the function twice with different numbers of arguments
make_sandwich("turkey", "lettuce", "avocado", "mayo")

make_sandwich("ham", "havarti", "mustard", "horseradish")




