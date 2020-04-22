#Jorge Castro
#Assignment: TIP calculator
#Onemomth.com


#Assigment of variable to store the user input



bill_amount = float(input("Please enter your restaurant bill amount: ").strip("$"))


#Variables to store the result of the operations and calculate tips
total_tip15 = bill_amount * 0.15
total_tip18 = bill_amount * 0.18
total_tip20 = bill_amount * 0.20

#Variable to store the total to pay
total_to_pay_15 = bill_amount + total_tip15
total_to_pay_18 = bill_amount + total_tip18
total_to_pay_20 = bill_amount + total_tip20

#To make the result more readeble, multiple line on strings using """ """

print(f"""

 This are the sugested Tip amouns and the totals to pay:

 The Tip at 15% would be ${total_tip15:.2f} and the total to pay would be ${total_to_pay_15:.2f}

 The Tip at 18% would be ${total_tip18:.2f} and the total to pay would be ${total_to_pay_18:.2f} 

 The Tip at 20% would be ${total_tip20:.2f} and the total to pay would be ${total_to_pay_20:.2f}

 """)




