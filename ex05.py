#패킹과 언패킹
#packing은 나열된 객체를 tuple로 저장하는 것을 말한다.
#unpacking은 반대의 작업으로 tuple, list 안의 객체를 개개의 변수로 할당할 수 있다.
t = {10, 20, 30, "python"}
print(t)
print(type(t))

a, b, c, d = t
print(a, b, c, d)



aList = [10, 20, 30, "python"]
h, i, j, k = aList
print(h, i, j, k)


print("형변환==============")
t = (1, 2, 3)
print(t, type(t))

s=set(t)
print(s, type(s))

l = list(s)
print(l, type(l))

tu = tuple(l)
print(tu, type(tu))