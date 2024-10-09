def get_employee_data():
    employees = []
    num_employees = int(input("Enter the number of employees: "))
    for _ in range(num_employees):
        name = input("Enter employee name: ")
        attendance = []
        for month in range(1, 13):
            days_present = int(input(f"Enter days present in month {month} for {name}: "))
            attendance.append(days_present)
        employees.append({'name': name, 'attendance': attendance})
    return employees
