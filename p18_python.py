2.4 들여쓰기

많은 프로그래밍 언어가 코드의 단락을 구분하는데 중괄호:{  } 를 사용한다. 하지만 파이썬은 들여쓰기를 사용한다.

for i in [1, 2, 3, 4, 5]:
    print(i)                    # first line in "for i" block
    for j in [1, 2, 3, 4, 5]:
        print(j)                # first line in "for j" block
        print(i + j)            # last line in "for j" block
    print(i)                    # last line in "for i" block
print("done looping")

이 덕분에 파이썬의 기독성은 아주 높아졌지만, 들여쓰기를 잘못하면 오류가 발생하니 주의해야 한다.
공백문자는 소괄호: ( )와 대괄호: [ ] 안에서는 무시되기 때문에 다음과 같이 긴 계산을 하거나

long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 +
                           13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)
                           
 코드의 기독성을 높이는데 유용하게 씋 수 있다.
 
 list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

easier_to_read_list_of_lists = [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]
                                
자주 사용하지는 않지만, 역슬래시를 사용하면 코드가 다음 줄로 이어지는 것을 명시할 수 있다.

two_plus_three = 2 + \
                 3
                 
들여쓰기를 사용함으로써 생기는 한 가지 문제는 코드를 복사해서 파이썬 셸에 붙여넣을 때 어려움을 겪을 수 있다는 것이다.
예를 들면 다음과 같은 코드를 파이썬 셸에 붙여넣기를 하면

for i in [1, 2, 3, 4, 5]:

    # notice the blank line
    print(i)
    
인터프린터가 빈 줄을 보고 for문이 끝난 것으로 판단해서 다음과 같은 에러가 출력된다.

IndentaionError : expected an indented block

2.5 모듈

모듈을 사용하기 위해서는 import 하여 불러와야 한다.

import re
my_regex = re.compile("[0-9]+", re.I)

여기에서 re는 정규표현식을 다룰 때 필요한 다양한 함수와 상수를 포함하고 있다.
코드에서 이미 re를 사용하고 있다면 별칭을 사용할 수도 있다.

import re as regex
my_regex = regex.compile("[0-9]+", regex.I)

2.6 함수

함수란 0개 혹은 그 이상의 인자를 입력 받아 결과를 반환하는 규칙이다.
파이썬에서는 def를 이용해 함수를 정의한다.

def double(x):
    """
    이 곳에 설명 추가 할 수 있다.
    """
    return x * 2
    
    파이썬 함수들은 변수로 할당되거나 함수의 인자로 전달할 수 있다는 점에서 일급 함수의 특성을 가진다.
    
    def apply_to_one(f):
    """ 인자가 1인 함수 f를 호출"""
    return f(1)

my_double = double             
x = apply_to_one(my_double)    

짧은 익명의 람다 함수도 간편하게 만들수 있다.

y = apply_to_one(lambda x: x + 4) 

변수에 람다 함수를 할당할 수도 있다.

another_double = lambda x: 2 * x       # 이 방법은 최대한 피하는게 좋다.

def another_double(x):
    """대신 이렇게 작성하는게 좋다."""
    return 2 * x
    
함수의 인자에는 기본값을 할당할 수 있는데, 기본값 외의 값을 전달하고 싶을때는 값을 직접 명시해주면 된다.

def my_print(message = "my default message"):
    print(message)

my_print("hello")   
my_print()        

가끔씩 인자의 이름을 명시해 주면 편리하다.

def full_name(first = "What's-his-name", last = "Something"):
    return first + " " + last

full_name("Joel", "Grus")     # "Joel Grus"
full_name("Joel")             # "Joel Something"
full_name(last="Grus")        # "What's-his-name Grus"


assert full_name("Joel", "Grus")     == "Joel Grus"
assert full_name("Joel")             == "Joel Something"
assert full_name(last="Grus")        == "What's-his-name Grus"

2.7 문자열

작은 따옴표: (') 또는 큰 따옴표: (")로 묶어 나타낸다.

single_quoted_string = 'data science'
double_quoted_string = "data science"

2.8 예외처리

코드가 뭔가 잘못됐을 때 파이썬은 예외가 발생했음을 알려준다.
이를 방지하기 위해 사용할 수 있는것이 try와 excet이다.

try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")
    
 2.9 리스트
 순서가 있는 자료의 집합이라고 볼 수 있다. 배열과 비슷하지만, 리스트의 기능이 조금 더 풍부하다.
 
 integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]

list_length = len(integer_list)     #  3
list_sum    = sum(integer_list)     #  6

대괄호를 사용햐 리스트의 n번째 값을 불러오거나 설정할 수 있다.

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

zero = x[0]          # equals 0
one = x[1]           # equals 1
nine = x[-1]         # equals 9
eight = x[-2]        # equals 8
x[0] = -1            

또한 대괄호를 사용해서 리스트를 슬라이싱 할 수도 있다.
i:j는 리스트를 i번째 값부터 j번째 직전의 값까지 분리하라는 의미이다.

assert x == [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]

first_three = x[:3]                 # [-1, 1, 2]
three_to_end = x[3:]                # [3, 4, ..., 9]
one_to_four = x[1:5]                # [1, 2, 3, 4]
last_three = x[-3:]                 # [7, 8, 9]
without_first_and_last = x[1:-1]    # [1, 2, ..., 8]
copy_of_x = x[:]                    # [-1, 1, 2, ..., 9]

문자열 같은 순차형 변수를 나눌 수도 았다.
간격을 설정도 가능하다. 간격은 음수로도 설정 할 수 있다.

assert every_third == [-1, 3, 6, 9]
assert five_to_three == [5, 4, 3]

in연산자를 사용하면 리스트 안에서 항목의 존재 여부를 확인할 수 있다.

1 in [1, 2, 3]    # True
0 in [1, 2, 3]    # False

주어진 리스트에 바로 다른 리스트를 추가하고 싶다면 extend를 사용한다.

x = [1, 2, 3]
x.extend([4, 5, 6])     

만약 x를 수정하고 싶지 않다면 리스트를 더해 줄 수도 있다.

x = [1, 2, 3]
y = x + [4, 5, 6]      

주로 리스트에 항목을 하나씩 추가하는 경우가 많다.

x = [1, 2, 3]
x.append(0)      # x = [1, 2, 3, 0]
y = x[-1]        #  0
z = len(x)       #  4

만약 리스트 안에 몇 개의 항목이 존재하는지 알고 있다면 손쉽게 리스트를 풀수도 있다.

x, y = [1, 2]    

하지만 양쪽 항목의 개수가 다르다면 ValueError가 발생한다.

2.10 튜플
변경할 수 없는 리스트이다.
리스트에서 수정을 제외한 모든 기능을 튜플에 적용할 수 있다.
튜플은 대괄호 대신 괄호를 사용해서 정의한다.

my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3      #  [1, 3]

try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")
    
함수에서 여러 값을 반환할 때 튜플을 사용하면 편하다.

def sum_and_product(x, y):
    return (x + y), (x * y)

sp = sum_and_product(2, 3)     #  (5, 6)
s, p = sum_and_product(5, 10)  # s = 15, p = 50

튜플과 리스트는 다중 할당을 지원한다.

x, y = 1, 2     #  x = 1, y = 2
x, y = y, x     #  x = 2, y = 1

2.11 딕셔너리
특정 값과 연관된 키(key)를 연결해 주고 이를 사용해 값을 빠르게 검색할 수 있다.

empty_dict = {}                    
empty_dict2 = dict()                
grades = {"Joel": 80, "Tim": 95}   

대괄호를 사용하여 키 값을 불러올 수 있다.

joels_grade = grades["Joel"]       

존재하지 않는 키값을 입력하면 애러가 발생한다.

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")
    
연산자 in을 사용하면 키의 존재 여부를 알수있다.

joel_has_grade = "Joel" in grades     # True
kate_has_grade = "Kate" in grades     # False

joels_grade = grades.get("Joel", 0)   #  80
kates_grade = grades.get("Kate", 0)   #  0
no_ones_grade = grades.get("No One")  #  None

grades["Tim"] = 99                   
grades["Kate"] = 100                  
num_students = len(grades)            #  3

tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys   = tweet.keys()     
tweet_values = tweet.values()   
tweet_items  = tweet.items()   

"user" in tweet_keys            
"user" in tweet                 
"joelgrus" in tweet_values    

2.11.1 defaultdict

단어를 키로, 빈도수를 값으로 지정하는 딕셔너리를 생성한다.

word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
        
예외를 처리하면서 딕셔너리를 생성하는 방법

word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1
        
존재하지 않는 키를 적절하게 처리해 주는 get을 사용하여 생성 하는 방법

word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1
    
 defaultdict를 사용하기 위해서는 먼저 defaultdict모듈에서 defaultdict를 불러와야 한다.
 
 from collections import defaultdict
 
 2.12 Counter
 
 연속된 값을 defaultdict(int)와 유사한 객체로 변환해 주며, 키와 값의 빈도를 연결시켜 준다.
 
 from collections import Counter
c = Counter([0, 1, 2, 0])          # c = {0: 2, 1: 1, 2: 1}

2.13 Set

집한(set)은 파이썬의 데이터 구조 중 유일한 항목의 집합을 나타내는 구조이다.
집합은 중괄호를 사용해서 정의한다.

primes_below_10 = {2, 3, 5, 7}

{ } 는 비어있는 딕셔너리를 의미하기 때문에 set()을 사용해서 비어 있는 set을 생성할 수 있다.

s = set()
s.add(1)       # s = {1}
s.add(2)       # s = {1, 2}
s.add(2)       # s = {1, 2}
x = len(s)     #  2
y = 2 in s     #  True
z = 3 in s     #  False

2.14 흐름제어

if를 사용하면 조건에 따라 코드를 제어할 수 있다.

if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"
    
삼항 연산자를 한 줄로 표현 가능하다.
    
parity = "even" if x % 2 == 0 else "odd" 

while문

x = 0
while x < 10:
    print(f"{x} is less than 10")
    x += 1
    
# range(10) = 0, 1, ..., 9
for x in range(10):
    print(f"{x} is less than 10")
    
더 복잡한 논리 체계

for x in range(10):
    if x == 3:
        continue  
    if x == 5:
        break    
    print(x)   # 0,1,2,4
    
2.15 True와 False
항상 대문자로 시작한다.

one_is_less_than_two = 1 < 2          #  True
true_equals_false = True == False     #  False

x = None
assert x == None, "this is the not the Pythonic way to check for None"
assert x is None, "this is the Pythonic way to check for None"

2.16 정렬

x = [4, 1, 2, 3]
y = sorted(x)     # y = [1, 2, 3, 4]
x.sort()          # x = [1, 2, 3, 4]


절대값의 내림차순으로 정렬

x = sorted([-4, 1, -2, 3], key=abs, reverse=True)  # is [-4, 3, -2, 1]

빈도의 내림차순으로 단어와 빈도를 정렬

wc = sorted(word_counts.items(),
            key=lambda word_and_count: word_and_count[1],
            reverse=True)
            
2.17 리스트 컴프리헨션
            
기존의 리스트에서 특정 항목을 선탣하거나 변환시킨 결과를 새호운 리스트에 저장해야 하는 경우

even_numbers = [x for x in range(5) if x % 2 == 0]  # [0, 2, 4]
squares      = [x * x for x in range(5)]            # [0, 1, 4, 9, 16]
even_squares = [x * x for x in even_numbers]        # [0, 4, 16]

딕셔너리나 집합의 형태

square_dict = {x: x * x for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
square_set  = {x * x for x in [1, -1]}      # {1}

2.18 자동 테스트와 assert

assert 1 + 1 == 2
assert 1 + 1 == 2, "1 + 1 should equal 2 but didn't"

위의 예시처럼 조건이 충족되지 않을 때 출력하고 싶은 문구를 추가 가능

2.19 객체 지향 프로그래밍

데이터와 관련 함수를 하나로 묶어 줄 수 있다.

class CountingClicker:
    """ 주석 추가 가능 """
    
 def __init__(self, count = 0):
        self.count = count
        
def __init__(self, count = 0):
        self.count = count

    def __repr__(self):
        return f"CountingClicker(count={self.count})"

    def click(self, num_times = 1):
        """Click the clicker some number of times."""
        self.count += num_times

    def read(self):
        return self.count

    def reset(self):
        self.count = 0
        
  clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "after two clicks, clicker should have count 2"
clicker.reset()
assert clicker.read() == 0, "after reset, clicker should be back to 0"


clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
assert clicker2.read() == 1
clicker2.reset()
assert clicker2.read() == 1, "reset shouldn't do anything"   

2.20 이터레이터와 제너레이터

제너레이터

def generate_range(n):
    i = 0
    while i < n:
        yield i   
        i += 1
        
 for i in generate_range(10):
    print(f"i: {i}")

def natural_numbers():
    """returns 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1
        
또는

evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)

정교한 데이터 처리 파이프라인을 만들 수 있다.

data = natural_numbers()
evens = (x for x in data if x % 2 == 0)
even_squares = (x ** 2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)

항목의 순서를 반환하고 싶을 때

names = ["Alice", "Bob", "Charlie", "Debbie"]

2.21 난수 생성

import random
random.seed(10)  

four_uniform_randoms = [random.random() for _ in range(4)]

random.seed(10)         
print(random.random()) 
random.seed(10)         
print(random.random()) 


random.randrange(10)    # (10) = [0, 1, ..., 9]
random.randrange(3, 6)  # (3, 6) = [3, 4, 5]

리스트의 항목을 임의 순서로 재정렬 해준다.

up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)
print(up_to_ten)
# [7, 2, 6, 8, 9, 4, 10, 1, 3, 5]   

리스트에서 임의의 항목을 하나 선택 가능

my_best_friend = random.choice(["Alice", "Bob", "Charlie"])

리스트에서 중복이 허용되지 않는 임의의 표본 리스트를 만들 수 있다.

lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)  # [16, 36, 10, 6, 25, 9]

만약 중복이 허용되는 임의의 표본 리스트를 만들고 싶다면

four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement)  # [9, 4, 4, 2]

2.22 정규표현식

문자열을 찾을 수 있다.

import re

re_examples = [                        #  true
    not re.match("a", "cat"),             
    re.search("a", "cat"),                 
    not re.search("c", "dog"),             
    3 == len(re.split("[ab]", "carbs")),   # ['c','r','s']
    "R-D-" == re.sub("[0-9]", "-", "R2D2") 
    ]
    
  assert all(re_examples), "all the regex examples should be True"
  
  2.23 함수형 도구
  
  2.24 zip과 인자 언패킹
  
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)


letters, numbers = zip(('a', 1), ('b', 2), ('c', 3))

def add(a, b): return a + b

add(1, 2)      #  3
try:
    add([1, 2])
except TypeError:
    print("add expects two inputs")
add(*[1, 2])   #  3

2.25 args와 kwargs

결과를 2배로 만드는 함수를 반환해 주는 함수

def doubler(f):
    def g(x):
        return 2 * f(x)
    return g

def f1(x):
    return x + 1

g = doubler(f1)
assert g(3) == 8,  "(3 + 1) * 2 should equal 8"
assert g(-1) == 0, "(-1 + 1) * 2 should equal 0"


def f2(x, y):
    return x + y

g = doubler(f2)
try:
    g(1, 2)
except TypeError:
    print("as defined, g only takes one argument")
    
 def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)

magic(1, 2, key="word", key2="word2")

# prints
#  unnamed args: (1, 2)
#  keyword args: {'key': 'word', 'key2': 'word2'}

def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = {"z": 3}
assert other_way_magic(*x_y_list, **z_dict) == 6, "1 + 2 + 3 should be 6"

def doubler_correct(f):
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
assert g(1, 2) == 6, "doubler should work now"

2.26 타입 어노테이션

동적 타입

def add(a, b):
    return a + b

assert add(10, 5) == 15,                  "+ is valid for numbers"
assert add([1, 2], [3]) == [1, 2, 3],     "+ is valid for lists"
assert add("hi ", "there") == "hi there", "+ is valid for strings"

try:
    add(10, "five")
except TypeError:
    print("cannot add an int to a string")

정적 타입

def add(a: int, b: int) -> int:
    return a + b

add(10, 5)           
add("hi ", "there") 

2.26.1 타입 어노테이션하는 방법

def total(xs: list) -> float:
    return sum(total)
    
예시

from typing import Callable

def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s, 2)

def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)

assert twice(comma_repeater, "type hints") == "type hints, type hints"

  Number = int
Numbers = List[Number]

def total(xs: Numbers) -> Number:
    return sum(xs)  
 


