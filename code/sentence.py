#import cv2
import argparse
#from contextlib import contextmanager

# parse argument
def parse_opt(known=False,**kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--name',type=str,default=kwargs['name'],help='your name')
    parser.add_argument('--password', type=int, default=kwargs['passw'], help='your password')
    parser.add_argument('--isAdmin',action='store_true', help='Are you admin or not', default=False)
    opt = parser.parse_known_args()[0] if known else parser.parse_args()
    return opt

# 1 equal if
def eqif(x):
    a = x if x> 10 else 0
    return a

#2  if in
def ifin(x):
    if x in range(0,10):
        return x
    else:
        return -1

#3  equal for
def eqfor(x):
    a = [i for i in range(x) if i >0]
    return a

#4  for in
def forin(x):
    for a,b,c in x:
        print(a,b,c)

#5  with as : generally operating files and !! @contextmanager
def wias():
    with open("test.txt",'r',encoding='utf-8') as f:
        #print(f.read())
        for line in f.readlines(): print(line)
        if f : f.close()

#6  print str
def prts(x):
    for a,b,c,d,e,f in x:
        print(('\n' + '%10s' *6) % (a,b,c,d,e,f))

#7  lambda
def lambdpr(n,foo):
    #1
    return list(filter(lambda x: x % 3 == 0, foo)) if n==1 else list(map(lambda x: x * 2 + 10, foo))
    #2
    #return [x for x in foo if x % 3 == 0] if n==1 else reduce(lambda x, y: x + y, foo)
    #3
    # g = lambda x: x + 1
    # print(g(1))

if __name__ == '__main__':

    #4
    a = [(1,2,1),(2,3,1),(3,4,1)]
    #5
    #wias()
    #6
    b = [('a','b','c','d','e','f'),('a','b','c','d','e','f')]
    #7
    #print(lambdpr(2,[1,2,3,4,5]))

    #1
    #opt = parse_opt()
    #or
    #opt = parse_opt(True,name='sito',passw=123)
    #print(('\n' + '%10s' * 3) % (opt.name, opt.password, opt.isAdmin))
	print('My play program running succesfully')

