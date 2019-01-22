#fuctions

#first_num = 40
#second_num = 60

#define a fuction declare
def sum_numbers(first_num, second_num):
    sum_num = first_num + second_num
    return sum_num

#declare diff_numbers fuction
def diff_numbers(first_num, second_num):
    diff_num = first_num - second_num
    return diff_num

#declare name
def print_name():
    name = input ("what is your name")
    print("your name is "+ name) 


#call a fuction
print(sum_numbers(40, 60))
print(diff_numbers(40, 60))    
print_name()

