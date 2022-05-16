import concurrent.futures
import random
from time import perf_counter

background = {
    1 : "badle1",
    2 : "badle2",
    3 : "badle3",
    4 : "sport1",  
}

l = list(background.keys())

proba = [1 , 1 , 1 , 1]
x = random.choices(l , proba)
print(x)

body = {
    1 : "body1",
    2 : "body2",
    3 : "body3"
}

l = list(body.keys())
proba = [1 , 1 , 1]
x = random.choices(l , proba)
print(x)

glasses = {
    1 : "badle1glass1",
    2 : "badle1glass2",
    3 : "badle2glass1",
    4 : "badle2glass2",
    5 : "sport1glass1"
}

l = list(glasses.keys())
proba = [1 , 1 , 1 , 1 , 1]
x = random.choices(l , proba)
print(x)
mouth = {
    1 : "mouth1",
    2 : "mouth2",
    3 : "mouth3"
}
l = list(mouth.keys())
proba = [1 , 1 , 1]
x = random.choices(l , proba)
print(x)
accessory = {
    0 : '',
    1 : "badle1acccessory1",
    2 : "badle2accesssory1",
    3 : "sport1accessory1"
}

l = list(accessory.keys())
proba = [1 , 1 , 1 , 1]
x = random.choices(l , proba)
print(x)
def getData():
    back , bd, e , m , acce = [] , [] , [] , [] , []

    for i in background:
        back.append(background[i])
    for j in body:
        bd.append(body[j])
    for h in glasses:
        e.append(glasses[h])
    for a in mouth:
        m.append(mouth[a])
    for x in accessory:
        acce.append(accessory[x])
    
    return back , bd , e , m , acce

def randomChoice():
    nft = []
    for i in getData()[0]:
        for j in getData()[1]:
            for k in getData()[2]:
                for l in getData()[3]:
                    for m in getData()[4]:
                        if "badle1" in i and "badle1" in k and ("badle1" in m or len(m) == 0):
                            nft.extend([[i , j , k , l , m]])
                        if "badle2" in i and "badle2" in k and ("badle2" in m or len(m) == 0):
                            nft.extend([[i , j , k , l , m]])
                        if "badle3" in i and "badle3" in k and ("badle3" in m or len(m) == 0):
                            nft.extend([[i , j , k , l , m]])
                        if "sport1" in i and "sport1" in k and ("sport1" in m or len(m) == 0):
                            nft.extend([[i , j , k , l , m]])
                            
    l = [i for i in range(len(nft))]
    dictionary =  dict(zip(l , nft))
    
    
    group1 , group2 , group3 , group4 , group5 = [] , [] , [] , [] , []
    for i in range(len(dictionary)):
        if i < 10:
            group1.append(i)
        if i >= 10 and i < 20:
            group2.append(i)
        if i >= 20 and i < 30:
            group3.append(i)
        if i >= 30 and i < 40:
            group4.append(i)
        if i >= 40 and i < 50:
            group5.append(i)
    return group1 , group2
start = perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(randomChoice)
    result = future.result()
