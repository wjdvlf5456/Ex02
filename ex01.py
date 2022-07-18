# list
# 리스트는 변경이 가능한 자료형이다.
print("================== 리스트 기본 ==================")

tList = []
tList = [1, 2, "python"]
print(tList[0], tList[1], tList[2])     # 출력결과: 1 2 python
print(tList[-1], tList[-2], tList[-3])  # 출력결과: python 2 1

print(tList[1:3])                       # 출력결과: [2, 'python']
ttList = tList[1:3]
print(tList)
print(ttList)

print(tList * 2)
print(tList + [3, 4, 5])
print(len(tList))                       # len(리스트) 리스트의 길이 출력
print(2 in tList)                       # 배열내에 값이 있는지 확인

print("")
print("================== 리스트 삭제방법 ==================")
# del(tList[0])
print(tList)

print("")
print("================== 리스트 수정방법 ==================")
tList[0] = "일"
print(tList)

bList = ['apple', 'banana', 10, 20]
bList[2] = bList[2] + 90
print(bList)

print("")
print("============= 리스트 수정방법(슬라이스 사용) =============")
# 값만 사라지고 배열은 사라지지 않는다.
print("========== cList ==========")
cList = [1, 12, 123, 1234]
cList[0:2] = [10, 20]
print(cList)

cList[0:2] = [10]
print(cList)

cList[1:2] = [20]
print(cList)

cList[2:3] = [30]
print(cList)

print("")
print("========== dList ==========")
dList = [1, 12, 123, 1234]
print(dList)
dList[1:2] = []
print(dList)

dList[0:] = []                             # 전체 비우기
print(dList)

print("")
print("============= 리스트 값 추가(슬라이스 사용) =============")
print("========== eList ==========")
eList = [1, 12, 123, 1234]

#eList[1:2] = "a"                           # 수정
eList[1:1] = "a"                            # 추가    [1:1] 처럼 같은 숫자이면 배열에 값이 추가된다.
print(eList)

eList[5:] = [12345]                         #[입력숫자:] 만약에 입력한 숫자가 배열의 len 이상이면 추가된다.
print(eList)

eList[:0] = [12, -1, 0]                     #[:0] 배열 앞에 값을 추가
print(eList)

print("=================== 리스트의 메소드 ===================")
print("============ a ============")
a = [1, 12, 123, "hello", 3.14, 1000]
print(a)

#배열 뒤 값 추가
a.append(5)
print(a)

#배열 원하는 위치에 값 추가
a.insert(3, 1000)
print(a)

#원하는 만큼 뒤에 값 추가
a.extend([6,7,8])
print(a)

b = a

#카운트
print(len(b))

#뒤집기
b.reverse()
print(b)

#정렬
b.sort()
print(b)

