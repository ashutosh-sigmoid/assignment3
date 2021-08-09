def hello_decorator(func):


    def inner():
        print("the outer loop")
        func()
        print("the final execution")
    return inner


def function_to_be_used():
    print("this is function_to_be_used")

function_result=hello_decorator(function_to_be_used)
function_result()