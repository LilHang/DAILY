referee_num = int(input("请输入评委人数："))
score = list()

for i in range(referee_num):
    print("第%d位评委打分: " % (i + 1))
    referee_score = float(input(">>>>> "))
    score.append(referee_score)

max_score = max(score)
min_score = min(score)
avg_score = (sum(score) - max_score - min_score) / (referee_num - 2)

print("\n去掉一个最高分: %f " % max_score)
print("去掉一个最低分: %f " % min_score)
print("最后得分为: %f " % avg_score)

a = input("\n按任意键退出")