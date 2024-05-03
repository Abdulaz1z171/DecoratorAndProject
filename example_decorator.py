import time

# vaqtni xisoblaydigan decorator yaraatamiz
def calculate_time(func):
    def wrapper(*args,**kwargs):
        begin = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(f'Total time take in : {end - begin}')
    return wrapper




# fibonacci sonlarini hisoblaydigan funksiya yaratamiz
@calculate_time
def fibonacci(n:int):
    prev_number = 0
    current_number = 1
    count = 1
    while count <= n:
        next_number = prev_number + current_number
        current_number = prev_number
        prev_number = next_number
        count += 1
        print(prev_number)


fibonacci(5)
