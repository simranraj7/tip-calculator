#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill=float(input("What is the total bill: Rs."))
tip=int(input("How much tip would you like to give? : "))
number_people=int(input("How many people to split the bill?: "))

total_tip= (tip/100) + 1


split_money= (bill/number_people)*total_tip
final_amount=round(split_money,2)
final_amount="{:.2f}".format(split_money)
print("Each person should pay:Rs.",final_amount)





