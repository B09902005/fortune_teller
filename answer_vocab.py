import random
myfile = open('vocabulary.txt')
english = []
chinese = []
while (True):
    a = myfile.readline()
    if (a == ''):
        break
    if (a[0] in {'a','b','c','d','e','f','g','h','i','j','k','l','m',
                     'n','o','p','q','r','s','t','u','v','w','x','y','z'}):
        english.append(a.split(' ')[0])
        chinese.append('')
        while (a != '\n'):
            a = myfile.readline()
            chinese[-1] = chinese[-1] + a[0:-1]
length = len(english)
print('我是程式算命師。問我一個問題(如：我今天運勢如何？)，我可以用一個英文單字來回答你。')
for i in range (10):
    a = input()
    num = random.randint(0,length-1)
    print(english[num])
    print(chinese[num])
    print()
