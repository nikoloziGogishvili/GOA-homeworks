# 2) გაკვეთილზე განხილული შედარების ოპერატორებიდან (>, <, ==, >=, <=, !=)
#  თითოეულზე ჩამოწერეთ 5-5 მაგალითი

# შევქმენი ცვლადები
num1 = 1
num2 = 2 
num3 = 3
num4 = 4
num5 = 5
# Greater than >
 # True 
print(num2 > num1)
print(num3 > num2)
print(num3 > num1)
print(num5 > num4)
print(num4 > num3)
 # False 
print(num1 > num1)
print(num1 > num5)
print(num2 > num3)
print(num4 > num5)
print(num3 > num4)
# Less than <
 # True 
print(num1 < num2)
print(num4 < num5)
print(num2 < num3)
print(num3 < num4)
print(num1 < num5)
 # False
print(num2 < num1)
print(num5 < num1)
print(num4 < num3)
print(num3 < num2)
print(num1 < num1)
# Equal ==
 # True
print(num1 == num1)
print(num2 == num2)
print(num3 == num3)
print(num4 == num4)
print(num5 == num5)
 # False
print(num5 == num1)
print(num4 == num2)
print(num3 == num5)
print(num2 == num1)
print(num4 == num2)
# Greater than or Equal >=
 # True
print(num2 >= num1)
print(num3 >= num2)
print(num4 >= num4)
print(num5 >= num5)
print(num3 >= num2)
 # False
print(num1 >= num5)
print(num4 >= num5)
print(num3 >= num4)
print(num2 >= num3)
print(num1 >= num2)
# Less than or Equal <=
 # True
print(num5 <= num5)
print(num1 <= num2)
print(num3 <= num4)
print(num4 <= num5)
print(num1 <= num1)
 # False
print(num5 <= num1)
print(num4 <= num3)
print(num3 <= num2)
print(num2 <= num2)
print(num4 <= num1)
# Don't Equal !=
 # True
print(num1 != num1)
print(num2 != num2)
print(num3 != num3)
print(num4 != num4)
print(num5 != num5)
 # False
print(num1 != num2)
print(num3 != num4)
print(num5 != num1)
print(num2 != num3)
print(num4 != num1)


# 3) ჩამოწერეთ 10-10 მაგალითი and და or ოპერატორებზე

# და - and
 # True
print(num1 < num2 and num2 != num3)
print(num3 < num4 and num5 > num4)
print(num2 > num1 and num2 < num4)
print(num1 == num1 and num5 == num5)
print(num4 > num1 and num2 == num2)
print(num3 <= num5 and num2 >= num2)
print(num1 != num2 and num5 >= num3)
print(num2 >= num1 and num3 >= num2)
print(num4 == num4 and num2 <= num5)
print(num5 != num1 and num1 != num5)
 # False
print(num1 == num4 and num5 < num1)
print(num2 != num3 and num3 != num3)
print(num5 != num4 and num3 < num1)
print(num1 <= num3 and num4 >= num5)
print(num1 == num3 and num5 != num4)
print(num3 < num2 and num4 > num5)
print(num5 == num3 and num1 > num3)
print(num2 != num2 and num3 <= num3)
print(num4 >= num4 and num2 != num2)
print(num3 > num3 and num1 == num5)
# ან - or
 # True
print(num1 > num2 or num3 == num3)
print(num5 != num1 or num3 >= num3)
print(num4 < num5 or num1 == num1)
print(num3 != num3 or num1 <= num3)
print(num4 > num1 or num5 == num2)
print(num4 >= num3 or num1 == num3)
print(num5 != num3 or num1 < num1)
print(num3 > num2 or num1 == num1)
print(num5 >= num5 or num2 < num1)
print(num4 == num1 or num3 != num2)
 # False
print(num2 == num3 or num1 > num5)
print(num2 != num2 or num1 >= num4)
print(num5 <= num2 or num1 >= num3)
print(num4 == num3 or num1 != num1)
print(num2 <= num1 or num3 < num3)
print(num2 == num1 or num5 != num5)
print(num3 <= num2 or num1 > num5)
print(num1 == num3 or num3 == num1)
print(num5 != num5 or num1 > num2)
print(num3 < num2 or num4 == num5)



