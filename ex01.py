#List
print("리스트 기본=======================")

tList = [1, 2, "python"]
print(tList[0], tList[1], tList[2])
print(tList[-1], tList[-2])

ttList = tList[1:3]
print(ttList)


print(tList*2)
print(tList + [3, 4, 5])
print(len(tList))       #원본은 변하지않는다

print(2 in tList)

print("리스트 삭제=======================")
# del(tList[0])       #원본에서 진짜 삭제
# del tList[0]
print(tList)



print("리스트 수정=======================")
tList[0] = "일"
print(tList)

bList = ['apple', 'banana', 10, 20]
bList[2] = bList[2] + 90
print(bList)

cList = [1, 12, 123, 1234]
cList[0:2] = [10, 20]
print(cList)

cList[0:2] = [20]
print(cList)

cList[1:2] = [20]
print(cList)

cList[2:3] = [30]
print(cList)




print("리스트 슬라이스를 통한 삭제=======================")
dList = [1, 12, 123, 1234]
dList[1:2] = []
print(dList)

dList[0:] = []      #리스트 내용만 비워버리기
print(dList)



print("리스트 슬라이스를 통한 삽입=======================")
eList = [1, 12, 123, 1234]

#eList[1:2] = "A"    #변경
eList[1:1] = "a"    #1:1 2:2 이런식으로 같은 숫자면, 추가가 된다!
print(eList)

eList[5:] = [12345]     #5번째에는 데이터가 없었기 때문에, 추가가 됨
print(eList)

eList[:0] = [12, -1, 0]     #앞에 추가
print(eList)


print("리스트의 메소드=======================")
a = [1, 12, 123, "hello", 3.14, 1000]
print(a)

#추가
a.append(5)
print(a)

a.insert(3, 1000)
print(a)

a.extend([6, 7, 8])
print(a)

#제거
a.remove(1000)
print(a)

a.pop(2)
print(a)

a.pop()
#del(a[4])



print("리스트의 메소드2=======================")
b = [1, 123, 1000, 12, 1000]
print(b)

# 카운트
print(b.count(1000))

# 뒤집기
b.reverse();
print(b)

# 정렬
b.sort()
print(b)

# index 찾기
print(b.index(1000))
