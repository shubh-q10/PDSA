class employee:
    def putdata(self):
        self.id = int(input("enter the employee id"))
        self.name = input("enter the employee name")
        self.salary = float(input("enter the employee salary"))
    def display(self):
        print("employee_id:", self.id )
        print("employee_name:", self.name)
        print("employee_salary", self.salary)
        

a = employee()
a.putdata()
a.display()

b = employee()
b.putdata()
b.display()

c = employee()