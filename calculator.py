def add(num_1, num_2):
 return num_1 + num_2

def sub(num_1, num_2):
 return num_1 - num_2

def multiply(num_1, num_2):
 return num_1 * num_2

def divide(num_1, num_2):
 return num_1 / num_2

print("operations")
print("addition ")
print("subtraction")
print("multiplication")
print("divison")
while True:
    # take input from the user
    print(" choose 1 for additon ")
    print(" choose 2 for subtraction ")
    print(" choose 3 for multiplication ")
    print(" choose 4 for divion  ")
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
       try:
         
         num_1 = float(input("enter the number_1:"))
         num_2 = float(input("enter the number_2:"))
        
       except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    if choice == '1':
               print(num_1, "+", num_2, "=", add(num_1, num_2))
    elif choice == '2':
                    print(num_1, "-", num_2, "=", sub(num_1, num_2))
    elif choice == '3':
                 print(num_1, "*", num_2, "=", multiply(num_1, num_2))
    elif choice == '4':
                 print(num_1, "/", num_2, "=", divide(num_1, num_2))

    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
            break
    else:
             print("Invalid Input")

   
