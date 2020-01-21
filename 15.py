"""대소문자 구별 :isupper(), islower() 을 이용하면. 이 문자가 모두 대문자인지 모두 소문자인지 확인하여 
Boolean형태로 뱉어내준다. True False로
 
char1 = input(&QUOT;문자를입력하십시오:&QUOT;)

if str.isupper(char1)==True :

print(&QUOT;대문자입니다&QUOT;)

else :

print (&QUOT;소문자입니다&QUOT;)"""


char1 = input()
if str.isupper(char1) == True :
    print('%s 는 대문자 입니다.' % (char1))
else:
    print('%s 는 소문자 입니다.' % (char1))

