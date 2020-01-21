#Q1. 두 개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 별(*)문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.
#가로 5, 세로 9
'''
n = 5; m = 9
print((str('*'*n)+'\n')*m)

#print ('*****\n*   *\n*   *\n*   *\n*   *\n*   *\n*   *\n*   *\n*****')
'''

#Q2. Print 함수를 한번만 사용해 다음 문장을 출력하시오.

'''print('\"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되어있습니다."\n나는 생각했다. \'cd를 써서 git bash로 들어가봐야지\'')'''

#Q3. 다음과 같은 이차방정식이 있을 때 근을 찾는 수식을 파이썬 코드를 이용하여 출력해보시오.
'''import math

def fun_2(a, b, c):
    return ((-b+math.sqrt(b**2-4*a*c))/2*a, (-b-math.sqrt(b**2-4*a*c))/2*a)
print(fun_2(1, 4, -21))'''

#Q4. Python에서 사용할 수 없는 식별자(예약어)를 찾아 작성하세요.
'''False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield'''

#Q5. 파이썬에서 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다. (float point rounding error)
# 따라서, 아래의 값을 비교하기 위해 작성해야 하는 코드를 작성하세요.
'''
a = 0.1 *3
b = 0.3
print(bool(abs(a-b) <= 1e-10))


import sys
print(bool(abs(a-b) <= sys.float_info.epsilon))

import math
print(bool(math.isclose(a,b)))
'''

#Q6. 이스케이프 문자열 중 1)줄바꿈 2)탭 3)\를 작성하세요.
'''\n , \t, \\'''

#Q7. "안녕, 철수야"를 String Interpolation 을 사용하여 출력하세요.
'''
name = "철수"
print(f'"안녕, {name}야"')
'''

#Q8. 다음 중 형변환시 오류가 발생하는 것은?
'''
int('3.5'), bool('50')
'''