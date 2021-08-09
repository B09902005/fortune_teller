import random
myfile = open('code.txt')
chinese = [0 for i in range (10000)]
while (True):
    a = myfile.readline().split(',')
    if (a[0] != '') and (a[0][0] in {'0','1','2','3','4','5','6','7','8','9'}):
        chinese[int(a[0])] = a[1]
        if (int(a[0]) == 9999):
            break
length = len(chinese)
print('我是程式算命師。問我一個問題(如：我今天運勢如何？)，我可以用中文字來回答你。')
question = [0 for i in range (10)]
for i in range (10):
    question[i] = input()
    num = random.randint(0,length-1)
    print('電碼%04s  ' % num, chinese[num])
