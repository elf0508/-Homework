확률

 

어떠한 사건의 공간에서 특정 사건이 선택될 때 발생하는 불확실성을 숯;적으로 나타내는 것이다.

 

6.1 종속성과 독립성

 

사건 E의 발생 여부에 대한 정보를 제공한다면 --> 종속 사건

그렇지 않다면 --> 독립 사건이다.

 

P(E,F) = P(E)P(F)

 

6.2 조건부 확률

 

만약 두 사건이 독립 사건이라면, 정의에 따라 다음과 같은 식을 얻을 수 있다.

 

P(E,F) = P(E)P(F)

 

조건부 확률

 

P(E|F) = P(E,F)/P(F) 

 

6.3 베이즈 정리

 

조건부 확률을 '반대로 뒤집는' 베이즈 정리

 

P(D/T) = P(T/D) P(D) / [P(T|D) P(D) + P(T|D) P(D)]

 

6.4 확률변수

 

특정 확률분포와 연관되어 있는 변수를 의미한다.

 

6.5 연속 분포

 

동전 던지기 : 이산형 분포

 

균등 분포의 확률 밀도

 

def uniform_cdf(x: float) -> float:

    if x < 0:   return 0    

    elif x < 1: return x   

    else:       return 1    

 

-------------------------------

 

6.6 정규분포

 

종형 곡선 모양의 분포이며, 평균인 뮤와 시그마 두 파라미터로 정의된다.

평균은 종의 중심이 어디인지를 나타내며, 표준편차는 종의 폭이 얼마나 넓은지를 나타낸다.

 

import math

SQRT_TWO_PI = math.sqrt(2 * math.pi)

 

def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:

    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma))

 

import matplotlib.pyplot as plt

xs = [x / 10.0 for x in range(-50, 50)]

plt.plot(xs,[normal_pdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')

plt.plot(xs,[normal_pdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')

plt.plot(xs,[normal_pdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')

plt.plot(xs,[normal_pdf(x,mu=-1)   for x in xs],'-.',label='mu=-1,sigma=1')

plt.legend()

plt.title("Various Normal pdfs")

plt.show()

 

------------------------------------

 

누적 분포 함수

 

xs = [x / 10.0 for x in range(-50, 50)]

plt.plot(xs,[normal_cdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')

plt.plot(xs,[normal_cdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')

plt.plot(xs,[normal_cdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')

plt.plot(xs,[normal_cdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')

plt.legend(loc=4) # bottom right

plt.title("Various Normal cdfs")

plt.show()

 

-------------------------------------------------------

 

역삼수가 필요 할 수도 있다.

 

def inverse_normal_cdf(p: float,

                       mu: float = 0,

                       sigma: float = 1,

                       tolerance: float = 0.00001) -> float:

 

 

if mu != 0 or sigma != 1:

        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

 

    low_z = -10.0                     

    hi_z  =  10.0                      

    while hi_z - low_z > tolerance:

        mid_z = (low_z + hi_z) / 2     

        mid_p = normal_cdf(mid_z)      

        if mid_p < p:

            low_z = mid_z              

        else:

            hi_z = mid_z               

 

    return mid_z


6.7 중심극한정리

동일한 분포에 대한 독립적인 확률변수의 평균을 나타낸다.

이항 확률변수

def bernoulli_trial(p: float) -> int:
    return 1 if random.random() < p else 0

def binomial(n: int, p: float) -> int:
    return sum(bernoulli_trial(p) for _ in range(n))

----------------------------------------------------

베르누이 확률변수

 

from collections import Counter

 

def binomial_histogram(p: float, n: int, num_points: int) -> None:

    data = [binomial(n, p) for _ in range(num_points)]

 

    histogram = Counter(data)

    plt.bar([x - 0.4 for x in histogram.keys()],

            [v / num_points for v in histogram.values()],

            0.8,

            color='0.75')

 

    mu = p * n

    sigma = math.sqrt(n * p * (1 - p))

 

    xs = range(min(data), max(data) + 1)

    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)

          for i in xs]

    plt.plot(xs,ys)

    plt.title("Binomial Distribution vs. Normal Approximation")

plt.show()

 

 

 

 

 

 


 

 
