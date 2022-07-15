# list
# 리스트는 변경이 가능한 자료형이다.
print("================== 리스트 기본 ==================")

tList = []
tList = [1, 2, "python"]
print(tList[0], tList[1], tList[2])      # 출력결과: 1 2 python
print(tList[-1], tList[-2], tList[-3])   # 출력결과: python 2 1

print(tList[1:3])                        # 출력결과: [2, 'python']
ttList = tList[1:3]
print(tList)
print(ttList)

print(tList * 2)
print(tList + [3, 4, 5])
print(len(tList))                        # len(리스트) 리스트의 길이 출력
print(2 in tList)                        # 배열내에 값이 있는지 확인


print("================== 리스트 삭제방법 ==================")
#del(tList[0])
print(tList)


print("================== 리스트 수정방법 ==================")
tList[0] = "일"
print(tList)

bList = ['apple', 'banana', 10, 20]
