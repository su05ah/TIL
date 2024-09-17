"Tuple"
#Sequence_ 데이터가 순서대로 저장되는 자료구조(스트링, 리스트, 튜플)
#튜플과 리스트
#튜플=리스트_ 0개 이상의 객체들, 같은 원소 중복 가능, 객체 자료형 다를 수 있음
#튜플!=리스트_각 개체 수정하거나 삭제 불가, 임의 위치에 객체 추가 불가,=> 튜플은 불변
#리스트 대신 튜플? 메모리 적다/원소수정의 오류 없다/딕셔너리의 키로 사용가능/함수 인자는 튜플로 전달됨
empty_tuple=() #빈 튜플
print(empty_tuple)
students=("suah",) #콤마도 함께 출력된다!__원소가 한개인 튜플은 원소 다음에 반드시 콤마를 붙인다 -- 원소 한개 이상이면 마지막 콤마 안붙여도 됨
student=["suah", ] #콤마는 출력되지 않는다. 리스트
print(students)
print((student))
#콤마가 없다면?
fruit=("apple") #콤마 없는 튜플(?)
print(type(fruit)) #class 'str'로 리턴... 튜플이 아니아ㅏ??
print(type(students)) #class 'tuple'을 리턴!!

#튜플 언패킹_ 튜플의 원소를 한 번에 여러 변수에 할당 가능
students =(1,2,3) #튜플은 불변의 시퀀스지만, 같은 이름으로 여러개의 튜플 존재 가능~
a, b, c =students #튜플 언패킹 (변수가 왼쪽이어야함!! 원소개수와 변수개수 일치!
print(a,b,c)
# 변수개수가 원소개수보다 작을 때, *붙은 변수에 나머지 튜플 원소가 할당된다
x,*y =students
print(x) #x에 1 할당
print(*y) #*y에 2,3 할당
print(len(students)) #len()
print(max(students)) #max()
print(min(students)) #min()
print(sum(students)) #sum()
a=sorted(students) #sorted()
print(a)
print(dir(students)) #튜플의 속성
print(students.index(1)) #튜플의 메소드
print(students.count(2))
