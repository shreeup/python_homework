import csv
import traceback
def read_employees():
    employeesrecords=[]
    try:
        with open('./csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            first=True
            for row in reader:
                if first:
                    first=False
                else:
                    employeesrecords.append(row)
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    return employeesrecords
employees=read_employees()
print(employees)
names=[emp[1] for emp in employees]
print(f"names: {names}")
fullnames=[emp[1]+' '+emp[2] for emp in employees]
print(f"full names: {fullnames}")

filtered_list = [word for word in names if 'e' in word.lower()]

print(f"filtered list: {filtered_list}")