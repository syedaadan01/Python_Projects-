def calculate_total_attendance(employees):
    for employee in employees:
        employee['total_attendance'] = sum(employee['attendance'])

def calculate_monthly_attendance(employees):
    monthly_attendance = [0] * 12
    for employee in employees:
        for month in range(12):
            monthly_attendance[month] += employee['attendance'][month]
    return monthly_attendance
