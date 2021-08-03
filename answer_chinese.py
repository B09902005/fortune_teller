import random
myfile = open('chinese.txt')
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
answer = [0 for i in range (10)]
for i in range (10):
    question[i] = input()
    ans = []
    '''
    for j in range (5):
        num = random.randint(0,length-1)
        print(j+1,':   編號%04s  ' % num, chinese[num])
        ans.append(num)
    a = input('從1到5中選一個最合適的數字，代表這一題的答案。')
    print('問題：',question[i],'     答案：', chinese[ans[int(a)-1]])
    answer[i] = chinese[ans[int(a)-1]]
    '''
    num = random.randint(0,length-1)
    print('編號%04s  ' % num, chinese[num])
    answer[i] = chinese[num]
print('\n\n\n\n')
for i in range (10):
    print('問題：',question[i],'     答案：', answer[i])

'''
問題： 我今天運勢如何？      答案： 砸
問題： 我明天運勢如何？      答案： 奸
問題： 我這幾天的幸運物品？      答案： 螅
問題： 我這幾天要注意什麼事情？      答案： 丞
問題： 我等等要做什麼？      答案： 咀
問題： 用一個字形容今年的奧運？      答案： 瘻
問題： 用一個字形容中華隊今年的表現？      答案： Ｏ
問題： 明年的學測國寫題目？      答案： 尿
問題： 今年下半年的新冠肺炎疫情走向？      答案： 辣
問題： 給我一個我不會唸的字。      答案： 醣
'''
