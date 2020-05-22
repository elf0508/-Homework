선형대수

벡터 공간을 다루는 수학의 한 분야이다.

4.1 벡터

어떤 유한한 차원에 존재하는 점들이다.
대부분의 데이터, 특히 숫자로 표현된 데이터는 벡터로 표현 가능하다.

from typing import List

Vector = List[float]

height_weight_age = [70,  
                     170,
                     40 ] 

grades = [95,   
          80,   
          75,   
          62 ] 

-----------------------------------------------

 두 벡터를 묶은 뒤, 각 성분끼리 더한다
 
def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]   

-----------------------------------------------------------

뻴셈 : 각 성분끼리 빼준다.

def subtract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v, w)]
    
  assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]
  
  -------------------------------------------------------
  
  벡터로 구성된 리스트에서 모든 벡터와 각 성분을 더한다.
  
 def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "no vectors provided!"

    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]

------------------------------------------------------------------------

벡터에서 스칼라를 곱한다.

def scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]

----------------------------------------------------------

같은 길이의 벡터로 구성된 리스트 --> 각 성분별 평균 구하기

def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]

-------------------------------------------------------------

벡터의 내적 : 벡터의 각 성분별 곱한 값을 더한다.

def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vectors must be same length"
    
   return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32  # 1 * 4 + 2 * 5 + 3 * 6 

def sum_of_squares(v: Vector) -> float:
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14  # 1 * 1 + 2 * 2 + 3 * 3

-----------------------------------------------------

제곱의 합을 이용 --> 벡터의 크기 구하기

import math

def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))   

assert magnitude([3, 4]) == 5

-----------------------------------------------------

두 벡터간의 거리 구하기

def squared_distance(v: Vector, w: Vector) -> float:
    return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
    return math.sqrt(squared_distance(v, w))

def distance(v: Vector, w: Vector) -> float: 
    return magnitude(subtract(v, w))

-------------------------------------------------

 4.2 행렬   

2차원으로 구성된 숫자의 합

Matrix = List[List[float]]

A = [[1, 2, 3],  
     [4, 5, 6]]

B = [[1, 2],     
     [3, 4],
     [5, 6]]

------------------------------------------

 행렬을 리스트의 리스트로 나타내는 경우
 
from typing import Tuple

def shape(A: Matrix) -> Tuple[int, int]:
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0   
    return num_rows, num_cols

assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3) 

-------------------------------------------------

행렬이 n개의 행과 k개의 열로 구성되어 있다면 이 행렬을 'n x k 행렬' 이라고 한다.
각 행의 길이 : k
각 열의 길이 : n

def get_row(A: Matrix, i: int) -> Vector:
    return A[i]            

def get_column(A: Matrix, j: int) -> Vector:
    return [A_i[j]         
            for A_i in A]   
            
-------------------------------------------------------

형태(shape)가 주어졌을때

from typing import Callable

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    
    return [[entry_fn(i, j)            
             for j in range(num_cols)]  
            for i in range(num_rows)]   
  ----------------------------------------------------
  
  5 x 5 단위 행렬
  
  def identity_matrix(n: int) -> Matrix:
    
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]
                              


