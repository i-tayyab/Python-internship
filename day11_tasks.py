from employee import Employee

class EmployeeManager:
    def __init__(self, data_file="employee_data.txt"):
        self.employees = []
        self.data_file = data_file
        self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.data_file, 'r') as f:
                for line in f:
                    self.employees.append(Employee.from_string(line))
        except FileNotFoundError:
            pass  # No data file yet

    def save_to_file(self):
        with open(self.data_file, 'w') as f:
            for emp in self.employees:
                f.write(emp.to_string() + '\n')

    def add_employee(self):
        try:
            name = input("Enter name: ")
            dept = input("Enter department: ")
            salary = float(input("Enter salary: "))
            year = int(input("Enter joining year: "))
            self.employees.append(Employee(name, dept, salary, year))
        except ValueError:
            print("Invalid input.")

    def list_employees(self):
        for emp in self.employees:
            emp.display()

    def search_employee(self, term):
        results = list(filter(
            lambda e: term.lower() in e.name.lower() or term.lower() in e.department.lower(),
            self.employees
        ))
        for emp in results:
            emp.display()

    def sort_by_salary(self, desc=False):
        sorted_list = sorted(self.employees, key=lambda e: e.salary, reverse=desc)
        for emp in sorted_list:
            emp.display()

    def generate_report(self, report_file="employee_report.txt"):
        with open(report_file, 'w') as f:
            f.write("Employee Summary Report\n")
            f.write(f"Total Employees: {len(self.employees)}\n")
            if self.employees:
                highest_paid = max(self.employees, key=lambda e: e.salary)
                f.write(f"Highest Salary: {highest_paid.salary} ({highest_paid.name})\n")
                avg_salary = sum(e.salary for e in self.employees) / len(self.employees)
                f.write(f"Average Salary: {avg_salary:.2f}\n")
