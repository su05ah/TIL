"Data Types"
'내장 자료형_ Built-in data types'

#Numeric types
print(type(365)) #int
print(type(3.14)) #float
print(type(1.0+2.0j)) #complex

#Text type
print(type("Hello world")) #str

#Sequence types
print(type(["kim", "lee"])) #list_여러 항목을 담을 수 있는 가변(variable)의 시퀀스 자료형  []
print(type(("kim", "lee"))) #tuple_리스트와 유사하지만 변경할 수 없는 시퀀스 자료형(한 번 생성된 튜플의 요소를 변경하거나 추가할 수 없다)  ()
print(type(range(6))) #range_연속된 숫자의 시퀀스를 생성하는 함수/보통 for루프와 함께 사용되며. 시작,끝,간격을 인자로 받는다 

#Mapping type
print(type({"name":"suah", "age":"20"})) #dict_key값과 value값의 쌍(각각의 키와 값은 콜론(:)을 저장하는 자료구조  {}

#Set types
print(type({1,2,4,8})) #set_중복되지 않는 항목들의 모음, 각 항목은 쉼표로 구분  {}
print(type(frozenset({1,2,4,8}))) #frozenset_변경할 수 없는 집합, 각 항목은 쉼표로 구분 {}

#Boolean type
print(type(True)) #bool_참 또는 거짓을 나타내는 자료형

#Binary types
print(type(bytes(b"Hello suah"))) #bytes_변경할 수 없는 바이트의 시퀀스/ []안에 숫자로 구성된 리스트나 bytes()생성자를 사용
print(type(bytearray(13))) #bytearray_변경 가능한 바이트의 시퀀스/ []안에 숫자로 구성된 리스트나 bytearray()생성자를 사용
print(type(memoryview(bytes(13)))) #memoryview_바이트 데이터에 접근할 수 있는 메모리 기반의 저수준 인터페이스/ 보통 바이트나 바이트어레이를 인수로 받아 생성
"""
바이트 데이터란? 컴퓨터에서 정보를 저장하고 전송하는 데 사용되는 가장 작은 단위 
하나의 byte(8bits)는 0~255까지의 숫자 중 하나를 나타낸다 = 256가지의 가능한 값 
예를 들어, 텍스트 파일, 이미지, 오디오, 비디오 등 모든 종류의 파일은 바이트 데이터로 저장된다 
Bytes_ "hello"라는 문자열을 바이트로 표현하면 b'hello'로 나타낸다,,, 한 번 생성되면 값 바꿀 수 없다! 
Bytearray_ 문자열에서 일부 문자를 변경할 수 있다 
Memoryview_ 바이트 데이터를 메모리에 직접 저장하고 읽거나 쓸 수 있도록 도와준다 -> 데이터를 복사하지 않고도 여러 다른 형태로 표현가능
"""

#None type
print(type(None)) #Nonetype_값이 없음을 나타내는 특별한 상수/ 주로 함수의 리턴 값 없을 때 사용-> 함수가 아무 값도 반환하지 않으면 자동으로 None 반환

'자료형'
#object_ 파이썬에서 모든 것이 객체로 구현됨(내장 자료형 데이터, 데이터구조, 함수, 프로그램 등)
#data types_ 객체의 자료형, data 표현법

'변수'
#컴퓨터 메모리에 저장된 값에 접근하기 위한 이름
#할당 연산자'=' -> 변수에 값을 할당

'식별자'
#변수 이름, 함수 이름. 클래스 이름. 모듈 이름 등의 이름을 칭함
'''
식별자 만드는 규칙
= 영문자 대/소문자, 숫자, 밑줄(_)을 조합하여 만든다 
= 숫자로 시작X 
= 키워드는 식별자로 사용X 
= 길이에 제한X 
= 밑줄(_)을 제외한 특수문자 사용X 
= 클래스 이름은 대문자로 시작, 그 이외의 모든 식별자는 소문자로 시작 
'''

'키워드'
#특별한 의미가 부여되어 사전에 미리 예약된 식별자
#예약어(reserves word라고도 불림)
#False None True and as assert break class continue def del elif else except finally for from global of import in is lambda ...

'리터럴'
#프로그램 내에서 그 자체로 고정된 값을 표현하는 데이터/ 프로그래밍 언어에서 값을 나타내는 방법
#숫자, 문자열, 불리언 값, 배열 등

'Numeric Types'
#정수, 실수, 복소수 
#산술 연산자
'''
x + y  더하기
x - y  빼기
x * y  곱하기
x / y  나누기
x // y  나누기
x % y  나머지
-x  음수
+x  양수
abs(x)  절대값
int(x)  정수
float(x)  실수
complex(re, im)  복소수
c.conjugate()  켤레 복소수
divmod(x, y)  tuple(x//y, x%y)를 리턴
pow(x, y)  거듭 제곱
x ** y  거듭 제곱 
'''
#floor division  (math.floor()) -> floor에 가까운 정수로 내림
#floor(3.5) = 3.0 / floor(-3.9) = -4.0 => floor에 가까운 정수로 내린다
#int(3.9) = 3.0 / int(-3.9) = -3.0 => 소수점을 버린다

'정수의 진수'
'''
10진 정수(0~9) 
2진 정수(0,1)_접두어 0b 혹은 0B
8진 정수(0~7)_접두어 0o 혹은 0O
16진 정수(0~9, a~f, A~F)_접두어 0x 혹은 0X
'''

'Boolean Type'
#Boolean type__True or False
#Boolean operators부울 연산자_ or, and, not

'비교 연산자'
'''
<
<=
>
>=
==
!=
'''

'복합 대입 연산자'
'''
x += y  x = x+y
x -= y  x = x-y
x *= y  x = x*y
x /= y  x = x/y
x %= y  x = x%y
x //= y  x = x//y
x **= y  x = x**y
x &= y  x = x&y  ->AND
x |= y  x = xㅣy  ->OR
x ^= y  x = x^y
x >>= y  x = x>>y  -> shift연산/오른쪽으로 비트를 이동시킨다. 이때 빈 자리는 부호 비트를 따라 채워진다 
x <<= y  x = x<<y  -> shift연산/왼쪽으로 비트를 이동시킨다. 이때 빈 자리는 0으로 채워진다
'''

'형변환'
#함수 int()사용
#부울 데이터를 정수로 형변환 
print(type(int(True)))
#실수 데이터를 정수로 형변환
print(int(3.14))
#정수 문자열을 정수로 형변환
a= 365
int(a)
#실수로의 형변환
print(float(False)) #부울 데이터를 실수로 형변환
print(float(355)) #정수 데이터를 실수로 형변환
print(float(a)) #실수 문자열을 실수로 형변환
#자동 형변환
'''
연산자는 같은 자료형의 데이터에 대해서만 적용가능
정수+실수 = 실수
실수+정수 = 실수
True -> 1 혹은 1.0
False -> 0 혹은 0.0
'''

'문자'
#문자와 ASCII코드 변환
#ord(): 문자를 ASCII코드로 변환
#chr(): ASCII코드를 문자로 변환
print(ord('0'))
print(chr(48))

'Escape Sequence 이스케이프 시퀀스'
#나타낼 심볼이 없어서 문자 리터럴로 표시하기 어려운 문자를 표시하기 위해 사용
"""
\n  줄바꿈
\t  탭
\v  수직 탭
\b  백 스페이스
\r  캐리지 리턴(같은 줄의 처음으로 이동)
\f  페이지 넘김
\a  경보음
\\  백슬래시
\?  물음표
\'  작은 따옴표
\"  큰 따옴표
\ooo  정수(8진수) 

HT  가로 탭
LF  줄 바꿈
VT  새로 탭
FF  폼 피드(새 페이지로 이동)
CR  캐리지 리턴(첫 칸으로 이동)
"""

fruits = 'apple,\nbanana,\nstrawberry'
fruits = '''(1)apple
   (2)banana
   (3)strawberry
   '''
print(fruits)

odd_line = "+-" * 10 +'\n'
even_line = "-+" * 10 +'\n'
square = (odd_line + even_line) * 5
print(square)

#문자열의 오프셋(offset) : 문자열의 처음 혹은 끝에서부터 현재 문자의 상대적 위치를 나타냄
#처음부터의 오프셋 : 0,1,2,3,4 ...
#끝에서부터의 오프셋 : -1,-2,-3,-4 ...

'슬라이스'
#문자열의 부분 문자열을 추출할 수 있음
#형식 : [start : end : step]
'''
[:]  처음부터 끝까지의 전체 문자열을 추출
[start:]  start 오프셋부터 끝까지의 부분 문자열을 추출
[:end]  처음부터 오프셋 end-1까지의 부분 문자열을 추출
[start:end]  start 오프셋부터 오프셋 end-1까지의 부분 문자열을 추출
[start:end:step]  step만큼의 문자를 건너뛰면서, start 오프셋부터 오프셋 end-1까지의 부분 문자열을 추출

if> step이 음수인 경우
[start:end:step] (-step)만큼의 문자를 왼쪽으로 건너뛰면서, start 오프셋부터 오프셋 end+1까지의 부분 문자열을 추출
'''

'문자열-함수/메소드'
#len() : 문자열의 길이를 리턴
string = '0123456789'
len(string) #리턴값 10

#문자열 메소드(methods)
#split() : 구분 문자 혹은 구분 문자열에 의해 분할된 부분 문자열의 리스트를 리턴
animals = 'rabbit, bird, monkey'
print(animals.split(',')) #디폴트를 ','로 구분하기
#join() : 구분 문자나 문자열로 문자열 리스트 내의 모든 문자열을 결합한 문자열 리턴
animals_list =['rabbit', 'bird', 'monkey']
print(', '.join(animals_list))
#replace() : 문자열의 일부를 다른 문자열로 대체

#T/F를 리턴하는 문자열 메소드
'''
isalnum() 문자열의 모든 문자가 알파벳이거나 숫자이면 True를 리턴
isalpha() 문자열의 모든 문자가 알파벳이면 True를 리턴
isascii() 문자열의 모든 문자가 ASCII문자이면 True를 리턴
isdecimal() 문자열이 10진수이면 True를 리턴
isdigit() 문자열의 모든 문자가 숫자이면 True를 리턴
isidentifier() 문자열이 식별자이면 True를 리턴
islower() 문자열의 영문자가 소문자이면 True를 리턴
isnumeric() 문자열의 모든 문자가 숫자이면 True를 리턴
isprintable() 문자열의 모든 문자가 출력할 수 있는 문자이면 True를 리턴
isspace() 문자열의 모든 문자가 공백문자(white space)이면 True를 리턴
istitle() 제목을 짓는 형식(모든 단어의 첫 글자는 대문자, 그 외는 모두 소문자)의 문자열이면 True를 리턴함
isupper() 문자열의 영문자가 대문자이면 True를 리턴
startswith() 특정한 부분 문자열로 시작하면 True를 리턴함
endswith() 특정한 부분 문자열로 끝나면 True를 리턴함
'''
#문자열을 반환하는 메소드
'''
capitalize() 첫 문자를 대문자로 변환
casefold() 모든 문자를 소문자로 변환
lower() 모든 문자를 소문자로 변환
upper() 모든 문자를 대문자로 변환
title() 제목을 짓는 형식(모든 단어의 첫 글자는 대문자, 그 외는 모두 소문자)의 문자열로 변환
swapcase() 대문자를 소문자로, 소문자를 대문자로 변환
replace()
zfill() 문자열의 길이가 주어진 숫자가 되도록 문자열의 처음에 '0'으로 채움
'''
#변환된 문자열을 리턴하는 메소드
'''
center() 중간 맞춤 형식으로 변환한 문자열을 리턴
ljust() 왼쪽 맞춤 형식으로 변환한 문자열을 리턴
rjust() 오른쪽 맞춤 형식으로 변환한 문자열을 리턴
strip() 문자열의 처음과 끝 부분의 모든 공백문자 혹은 주어진 문자를 제거한 문자열을 리턴
lstrip() 문자열의 첫 부분의 모든 공백문자 혹은 주어진 문자를 제거한 문자열을 리턴
rstrip() 문자열의 끝 부분의 모든 공백문자 혹은 주어진 문자를 제거한 문자열을 리턴
'''
#문자열의 오프셋이나 숫자를 리턴하는 메소드
'''
count() 문자열에서 주어진 부분 문자열이 나타나는 횟수를 리턴
find() 문자열에서 주어진 부분 문자열이 나타나는 위치의 인덱스를 리턴
index() find()와 동일하지만, 찾고자 하는 부분 문자열이 없는 경우에는 오류가 발생함
rfind() 문자열에서 주어진 부분 문자열이 나타나는 마지막 위치의 인덱스를 리턴
rindex() rfind()와 동일하지만, 찾고자 하는 부분 문자열이 없는 경우에는 오류가 발생함
'''
#리스트나 튜플을 리턴하는 메소드
'''
partition() 주어진 분리자(문자열)를 중심으로 세 부분으로 나눈 부분 문자열의 튜플을 리턴
rpartition() 주어진 분리자(문자열)가 마지막으로 나타나는 것을 중심으로 세 부분으로 나눈 부분 문자열의 튜플을 리턴
split()
rsplit() split()과 동일하지만, 오른쪽에서 부터 주어진 개수 만큼만 분리함
splitlines() 새줄 문자('\n')로 문자열을 분할한 부분 문자열의 리스트를 리턴
'''