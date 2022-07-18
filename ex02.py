#튜플
#순서를 가지는 객체들의 집합이라는  것은 list와 같지만 수정 불가(immutable) 자료형
#순서(index)가 있는 시퀀스 자료형이다.
#시퀀스의 연산(인덱싱, 슬라이싱, 연결(+), 반복(*), len(), in, not in 등의 연산이 가능

print("튜플 생성하기==============")
t = (1, 2, 3)
# t = 1, 2, 3
# t = tuple([1,2,3])
#t = (1,)
print(t, type(t))


print("튜플값 사용하기==============")
t = (1,2,"python")
print(t, type(t))

print(t[0], t[1], t[2], t[-1], t[-2])
print(t[1:3])
print(t[1:])
print(t[:])


print("튜플의 연결 확장==============")
ttt = t*3
print(ttt)
print(t)

print(t + (3,4,5))
print(t)

t = t+(3,4,5)   #이렇게 해야 합쳐짐
print(t)


print(len(t))
print(20000 in t)


print("튜플의 값 변경불가==============")
t = ('apple', 'banana', 10, 20)
#t[0] = "mango"  #변경 불가능
#t[2] = t[2] + 90   #불가
print(t)
print(t[2])
print(t[2] + 90)


t[1:2] = (1000, 2000)
print(t)