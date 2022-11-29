src_count = int(input())
src = list(map(int,input().split()))
student_count = int(input())
result = ''

for _ in range(student_count):
    gender, num = map(int,input().split())
    if gender == 1:
        for idx in range(num-1,len(src),num):
            src[idx] ^= 1
    else:
        src[num-1] ^= 1
        for idx in range(1,int(len(src)/2)+1):
            if (num-1) -idx >=0 and  (num-1) +idx <len(src) and src[(num-1) -idx] == src[(num-1) + idx]:
                src[(num-1) -idx] ^= 1
                src[(num-1) + idx] ^= 1
            else:
                break
for idx,it in enumerate(src):
    if idx % 20 == 0 and idx != 0:
        print()    
    print(it,end=' ')
