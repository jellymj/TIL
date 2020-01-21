n = int(input())
count = 0
for i in range(1, n+1):
    if n%i == 0:
        count = count + 1
        print('%d(은)는 %d의 약수입니다.' % (i, n))

if count == 2:
        print('%d(은)는 %d과 %d로만 나눌 수 있는 소수입니다.' % (n, 1, n))