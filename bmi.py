#classify and report the risk of developing disease to the user
weight=float(input("Enter your weight(kg):"))
height=float(input("Enter your height(m):"))
# calculate Body Mass Index
BMI=weight/(height*height)
#Compare values

if BMI <18.5:
    print("Your BMI is:",BMI,"you are underweight and the risk of developing disease is low")
elif BMI<24.9:
    print("Your BMI is:",BMI,"you are normal and the risk of developing disease is normal")
elif BMI<29.9:
    print("Your BMI is:",BMI,"you are little overweight and the risk of developing disease is high")
elif BMI<35.0:
    print("Your BMI is:",BMI,"you are obesity grade 1 and the risk of developing disease is high")
elif BMI<39.9:
    print("Your BMI is:",BMI,"you are obesity grade 2 and the risk of developing disease is very high")
elif BMI>40:
    print("Your BMI is:",BMI,"you are obesity grade 3 and the risk of developing disease is dangerous")
