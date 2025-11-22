pyspace = globals()


class sdf_SL:
    def __init__(self):
        self.space = {}
        for i in pyspace.keys():
            if i == 'pyspace':
                continue
            else:
                self.space[i] = pyspace[i]
    def addopt(self,name:str,value):
        self.space[name] = value
    def do(self,str):
        exec(str,self.space)
'''
def a():
    x = [1,1]
    for i in range(9):
        x.append(x[-2]+x[-1])
    print(x)
def b():
    x = [0,1,1]
    y = [9,1,5]
    for i in range(len(x)):
        y[i]+=x[i]
    print(y)


sl = sdf_SL()
sl.addopt('a',a)
sl.addopt('b',b)
sl.do("a();b()")
'''