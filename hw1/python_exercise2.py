#This function determines if the inputted number is a prime number or not
def prime_or_not(number):
    for i in range(2, number):
        if(number % i == 0):
            return False

    return True

#This function will print out all the numbers that are prime 
def print_number_if_prime():
    for i in range(3, 101):
        if(prime_or_not(i) == True):
            print("The number", i , "is a prime number")



def main():
    print_number_if_prime()



main()
