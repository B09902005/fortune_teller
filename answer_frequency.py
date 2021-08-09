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

'''
我今天運勢如何？
我明天運勢如何？
我最近的幸運物品？
我最近要避免什麼東西？
用一個字形容今天的編遊？
用一個字形容今天的among us。
今年的東奧辦得怎麼樣？
新冠肺炎下半年的疫情走向？
薛若廷的轉系會不會過？
我是智障嗎？
'''
