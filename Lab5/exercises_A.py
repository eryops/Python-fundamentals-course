course_name = 'Python fundamentals'

def return_course_name():
    course_name = 'PHP fundamentals'
    return course_name

def counter_function():
    counter = 0
    while counter < 5:
        counter += 1
    return counter

counting = 10   # global variable
# def increase():
#     counting = counting + 1   # trying to change global value, will fail
#     print(counting)


def increase(value):
    value = value + 1
    return value


def outer():
    count = 5

    def inner():
        count = 10
        print('inner counter: ', count) 
    inner() # will print 10
    print('outer counter: ', count) # will print 5


# Example on how to avoid shadowing build ins
# number_list instead of list
# string instead of str
# max_value instead of max


# --- Main like section ---
print(course_name) # will print the global variable that is set outside the function because we don´t have access to the scoped variable outside of the function
print(return_course_name()) # will print the scoped variable in side the function and not the global one outside the function

#print(counter) # not available because it is inside of the scope of a function
print(counter_function())

counting = increase(counting)
print(counting)

outer()