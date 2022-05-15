# Functions

def add_numbers(a, b):
    sum = a+b
    print('Doing math')
    return sum


def greet_person(person):
    return f"Hello there , {person}"


def divide(a, b):
    if type(a) is int and type(b) is int:
        return a/b
    # this return is a or b are not int (numbers )
    return 'a and b must be intergers'


# Functions arguments

# the functions need 3 arguments if not will give error
def three_things(a, b, c):
    print('3 arguments')

# """ this creates a multilane


def send_email(to_email, from_email, subject, body):
    email = f"""
       to:{to_email}
       from:{from_email}
       subject:{subject}
       -----------------
       body:{body}
    """
    print(email)


# we can set the arguments withaout doing the exact order
send_email(subject='love', to_email='yaki@algo',
           from_email='denny@alog', body='i love you')
