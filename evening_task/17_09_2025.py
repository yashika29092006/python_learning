# # print vowels or not using match case
# v = input("enter the vowel :")
# match v:
#     case 'a'|'A'|'e'|'E'|'i'|'I'|'o'|'O'|'u'|'U':
#         print("VOWELS")
#     case _:
#         print("Constant")



# # age problem
# age=int(input("enter your age"))
# if age >0 and age <5:
#     print("FREE")
# elif age >= 5 and age <=12:
#     print("10")
# elif age >=13 and age <= 64:
#     print("20")
# elif age >=65:
#     print("15")
# else:
#     print("invalid")


# # print month using match case
# monthNumber=int(input("enter the number between (1-12) : "))
# match monthNumber:
#     case 1:
#         print("January")
#     case 2:
#         print("February")
#     case 3:
#         print("March")
#     case 4:
#         print("April")
#     case 5:
#         print("may")
#     case 6:
#         print("June")
#     case 7:
#         print("July")
#     case 8:
#         print("August")
#     case 9:
#         print("September")
#     case 10:
#         print("october")
#     case 11:
#         print("November")
#     case 12:
#         print("December")
#     case _:
#         print("Invalid")

def num(n):
    n // 5
    print(n)
    n % 5
    print(n)
num(23)