overtime=100000
child=int(input("Enter child:"))
insurance=int(input("Enter insurance:"))
basic_salary=int(input("Enter basic_salary:"))
overtime_hours=int(input("Enter overtime_hours:"))
if child>=3:
    child_benefit=150000
elif child<3:
    child_benefit=50000*child
Total_wages=basic_salary + (overtime_hours * overtime) +child_benefit - insurance
print(Total_wages)
