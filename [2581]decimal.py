m = int(input())
n = int(input())
count = 0

numList = []
for i in range(m, n+1):
    for j in range(2, i):
        if i%j==0: # 나눴을때 0이 아니면 소수니까.
            count+=1
            break
        if count == 0:
            numList.append(i) # 나머지 0아니였던걸 리스트에 추가


if len(numList) > 0:
    print(numList)
    print(sum(numList))
   # print(min(numList))
else:
    print(-1)