# program to check both the numbers are greater than 35 or A is greater than B

A = int(input())
B = int(input()) 

both_greater_than_35 = A > 35 and B > 35 
A_greater_than_B = A > B 

condition = both_greater_than_35 or A_greater_than_B 
print(condition)

# program to check if one of the numbers is negative and sum is greater than 7 

A = int(input())
B = int(input())

negative_num = A < 0 or B < 0 
sum_of_nums_greater_than_7 = A + B > 7 

condition = negative_num and sum_of_nums_greater_than_7 
print(condition)

# program to check if both are positive numbers or both A and B are less than 70

A = int(input())
B = int(input()) 

positive_nums = A > 0 and B > 0 
less_than_70 = A < 70 and B < 70 

condition = positive_nums or less_than_70 
print(condition)

# program to check if one of the numbers is less than 60 and greater than 80

A = int(input())
B = int(input()) 

less_than_60 = A < 60 or B < 60 
greater_than_80 = A > 80 or B > 80 

condition = less_than_60 and greater_than_80 
print(condition)
