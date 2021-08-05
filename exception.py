day=32
try:
    if day>31:
        raise ValueError('invalid day number')
except ValueError as msg:
        print('the program found an',msg)
finally:
            print('exception handled')
