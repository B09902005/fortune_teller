import random
myfile = open('frequency.txt')
chinese = [0 for i in range (12050)]
frequency = [0 for i in range (12050)]
while (True):
    a = myfile.readline().split(' ')
    chinese[int(a[0])] = a[1]
    frequency[int(a[0])] = float(a[3])
    if (int(a[0]) == 12041):
        break
print('我是程式算命師。問我一個問題(如：我今天運勢如何？)，我可以用中文字來回答你。')
question = [0 for i in range (10)]
for i in range (10):
    question[i] = input()
    num = random.randint(1,1000000000000000)
    num /= 10000000000000
    for j in range (12041):
        if (frequency[j] >= num):
            print(chinese[j],'\n')
            break
