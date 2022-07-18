#Set 집합
print("셋 생성==========================")
a = {1, 2, 3}
print(a, type(a))
print(len(a))
print(2 in a)
print(2 not in a)


print("셋 메소드==========================")
a.add(4)
a.add(1)
print(a)

a.discard(100)  #값이 없어도 에러발생 없음
#a.remove(100)   #없는 값을 지우려고 시도해보면..? -> 오류난다
print(a)

a.update({1000, 5000, 3000})
print(a)


print("셋 메소드2==========================")
s1 = set([1, 2, 3, 4, 5, 6, 7, 9, 10])
s2 = set([10, 20, 30])
print(type(s1), type(s2))

s3 = s1.union(s2)   #합집합 / 겹치는거 중복 X /
#s3 = s1 | s2    #합집합(기호 사용) /
print(s3)


s4 = s1.intersection(s2)    #교집합
#s4 = s1 & s2       #교집합(기호 사용)
print(s4)


s5 = s1.difference(s2)  #차집합
#s5 = s1-s2         #차집합(기호 사용)
print(s5)


