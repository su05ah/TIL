"List"
#시퀀스(sequence) : 데이터가 순서있게 차례로 저장되는 자료구조 (스트링<문자열>, 리스트, 튜플)
#리스트(list) : 0개 이상의 객체들의 시퀀스/객체들의 자료형은 서로 다를 수 있음/각 개체들을 수정하거나 삭제 가능/같은 원소 중복가능

empty_list = [] #빈 리스트
print(empty_list)

names = ['suah', 'dohyun', 'mina'] #원소가 한 개 이상인 리스트
print(names)

long_list = ['Jan', 'Feb', "Mar", """Apr""",  #여러 개 줄에 걸쳐서 원소 나열
             '''May''','Jun','Jul', 'Aug',
             'Sep', 'Oct', 'Nov', 'Dec'
    ]
print(long_list)

vowels = list("aeiou")  #함수 list()를 사용
print(vowels)
vowel_tuple = ('a', 'e', 'i', 'o', 'u')  #튜플
vowels = list(vowel_tuple)
print(vowels)

today = "4/21/2024"  #문자열 메소드 split()에 의해 리스트가 리턴됨
print(today.split('/'))

month_names = ['', 'Jan', 'Feb', "Mar", """Apr""", 
'''May''', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
print(month_names[1])  #오프셋 사용하여 리스트 원소에 접근하기

fruits = ['apple', 'banana', 'strawberry']
fruits[2] = 'watermelon' #리스트의 원소 바꾸기
print(fruits)
fruits.append('pear') #리스트 끝에 원소 추가하기
print(fruits)
fruits.insert(1, 'berry') #리스트 중간에 항목 삽입하기
print(fruits)
fruits.remove('apple') #리스트 항목 삭제하기 -> 값을 기준으로 항목 삭제
print(fruits)
del fruits[2] #리스트 항목 삭제하기 -> 인덱스나 슬라이스를 기준으로 항목 삭제
print(fruits)

my_list =[1,2,3,4,5]
popped_item = my_list.pop(2)  #pop? list에서 해당하는 항목을 제거하고 동시에 반환하는 메소드
print(my_list)  #결과: [1,2,4,5]
print(popped_item)  #결과: 3

print(my_list.index(2)) #원소 값으로 항목의 오프셋 찾기

banana = list('banana')
print(banana)
print('a' in banana) #True 원소 값이 존재하는지 확인하기

people =['suah','dohyun','jiwon','mina','suah']
print(people.count('suah')) #2번 존재_ count()
print(',,'.join(people)) #join() <-> split()

list_a =[1,2,3]
list_b =[4,5,6]
print(list_a)
print(list_b)
list_a = list_b  #대입 연산자 = 사용
print(list_a)

#리스트 복사하기
list_x =[2,4,6]
list_y =[1,3,5]
list_x = list_y.copy() #메소드 copy()사용
list_x = list(list_y) #일반 함수 list()사용
list_x = list_y[:] #슬라이스 [:]사용
print(list_x)
print(list_y)

hello = list("hello")
world = list("world")
print(hello + world) #연산자 +로 병합하기
hello+=world
hello.extend(list("!")) #리스트에 '!'값 추가
print(hello)

hi = list("hi")
suah = list("suah")
hi.append(suah) #append를 사용하면 리스트가 병합되지 않고 리스트 자체가 원소로 추가된다
print(hi)

x = list("0123456789")
print(x) #0,1,2,3,4,5,6,7,8,9
print(x[:]) #0,1,2,3,4,5,6,7,8,9
print(x[0:10]) #0,1,2,3,4,5,6,7,8,9__ 10-1=9까지 값을 리턴
print(x[:9]) #0,1,2,3,4,5,6,7,8__ 9-1=8까지의 값을 리턴
print(x[::2]) #0,2,4,6,8__ start:end:step
print(x[1::2]) #1,3,5,7,9
print(x[::-1]) #9,8,7,6,5,4,3,2,1,0
print(x[::-2]) #9,7,5,3,1
print(x[-2::-2]) #8,6,4,2

exam_scores = [30,100,45,67,29]
print(exam_scores)
exam_scores.sort() #원소 정렬하기
print(exam_scores)
exam_scores.sort(reverse=True) #원소를 역순으로 정렬하기
print(exam_scores)
'**숫자와 문자열을 동시에 원소로 하는 리스트는 정렬 불가'
print(len(exam_scores)) #리스트 원소의 총 개수 리턴
print(sorted(exam_scores)) #리스트의 정렬된 복사본을 리턴하지만, 본래 리스트는 변하지 않았다!

#리스트는 다른 리스트의 원소가 될 수 있다
xyz =[1,2,3,4,[1,2,3,4]]
print(xyz[0])
print(xyz[4])
print(xyz[4][2])
