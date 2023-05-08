#Author: Pranav Shirali
#Description: Python program to find the best of two test average marks out of the three test's marks accepted from the user

marks_1 = float(input("Enter the marks for first subject: "))
marks_2 = float(input("Enter the marks for second subject: "))
marks_3 = float(input("Enter the marks for third subject: "))

average_1 = (marks_1 + marks_2) / 2
average_2 = (marks_1 + marks_3) / 2
average_3 = (marks_2 + marks_3) / 2

if average_1 > average_2 and average_1 > average_3:
    print(f"Marks {marks_1} and {marks_2} are highest and average is {average_1}.")
elif average_2 > average_1 and average_2 > average_3:
    print(f"Marks {marks_1} and {marks_3} are highes and average is {average_2}")
else:
    print(f"Marks {marks_2} and {marks_3} are highest and average is {average_3}")