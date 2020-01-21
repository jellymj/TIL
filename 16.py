"""import random

for i in range(1) :
num=int(input(&QUOT;가위= 0 바위= 1 보= 2\n\n중하나를결정하시오&QUOT;))
com=random.randrange(0,3,1)
print(&QUOT;컴퓨터의가위바위보숫자:&QUOT;,com)

if num&GT;2 or num&LT;0:
print(&QUOT;잘못입력&QUOT;)
break
elif num==com:
print(&QUOT;비겼습니다\n&QUOT;)
elif (num==0 and com ==1) or (num==1 and com==2) or (num==2 and com==0):
print(&QUOT;졌습니다\n&QUOT;)
else:
print(&QUOT;이겼습니다&QUOT;)"""

a = input()
b = input()
lst = ["가위", "바위", "보"]
result = "잘못된 입력입니다."

#a가 가위인 경우
if a == lst[0]:
    #b가 낸 것에 따라 결과 설정
    if b ==lst[0]:
        result = "Result : Draw"
    elif b == lst[1]:
        result = "Result : Man2 Win!"
    elif b == lst[2]:
        result = "Result : Man1 Win!"
