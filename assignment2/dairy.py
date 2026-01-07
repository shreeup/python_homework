import traceback
try:
    with open('dairy.txt', 'r') as file:
        content = file.read()  # Read entire file
        print(content)

    first=True
    with open('dairy.txt', 'a', newline='') as file:
        while True:
            mesage="What else?"
            if first:
                mesage="What happened today?"
                first=False
            user_input = input(mesage)
            file.write(f"{user_input} \n")
            if user_input=="done for now":
                break
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

