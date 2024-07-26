# num = 0
# while num != 10:
#     print("GOA")
#     num = num + 1

# 0 დან 10 ის ჩათვლით შეკრიბეთ ყველა ლუწი რიცხვი და დაბეჭდეთ ჯამი

# num = 0
# sum = 0
# while num <= 10:
#     sum = sum + num
#     num = num + 2
#     print(sum)
   

# შექმენით პროგრამა რომელსაც ჰქვია guess game, თქვენი დავალებაა, მომხმარებელს იქამდე შემოატანინოთ
# რიცხვი სანამ არ გამოიცნობს რიცხვ 5_ს, როცა გამოიცნობს ტერმინალში დაუბეჭდეთ რომ მან მოიგო
# , სხვა შემთხვევაში დაუბეჭდეთ რომ მან წააგო

num = 0

while num != 5:
    num = int(input("please enter number: "))
    # print("enter number again: ")
    
    if num == 5:
        print("you won")

    else:
        print("you lose, try again")












