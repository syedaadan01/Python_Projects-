def display_results(employees, monthly_attendance):
    print("\nEmployee Attendance Summary:")
    for employee in employees:
        print(f"{employee['name']} - Total Attendance: {employee['total_attendance']} days")
    
    print("\nMonthly Attendance Summary:")
    for month, total in enumerate(monthly_attendance, start=1):
        print(f"Month {month}: {total} days")
