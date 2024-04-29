
def prime_checker(number):
    count = 0
    for i in range(2, number):
        if number % i == 0:
            count += 1
    
    if count == 0:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
    

n = int(input()) # Check this number
prime_checker(number=n)