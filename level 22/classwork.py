# 1) შექმენით ფუნქცია სახელად add რომელსაც ექნება ორი პარამეტრი, სახელად num1 num2, ამ პარამეტრებმ,ა უნდა მიიღოს რიცხვები და ფუნქციამ უნდა დაბეჭდოს ამ ორი რიცხვის ჯამი

# def add(num1, num2):
#     print(num1 + num2)

# add(3, 3)


# შექმენით ფუნქცია რომელსაც გადაეცემა 2 რიცხვი. ამ ფუნქციას უნდა დაარქვათ calculate.
# უნდა დაბეჭდოთ რომელი ოპრეაციის არჩევა შეუძლია მომხმარებელს და შემდეგ უნდა ჩაატაროთ ის ოპერაცია იმ ორ რიცხვს შორის რომელიც მომხმარებელმა შემოიყვანა

# multimple
# devide

def calculate(num1, num2):  
    print("1 = *")
    print("2 = /")
    print("3 = +")
    print("4 = -")
    choice = int(input("choose operation: "))
    result = 0
    if input == 1:
        result = (num1 * num2)

    elif input == 2:
        result = (num1 / num2)

    elif input == 3:
        result = (num1 + num2)
        
    elif input == 4:
        result = (num1 - num2)

    return result
print(calculate(5, 10))



    # else:
    #     print("wrong number!!! enter again")


#   1 == num1 * num2
#     2 == num1 / num2
#     3 == num1 + num2
#     4 == num1 - num2




