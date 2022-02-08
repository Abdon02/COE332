#function will square and cube every element of the inputted list
def square_or_cube_list_elements(listname, degree):
    end_result = []
    for element in listname:
        multiplication = 1
        for i in range(degree):
            multiplication = multiplication * element
        end_result.append(multiplication)
    return end_result


#function will print out all the lists
def print_list(list_int1, list_int2, list_int3):
    for i in range(len(list_int1)):
        print(list_int1[i], "", list_int2[i], "", list_int3[i])


def main():
    list_int1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_int2 = square_or_cube_list_elements(list_int1, 2)
    list_int3 = square_or_cube_list_elements(list_int1, 3)

    print_list(list_int1, list_int2, list_int3)

main()
