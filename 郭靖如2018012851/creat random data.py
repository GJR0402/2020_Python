"""
Author:Guojr
Purpose:random data
Time:1/5/2020
"""
import random
import string

def dataSampling(datatype,datarange,num,strlen=6):
    result = set()
    for index in range(0,num):
        if datatype is float:
            it = iter(datarange)
            item=random.uniform(next(it),next(it))
            result.add(item)
            continue
        elif datatype is int:
            it = iter(datarange)
            item = random.randint(next(it), next(it))
            result.add(item)
            continue
        elif datatype is str:
            item=''.join(random.SystemRandom().choice(datarange)for _ in range(3))
            result.add(item)
        else:
            continue
    return result
def dataScreeing():
    pass
def apply():
    result1=dataSampling(int,[1,100],100)
    print(result1)
    result2=dataSampling(float,[1,100],50)
    print(result2)
    result3=dataSampling(str,"abcdefg",5)
    print(result3)
apply()