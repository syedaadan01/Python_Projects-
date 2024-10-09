from employee_input import get_employee_data
from attendance_calculations import calculate_total_attendance, calculate_monthly_attendance
from display_results import display_results

def main():
    employees = get_employee_data()
    calculate_total_attendance(employees)
    monthly_attendance = calculate_monthly_attendance(employees)
    display_results(employees, monthly_attendance)

if __name__ == "__main__":
    main()
