# # # # # # # # n1 = int(input("Enter first number: "))
# # # # # # # # n2 = int(input("Enter second number: "))
# # # # # # # # n3 = int(input("Enter third number: "))
# # # # # # # # n4 = int(input("Enter fourth number: "))

# # # # # # # # if(n1 > n2) and (n1 > n3) and (n1 > n4):
# # # # # # # #     largest = n1
# # # # # # # # elif(n2 > n1) and (n2 > n3) and (n2 > n4):
# # # # # # # #     largest = n2
# # # # # # # # elif(n3 > n1) and (n3 > n2) and (n3 > n4):
# # # # # # # #     largest = n3
# # # # # # # # else:
# # # # # # # #     largest = n4

# # # # # # # # print("The largest number is:", largest) 

# # # # # # # mark1 = int(input("Enter marks of subject 1: "))
# # # # # # # if(mark1 >= 33):
# # # # # # #     print("You have passed in subject 1")
# # # # # # # else:
# # # # # # #     print("You have failed in subject 1")
# # # # # # # mark2 = int(input("Enter marks of subject 2: "))
# # # # # # # if(mark2 >= 33):
# # # # # # #     print("You have passed in subject 2")
# # # # # # # else:
# # # # # # #     print("You have failed in subject 2")
# # # # # # # mark3 = int(input("Enter marks of subject 3: "))
# # # # # # # if(mark3 >= 33):
# # # # # # #     print("You have passed in subject 3")
# # # # # # # else:
# # # # # # #     print("You have failed in subject 3")

# # # # # # # total = (mark1 + mark2 + mark3)/3
# # # # # # # if(total >= 40 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33):
# # # # # # #     print("You have passed the exam")
# # # # # # # else:
# # # # # # #     print("Unfortunately, you haven't passed the exam")
# # # # # # text = input("Enter the comment: ")
# # # # # # if("Make a lot of money" in text):
# # # # # #     spam = True
# # # # # # elif("Buy now" in text):
# # # # # #     spam = True
# # # # # # elif("Subscribe this" in text):
# # # # # #     spam = True
# # # # # # elif("Click this" in text):
# # # # # #     spam = True
# # # # # # else:
# # # # # #     spam = False
# # # # # # if(spam):
# # # # # #     print("This is a spam message")
# # # # # # else:
# # # # # #     print("This is not a spam message")

# # # # # user_name = input("Enter your username: ")
# # # # # length = len(user_name)
# # # # # if(length < 10):
# # # # #     print("Username contains less than 10 characters")
# # # # # else:
# # # # #     print("Username does not contain less than 10 characters")

# # # # list_ = ["Fizaan", "Ali", "Areeb", "Usama", "Ahmed", "Hassan", "Hussain"]
# # # # name = input("Enter the name: ")

# # # # if name in list_:
# # # #     print("Your name is present in the list")
# # # # else:
# # # #     print("Your name is not present in the list")

# # # marks = int(input("Enter the marks: "))

# # # if(marks > 90) and (marks <= 100):
# # #     print("Grade: Ex")
# # # elif(marks > 80) and (marks <= 90):
# # #     print("Grade: A")
# # # elif(marks > 70) and (marks <= 80):
# # #     print("Grade: B") 
# # # elif(marks > 60) and (marks <= 70):
# # #     print("Grade: C")
# # # elif(marks >= 50) and (marks <= 60):
# # #     print("Grade: D")
# # # else:
# # #     print("Grade: F")
# # marks1 = int(input("Enter marks for subject 1: "))
# # marks2 = int(input("Enter marks for subject 2: "))
# # marks3 = int(input("Enter marks for subject 3: "))

# # total_percentage = (100)*(marks1+marks2+marks3)/300

# # if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
# #     print("You have passed the examination with total percentage of: ", total_percentage)
# # else:
# #     print("You have failed the examination with total perentage of: ", total_percentage)


# marks = int(input("Enter the marks: "))
# if(marks>=40):
#     print("You have passed the exam.")
# else:
#     print("You haven't passed the exam.")
