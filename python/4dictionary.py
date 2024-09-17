"Dictionary"
#딕셔너리_ 원소의 순서가 없기에 시퀀스는 아님
#offset, index 등으로 원소 접근 불가 -> only 'key'를 통해 접근
#불변하는 객체만 키로 사용가능(스트링, 정수, 실수. 튜플..)(리스트는 사용불가!)
empty_dict ={} #빈 딕셔너리
num = {1:'one', 2:'two'} #key:value #각 원소의 키는 유일하다(같은 키 가지는 원소가 두번이상 입력되면 나중 입력값이 앞의 입력값 대체)
num2 ={1:'one', 3:'three', 1:'four'} #같은 키 가지는 원소 두번 입력됨
print(len(num))
print(len(num2))
number = [[1,2],[3,4],[5,6]]
print(dict(number)) #시퀀스를 딕셔너리로 변환하기

num = {1:'one', 2:'two'}
num[3] ="three" #원소추가
num[1] ="once" #원소변경
print(num)

hey1={0:"zero", 10:"ten"}
hey2={5:"suah"}
hey1.update(hey2) #딕셔너리 결합하기
print(hey1)
del hey1[5] #리스트와 마찬가지로.. but! offset아니고 [key]값!
print(hey1)
print(hey1.clear()) #None값 리턴/ 모든 항목 삭제함
print(3 in hey2) #false
print(5 in hey2) #true
#값을 호출함으로써 '키' 읽어오기
a={1:"1",2:"2",3:"3"}
print(1 in a)
b=a.get(1)
print(b)
#모든 키 구하기
keys=a.keys()
print(type(keys)) #dict_keys(뷰 객체)
print(keys) #모든 키값 리턴
#모든 값 구하기
values=a.values()
print(type(values))
print(values)
#모든 키, 값 구하기
items=a.items()
print(type(items))
print(items) #각 원소는 튜플로 표현된다
abc=dict.fromkeys(a,3)
print(abc)
#대입 연산자 = 사용
b=a.copy() #copy() 메소드 사용
b[4]="4"
print(b)
c=dict(a) #dict() 일반 함수 사용
c[5]="5"
print(c)
#pop_ 주어진 키를 가진 원소를 삭제하고 그 값을 리턴
pop=a.pop(1)
print(a)
print(pop)
#popitem_ 랜덤으로 한 원소를 삭제하고 그 원소를 (key,value)형식으로 리턴