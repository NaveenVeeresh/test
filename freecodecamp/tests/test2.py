class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, position, salary):
        """Add a new employee to the system"""
        employee = {
            'id': emp_id,
            'name': name,
            'position': position,
            'salary': salary
        }
        self.employees.append(employee)
        print(f"Employee {name} added successfully!")

    def update_employee(self, emp_id, **kwargs):
        """Update employee details"""
        for employee in self.employees:
            if employee['id'] == emp_id:
                for key, value in kwargs.items():
                    if key in employee:
                        employee[key] = value
                print(f"Employee ID {emp_id} updated successfully!")
                return
        print(f"Employee ID {emp_id} not found!")

    def delete_employee(self, emp_id):
        """Remove an employee from the system"""
        for i, employee in enumerate(self.employees):
            if employee['id'] == emp_id:
                del self.employees[i]
                print(f"Employee ID {emp_id} deleted successfully!")
                return
        print(f"Employee ID {emp_id} not found!")

    def display_employees(self):
        """Show all employees using a for loop"""
        if not self.employees:
            print("No employees in the system!")
            return

        print("\nCurrent Employees:")
        print("-" * 40)
        for employee in self.employees:
            print(f"ID: {employee['id']}")
            print(f"Name: {employee['name']}")
            print(f"Position: {employee['position']}")
            print(f"Salary: ${employee['salary']}")
            print("-" * 40)

    def get_employee_count(self):
        """Return the total number of employees"""
        return len(self.employees)


# Example usage
if __name__ == "__main__":
    manager = EmployeeManager()

    # Add employees
    manager.add_employee(101, "John Doe", "Developer", 75000)
    manager.add_employee(102, "Jane Smith", "Manager", 90000)
    manager.add_employee(103, "Bob Johnson", "Designer", 65000)

    # Display all employees
    manager.display_employees()

    # Update an employee
    manager.update_employee(101, position="Senior Developer", salary=85000)

    # Delete an employee
    manager.delete_employee(103)

    # Display an updated list
    print("\nAfter updates:")
    manager.display_employees()

    # Show total count
    print(f"\nTotal employees: {manager.get_employee_count()}")
