가설과 추론

 

7.1 통계적 가설검정

 

특정 사실이 사실인지 아닌지 검정해 보고 싶을 때 사용한다.

 

7.2 예시 : 동전 던지기

 

from typing import Tuple

import math

 

def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:

    mu = p * n

    sigma = math.sqrt(p * (1 - p) * n)

    return mu, sigma

 

from scratch.probability import normal_cdf

 

normal_probability_below = normal_cdf

 

def normal_probability_above(lo: float,

                             mu: float = 0,

                             sigma: float = 1) -> float:

    return 1 - normal_cdf(lo, mu, sigma)

 

def normal_probability_between(lo: float,

                               hi: float,

                               mu: float = 0,

                               sigma: float = 1) -> float:

    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

 

def normal_probability_outside(lo: float,

                               hi: float,

                               mu: float = 0,

                               sigma: float = 1) -> float:

    

    return 1 - normal_probability_between(lo, hi, mu, sigma)

 

from scratch.probability import inverse_normal_cdf

 

def normal_upper_bound(probability: float,

                       mu: float = 0,

                       sigma: float = 1) -> float:

    

    return inverse_normal_cdf(probability, mu, sigma)

 

def normal_lower_bound(probability: float,

                       mu: float = 0,

                       sigma: float = 1) -> float:

    

    return inverse_normal_cdf(1 - probability, mu, sigma)

 

def normal_two_sided_bounds(probability: float,

                            mu: float = 0,

                            sigma: float = 1) -> Tuple[float, float]:

   

    tail_probability = (1 - probability) / 2

 

    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

 

    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

 

    return lower_bound, upper_bound

 

mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5) 

 

-----------------------------------------------------------------

 

# (469, 531)

lower_bound, upper_bound = normal_two_sided_bounds(0.95, mu_0, sigma_0)

 

 

# p가 0.5라고 가정할 때, 유의수준이 5%인 구간

lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

 

# p = 0.55인 경우 평균과 표준편차

mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

 

 

# X가 주어진 구간 안에 존재할 경우

type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)

power = 1 - type_2_probability      # 0.887

 

hi = normal_upper_bound(0.95, mu_0, sigma_0)

#  526 

 

type_2_probability = normal_probability_below(hi, mu_1, sigma_1)

power = 1 - type_2_probability      # 0.936

 

7.3 p-value

 

양측검정

 

def two_sided_p_value(x: float, mu: float = 0, sigma: float = 1) -> float:

    

    if x >= mu:

        # x is greater than the mean, so the tail is everything greater than x

        return 2 * normal_probability_above(x, mu, sigma)

    else:

       

        return 2 * normal_probability_below(x, mu, sigma)

 

two_sided_p_value(529.5, mu_0, sigma_0)   # 0.062

 

import random

 

extreme_value_count = 0

for _ in range(1000):

    num_heads = sum(1 if random.random() < 0.5 else 0   

                    for _ in range(1000))               

    if num_heads >= 530 or num_heads <= 470:             

        extreme_value_count += 1                        

 

# p-value was 0.062 => ~62 extreme values out of 1000

assert 59 < extreme_value_count < 65, f"{extreme_value_count}"

 

two_sided_p_value(531.5, mu_0, sigma_0)   # 0.0463

 

 

tspv = two_sided_p_value(531.5, mu_0, sigma_0)

assert 0.0463 < tspv < 0.0464

 

upper_p_value = normal_probability_above

lower_p_value = normal_probability_below

 

upper_p_value(524.5, mu_0, sigma_0) # 0.061

 

upper_p_value(526.5, mu_0, sigma_0) # 0.047

 

7.4 신뢰구간

 

p_hat = 525 / 1000

mu = p_hat

sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)   # 0.0158

 

normal_two_sided_bounds(0.95, mu, sigma)        # [0.4940, 0.5560]

 

p_hat = 540 / 1000

mu = p_hat

sigma = math.sqrt(p_hat * (1 - p_hat) / 1000) # 0.0158

normal_two_sided_bounds(0.95, mu, sigma) # [0.5091, 0.5709]

 

7.5 해킹

 

from typing import List

 

def run_experiment() -> List[bool]:

    

    return [random.random() < 0.5 for _ in range(1000)]

 

def reject_fairness(experiment: List[bool]) -> bool:

  

    num_heads = len([flip for flip in experiment if flip])

    return num_heads < 469 or num_heads > 531

 

random.seed(0)

experiments = [run_experiment() for _ in range(1000)]

num_rejections = len([experiment

                      for experiment in experiments

                      if reject_fairness(experiment)])

 

assert num_rejections == 46

 

7.7 베이즈 추론

 

베타분포

 

def B(alpha: float, beta: float) -> float:

   

    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)

 

def beta_pdf(x: float, alpha: float, beta: float) -> float:

    if x <= 0 or x >= 1:          

        return 0

    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta)
