def judge(score):
    if score >= 90:
        return"优秀"
    elif score>=60:
        return"及格"
    else:
        return"不及格"
scores=[]
for number in range(1,4):
    score=int(input(f"第{number}次输入整数成绩："))
    if 0<=score<=100:
        scores.append(score)
    else:
        print ("请输入0~100的整数")
total=0
passed=0
for score in scores:
    print(f"{score}分{judge(score)}")
    total=total+score
    if score>=60:
        passed=passed+1
if len(scores)>0:
    average=total/len(scores)
    print(f"有效{len(scores)}人 及格{passed}人")
    print(f"平均分为{average:.1f}")
else:
    print("没有有效成绩")
