#Bonus 
salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years > 5:
    bonus = salary * 0.1
else:
    bonus = salary * 0.05

print("Bonus =", bonus)
print("Net salary=",bonus+salary)