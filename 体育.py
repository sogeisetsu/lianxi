from random import random
def printready():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的值(以0到1之间的小数表示)")
def getpower():
    print("请输入A的能力值:",end='')
    A=eval(input(""))
    print("请输入B的能力值:",end='')
    B=eval(input(""))
    print("比赛次数",end='')
    n=eval(input(""))
    return A,B,n
def gameover(a,b):
    return a==15 or b==15
def oneresult(A,B):
    scorea,scoreb = 0,0
    s="a"
    while not gameover(scorea,scoreb):
        if s=="a":
            if random() < A:
                scorea +=1
            else:
                s="b"
        else:
            if random() < B:
                scoreb +=1
            else:
                s="a"
    return scorea,scoreb
def nresult(A,B,n):
    wisha,wishb = 0,0
    for i in range(n):
        scorea,scoreb = oneresult(A,B)
        if scorea > scoreb:
            wisha +=1
        else:
            wishb +=1
    return wisha,wishb
def printresult(wisha,wishb):
    n = wisha+wishb
    print("A赢了{}场,赢率是{:0.1%}".format(wisha,wisha/n))
    print("B赢了{}场,赢率是{:0.1%}".format(wishb,wishb/n))
def main():
    printready()
    A,B,n=getpower()
    wisha,wishb = nresult(A,B,n)
    printresult(wisha,wishb)
main()
