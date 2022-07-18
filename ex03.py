#dict(사전)
print("딕셔너리 생성=================")
a={}    #생성방법

a["r38"] = "빅데이터"
a["r32"] = "C언어"

print(a)

print("딕셔너리 생성=================")
d = {"야구": 5, "축구": 11, "농구":9}
print(d)

d["배구"] = 6
print(d)

del(d["축구"])
print(d)


print("딕셔너리 생성=================")
d = {"야구": 5, "축구": 11, "농구":9}
print(type(d), d)
print(len(d))
print("야구" in d)
print("배구" in d)
print("배구" not in d)

print(d["축구"])
print(d.get("축구"))

del(d["야구"])
print(d)

d = {}
print(d)


d = {"야구": 5, "축구":11, "농구": 9}
keys = d.keys()
print(keys)

values = d.values()
print(values)
print(type(values))

print(len(d))


d = {"야구": 5, "축구":11, "농구": 9}
keys = d.keys()
print(keys)

for key in keys:        #딕셔너리들의 키들을 리스트로 변환!
    #print(key, d[key])
    print("{0}:{1}".format(key, d[key]))

