hours= float(input("Enter Hours: "))
rate= float(input("Enter Rate: "))
pay = hours*rate
print("Regular Pay: ",pay)
ot= float(hours-40)
otr= float(rate*0.5)
otrate= float(otr+rate)
otpay= float(ot*otr)
if (ot>0):  
    print("Overtime Hours: ", ot)
    print("Overtime Rate: ", otrate)
    print("Overtime Pay: ", otpay)
    print("Total Pay: ",otpay+pay)
elif (ot<0):
    print("Overtime Hours: 0")
    print("Overtime Pay: 0")
    print("Total Pay: ", pay)


