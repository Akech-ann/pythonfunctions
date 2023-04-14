def hello(*name):
    for nam in name:
        print(f"hello {nam}")


def sum(*numbers):
    answer = 0
    for number in numbers:
        answer+=number
    return answer  


#write a function that 
def k (*numbers):
    answer = 1
    for number in numbers:
        answer*=number
    return answer         


def student_attributes(**num):
    for key,value in num.items():
        print(f"{key}:{value}")

def my_country(country="South Sudan"):
    print(f"Hello from {country}")   

    # A function named concatenate_args that takes any number of string
    #  arguments in positional arguments format and 
    # concatenates them into a single string  
def concatenate_args(*peoples):
    result = ""
    for people in peoples:
        result+=people
    return result


# A function named concatenate_kwargs that takes any number
#  of string arguments in keyword arguments  format and concatenates 
# them into a single string
def concatenate_kwargs(**word):
    answer=(" ")
    for key,value in word.items():
        answer+=(f"{key,value}")
    return answer



