# 1) შექმენით ფუნქციოა სახელად filter_odd რომელსაც გადაეცემა ერთი არგუმენტი და ეს არის რიცხვების სია,
#  თვქენი დავალებაა დააბრუნოთ ფუნქციიდან ახალი სია სადაც მხოლოდ იქნება ლუწი რიცხვები მოცემული
#  (აგრეთვე ახსენით რა არის ფუნქცია, პარამეტრი, არგუყმენტი და რგორო უნდა გამოვიძახოთ ის)

# def filter_odd(numbers_list):
#     even_numbers = []
#     for number in numbers_list:
#         if number % 2 == 0:
#             even_numbers.append(number)

#     return even_numbers       

# result = filter_odd([1,2,3,4,5,6,7,8,9,10])

# print(result)


# 2) შექმენით ფუნქცია სახელად even_sum, რომელსაც გადასცემთ რიცხვების სია,
# თქვენი დავალებაა ამ სიაში შეკრიბოთ ლუწი რიცხზვები და მიღებული ჯამი დააბრუნოთ ფუნქციიდან

def even_sum(numbers_list):
    even_numbers = []
    for number in numbers_list:
        if number % 2 == 0:
            even_numbers.append(number)
        sum(even_numbers)

    return sum(even_numbers)     

result = even_sum([1,2,3,4,5,6,7,8,9,10])

print(result)


# 3) შექმენით ფუნქცია სახელად odd_index_sum რომელსაც გადაეცემა რიცხვების სია, თქენი დავალებაა შეკრიბოთ ყველა ის რიცხვი რომელიც დგას !!!!კენტ ინდექსზე!!!, მიღებული ჯამი დააბრუნეთ ფუნქციიდან