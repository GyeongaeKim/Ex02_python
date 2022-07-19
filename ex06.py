#입출력
print("출력======================")
print("orange" "banana" "apple")
print("orange" + "banana" + "apple")

print("orange", "banana", "apple")


#다른 문자열로 구분할 때는 sep="" 를 사용한다
print("orange", "banana", "apple", sep=",")

#마지막 문자열을 지정할 수 있으며 기본값은 \n이다
print("orange", "banana", "apple", end="=====")
print("orange", "banana", "apple", end="\n")

#구분자와 마지막 값을 같이 쓸때
print("orange", "banana", "apple", sep=",", end="=====")



print("\n")
print("입력======================")
print('숫자를 입력해 주세요')
no = input()
print(no)

print('숫자를 입력해 주세요 :')
print("숫자: ", end="")
num = input()
print(num)