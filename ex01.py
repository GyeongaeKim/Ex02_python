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
