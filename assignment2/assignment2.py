import csv
import traceback
import os
import custom_module
from datetime import datetime
def read_employees():
    empty_dict={}
    empty_rows=[]
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            first=True
            for row in reader:
                if first:
                    empty_dict["fields"]=row
                    first=False
                else:
                    empty_rows.append(row)
            empty_dict["rows"]=empty_rows
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
    return empty_dict
employees=read_employees()
print(employees)

def column_index(input_str):
    return employees["fields"].index(input_str)

employee_id_column=column_index("employee_id")


def first_name(rownum):
    first_name_column=column_index("first_name")
    chosenrow=employees["rows"][rownum]
    return chosenrow[first_name_column]

employedd_first_name=first_name(10)

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

def sort_by_last_name():
    last_name_col_index=column_index("last_name")
    employees["rows"].sort(key=lambda x:x[last_name_col_index])
    print(employees)
    return employees["rows"]

class DynamicObject:
    def __init__(self):
        pass

def employee_dict(row):
    employee_data = {}

    for ix,key in enumerate(employees["fields"]):
        if key=="employee_id":
            continue
        employee_data[key] = row[ix]
    return employee_data

print(employee_dict(employees["rows"][0]))

def all_employees_dict():
    employee_data = {}

    for i,r in enumerate(employees["rows"]):
        employee_data[str(r[0])] = employee_dict(employees["rows"][i])
    print(employee_data)
    return employee_data

print(all_employees_dict())

def get_this_value():
    return os.getenv("THISVALUE")

def set_that_secret(secret):
    custom_module.set_secret(secret)

print(set_that_secret("THATVALUE"))

def read_minutes():
    minutes1={'fields': [], 'rows': []}
    minutes2={'fields': [], 'rows': []}
    try:
        with open("../csv/minutes1.csv", mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            minutes1['fields'] = next(reader)
            for row in reader:
                minutes1['rows'].append(tuple(row))
            
        with open("../csv/minutes2.csv", mode='r', newline='', encoding='utf-8') as file2:
            reader2 = csv.reader(file2)
            minutes2['fields'] = next(reader2)
            for row in reader2:
                minutes2['rows'].append(tuple(row))
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

    return  minutes1, minutes2

minutes1, minutes2 = read_minutes()

def create_minutes_set():
    global minutes1, minutes2

    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])

    combined_set = set1.union(set2)

    return combined_set

minutes_set=create_minutes_set()

def create_minutes_list():
    global minutes_set

    min_list = list(minutes_set)

    format_string = "%B %d, %Y"
    
    transformed_list = list(map(
        lambda x: (x[0], datetime.strptime(x[1], format_string)), 
        min_list
    ))

    return transformed_list

minutes_list=create_minutes_list()
print(minutes_list)

def write_sorted_list():
    global minutes_list, minutes1

    minutes_list.sort(key=lambda x: x[1])

    transformed_list_for_csv = list(map(
        lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),
        minutes_list
    ))
    
    try:
        with open('./minutes.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            writer.writerow(minutes1["fields"]) 
            
            writer.writerows(transformed_list_for_csv)

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

    # The function should return the converted list
    return transformed_list_for_csv
