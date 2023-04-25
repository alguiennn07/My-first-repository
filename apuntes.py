def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name()


def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
#BOTH ARE CORRECT

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(99)) # 55
print(sum_of_numbers(100)) # 5050

def money(name):
    bank_money=(f"{500+300}$")
    return bank_money
print(money("name"))

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))
def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
#Passing Arguments with Key and Value
#If we pass the arguments with key and value, the order of the arguments does not matter.
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)#NONE.WE HAVE TO ADD "RETURN"
print(print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    return (total)#NONE.WE HAVE TO ADD "RETURN"
print(add_two_numbers(num2 = 3, num1 = 2))

#RETURNING A BOOLEAN
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False   

def find_even_numbers(n):
    evens = []
    for i in range(n+1):#WE ADD 1 SO WHEN WE PUT A NUMBER LIKE 10(EVEN) IT RETURNS IT.
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))



