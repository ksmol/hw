def decorator(func):
    def wrapper(*kwargs):
        for i in range(3):
            func(*kwargs)
    return wrapper

@decorator
def sing(line):
    print(line)

sing('tgsfg')