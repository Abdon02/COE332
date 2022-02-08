#This function will print wether the number is even or odd
def even_or_odd(list_int):
    for element in list_int:
        if(element % 2 == 0):
            print('The number', element, 'is even')
        else:
            print('The number', element, 'is odd')



def main():
    #creating an list with 10 intergers
    list_int = [10, 20, 35, 43, 56, 69, 76, 89, 99, 120]
    even_or_odd(list_int)

main()
