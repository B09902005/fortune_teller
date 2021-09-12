import random

def correct(num,a,noun,verb,adj,adv):
    if (num == 9999):
        return False
    if (a == '1'):
        return noun[num]
    if (a == '2'):
        return verb[num]
    if (a == '3'):
        return adj[num]
    if (a == '4'):
        return adv[num]
    return True

myfile = open('vocabulary.txt')
(english,chinese) = ([],[])
(noun,verb,adj,adv) = ([],[],[],[])
while (True):
    a = myfile.readline()
    if (a == ''):
        break
    if (a[0] in {'a','b','c','d','e','f','g','h','i','j','k','l','m',
                     'n','o','p','q','r','s','t','u','v','w','x','y','z'}):
        english.append(a.split(' ')[0])
        noun.append(a.find('n.') != -1)
        verb.append(a.find('v.') != -1)
        adj.append(a.find('adj.') != -1)
        adv.append(a.find('adv.') != -1)
        chinese.append('')
        while (a != '\n'):
            a = myfile.readline()
            chinese[-1] = chinese[-1] + a[0:-1]
            
length = len(english)
a = input('我是程式算命師。問我一個問題(如：我今天運勢如何？)，我可以用一個英文單字來回答你。(按enter以繼續)')
for i in range (10):
    a = input('請輸入指定詞性？名詞輸入1，動詞輸入2，形容詞輸入3，副詞輸入4，不限詞性輸入0。')
    b = input('請輸入你的問題？')
    num = 9999
    while (correct(num,a,noun,verb,adj,adv) == False):
        num = random.randint(0,length-1)
    print(english[num], chinese[num])
    print()
