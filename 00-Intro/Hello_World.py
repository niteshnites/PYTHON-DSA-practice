print('Hello World!')


def print_items(n):
    for i in range(n): 
        print(i)
    for j in range(n): 
        print(j)

print_items(10)


def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items(10)


def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    
    for k in range(n):
        print(k)

print_items(10)


def add_items(n):
    return n + n

def add_items(n):
    return n + n + n

print(add_items(10))


def print_items(a,b):
    for i in range(a): 
        print(i)
    for j in range(b): 
        print(j)

print_items(10, 5)


def print_items(a, b):
    for i in range(a):
        for j in range(b):
            print(i,j)

print_items(10, 5)


class Cookie:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one color is: ', cookie_one.get_color())
print('Cookie two color is: ', cookie_two.get_color())

cookie_one = Cookie('yellow')

print('Cookie one color is: ', cookie_one.get_color())
print('Cookie two color is: ', cookie_two.get_color())


num1 = 11
num2 = num1

print("Before num2 value is updated:")
print("num1 = ", num1)
print("num2 = ", num2)

print("num1 points to: ", id(num1))
print("num2 points to: ", id(num2))

num2 = 22

print("After num2 value is updated:")
print("num1 = ", num1)
print("num2 = ", num2)

print("num1 points to: ", id(num1))
print("num2 points to: ", id(num2))


dict1 = {'value': 11}
dict2 = dict1

print("Before dict2 value is updated:")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print("dict1 points to: ", id(dict1))
print("dict2 points to: ", id(dict2))

dict22 = {'value': 22}

print("After num2 value is updated:")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print("dict1 points to: ", id(dict1))
print("dict2 points to: ", id(dict2))


import gc
gc.disable()  # Disables automatic garbage collection
gc.enable()   # Re-enables garbage collection

gc.collect()  # Force a garbage collection cycle

unreachable_objects = gc.collect()  # Returns the number of unreachable objects found
print(unreachable_objects)


head = {
    'value': 11,
    'next': {
        'value': 22,
        'next': {
            'value': 33,
            'next': {
                'value': 44,
                'next': {
                    'value': 55,
                    'next': None
                }
            }
        }
    }
}
print(head['next']['next']['value'])

# Below will only run with the linked list
# print(my_linked_list.head.next.next.value)

