import math
from functools import reduce

class Calculator:
    """Calculator class"""
    def __init__(self, value1, value2) -> None:
        self._v1 = value1
        self._v2 = value2

    def addition(self):
        return self._v1 + self._v2

    def substraction(self):
        return self._v1 - self._v2

    def multiplication(self):
        return self._v1 * self._v2

    def divison(self):
        return self._v1 / self._v2


def get_user_inputs():
    return [int(x) for x in input('Enter two values for operation: ').split()]


def perform_operation(user_choice, arg_list):
    print(f'arg_list = {arg_list}')
    if len(arg_list) == 2:
        cal_obj = Calculator(arg_list[0], arg_list[1])
        if user_choice == 1:
            print(f'Result = {cal_obj.addition()}')
        elif user_choice == 2:
            print(f'Result = {cal_obj.substraction()}')
        elif user_choice == 3:
            print(f'Result = {cal_obj.multiplication()}')
        elif user_choice == 4:
            print(f'Result = {cal_obj.divison()}')
    
    elif len(arg_list) > 2:
        if user_choice == 1:
            print(f'Result = {math.fsum(arg_list)}')
        elif user_choice == 2:
            negate_list = list(map(lambda x: -x, arg_list[1:len(arg_list)]))
            negate_list.insert(0, arg_list[0])
            print(f'Result = {math.fsum(negate_list)}')
        elif user_choice == 3:
            print(f'Result = {reduce(lambda x,y: x*y, arg_list)}')
        elif user_choice == 4:
            print(f'Result = {reduce(lambda x,y: x/y, arg_list)}')

    else:
        print('Minimum 2 variables needed for operation...')
    


def check_user_interest():
    user_continue = input()
    if user_continue.upper() == 'Y':
        print('Selected Yes...')
        return True
    elif user_continue.upper() == 'N':
        print('Selected No...')
        return False
    else:
        print(f'Invalid choice - {user_continue}')
        return False           


def start_calculator(choice_dict):
    print("Choose option: ")
    print(choice_dict)
    user_choice = int(input("Your choice: "))
    if user_choice in choice_dict.keys():
        print(f'Option picked: {user_choice} - {choice_dict[user_choice]}')
        arguments_list = get_user_inputs()
        perform_operation(user_choice, arguments_list)
        print("Wish to continue? (Y/N)")
        flag = check_user_interest()
        if flag == True:
            return True
        else:
            return False
    else:
        print("Invalid choice...Wish to continue? (Y/N)")
        flag = check_user_interest()
        if flag == True:
            return True
        else:
            return False
            
            

def main():
    print("***** Calculator Processing start *****")
    choice_dict = {1 : "Addition", 2 : "Substraction", 3 : "Multiplication" ,\
                   4 : "Division"}
    flag = start_calculator(choice_dict)
    while flag == True:
        flag = start_calculator(choice_dict)
    print("***** Calculator Processing end *****")


if __name__ == "__main__":
    main()
