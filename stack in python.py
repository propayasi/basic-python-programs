"""Rajiv has created a dictionary containing employee names and their salaries as
key value pairs of 6 employees.
Write a program, with separate user defined functions to perform the following operations:
Push the keys (employee name) of the dictionary into a stack, where the
corresponding value (salary) is less than 85000.
● Pop and display the content of the stack.
For example:
If the sample content of the dictionary is as follows:
Emp={"Ajay":76000, "Jyothi":150000, "David":89000, "Remya":65000,
"Karthika":90000, "Vijay":82000}
The output from the program should be:
Vijay Remya Ajay"""

def push_to_stack(emp_dict):
    stack = []
    for emp_name, salary in emp_dict.items():
        if salary < 85000:
            stack.append(emp_name)
    return stack

def pop_and_display(stack):
    while stack:
        print(stack.pop(), end=' ')

# sample dictionary
Emp={"Ajay":76000, "Jyothi":150000, "David":89000, "Remya":65000, "Karthika":90000, "Vijay":82000}

# push keys with salary less than 85000 to stack
stack = push_to_stack(Emp)

# pop and display contents of the stack
pop_and_display(stack)
