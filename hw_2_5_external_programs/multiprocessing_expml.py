from multiprocessing import Pool

def f(x,y):
    return x*y

if __name__ == '__main__':
    with Pool(4) as p:
        print(list(map(f, [1,2,3], [2,3,4])))
