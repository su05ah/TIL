"Set"
#셋_ 순서 없으므로 시퀀스 아님
#값 수정 불가/ 값 추가나 삭제는 가능
#set() = 빈 셋  /  {} = 빈 딕셔너리
empty_set = set()
print(empty_set)
vowels={'a','e','i','o','u','a','e'}
print(vowels) #중복된 원소는 삭제됨 / 원소의 순서가 없음
empty_set.add("abc")
empty_set.add((1,3)) #튜플은 원소로 추가 가능 BUT!! 리스트는 불가
print(empty_set)
set=empty_set.copy() #셋 복사하기
set.update({"list","시퀀스인데","반복가능객체를 집합으로 간주하여","합집합 가능"})
print(set)
set.discard("시퀀스인데") #무시함
set.remove("합집합 가능") #버림
print(set.discard(("시퀀스인데"))) #None 리턴
'''print(set.remove(("합집합 가능")))''' #오류

set1={1,2,3,4}
set2={4,5,6,7}
print(set1.isdisjoint(set2)) #false__set1과 set2가 서로소 집합 아님(셋 둘다 공집합일 경우 true)
p=set1.pop() #원소 중에서 무작위로 하나 삭제
print(p)
print(set1)
