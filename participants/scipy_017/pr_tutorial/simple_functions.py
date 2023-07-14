def fibonacci(max):
    values = [0, 1]
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values


def factorial(value):
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)

def is_prime(value):
    if value == 1:
        print(value, "is not a prime number")
    elif value > 1:
    # check for factors
        for i in range(2,value):
            if (value % i) == 0:
                break
            else:
                print(value,"is a prime number")
        
    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(value,"is not a prime number")
