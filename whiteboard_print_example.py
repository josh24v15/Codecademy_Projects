def num_print(nmbr):
    for i in range(nmbr):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    

num_print(9)
num_print(20)
num_print(45)