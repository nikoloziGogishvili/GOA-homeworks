# # მომხმარებელს შემოატანინეთ თავისი სახელი და პირველი ასო გარდაქმენით დიდ ასოთ

# name = input("please enter your name: ")

# capitalized_name = name.capitalize()

# print(capitalized_name)

# # capitalize მხოლოდ სახელის/ტექსტის პირველ ასოს გაადიდებს და გამოიტანს დიდ ასოდ


# # მომხმარებელს შემოატანინეთ თავისი სახელი და ყველა ასო გარდაქმენით დიდ ასოთ

# name = input("please enter your name: ")

# uppered_name = name.upper()

# print(uppered_name)


# # შექმენით რაიმე ცვლადი დაარქვით sentense და შეინახეთ წინადადება და count მეთოდის გამოყენებით დათვალეთ რაიმე ნებისმიერი ასო

# sentense = "My name is Nika, I am from Georgia"

# print(sentense.count("i"))


# # მომხმარებელს შემოატანინეთ რაიმე სიტყვა დიდი ასოებით და გადააქციეთ პატარა ასოებად

# upper_case = input("plese enter any text in upper case: ")

# print(upper_case.lower())


# # კომენტარებით ახსენით ორივე მეთოდი count & lower

# # count - ითვლის იმ string-ს რასაც ჩვენ ვეტყვით რო დაითვალოს

# # lower - თუ მომხმარებელმა დიდი ასოებით შემოითანა string-ი გადააქცევს პატარა ასოებად


# შექმენით პროგრამა სადაცგამოიყენებთ find & index მეთოდებს. ასევე ახსენით რისთვის გამოიყენება ისინი და რა განსხვავებაა მათ შორის

# sentense = "My name is Nika, I am from Georgia"

# print(sentense.find("i", 9))

# find - ეძებს string-ი მერამდენე index-ზეა

# sentense = "My name is Nika, I am from Georgia"

# print(sentense.index("i", 9))

# index - ეძებს string-ი მერამდენე index-ზეა

# index - find  რა განსხვავებაა?

# find - თუ ეგ stringi არ არის დაგვიბრუნებს -1

# index - თუ ეგ stringi არ არის დაგვიბრუნებს eror


# შექმენითცარიელისია.შემდეგ მომხმარებელს შეეკითხეთ რამდენი იმეილისშემოტანა რურს.
#  იმდენჯერ დაატრიალეთ for ლუპი რამდენი იმეილიც შემოიტანა და ყველა მათგანი შეამოწმეთ არის თუ არას წორი

# emails = []

# email_asker = int(input("რამდენი ემაილის შემოტანა გსურთ?: "))

# for i in range(email_asker):
#    email = input("enter your email: ")

# if email.endswith("@gmail.com"):
#     print("This email is valid.")
#     emails.append(email)

# else:
#     print("Email is not valid!")







