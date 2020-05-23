경사하강법

 

어떤 최적화 문제에 관한 답을 내리는 것

 

8.1 경사 하강법에 숨은 의미

 

from scratch.linear_algebra import Vector, dot

 

def sum_of_squares(v: Vector) -> float:

    

    return dot(v, v)

 

8.2 그래디언트 계산하기

 

from typing import Callable

 

def difference_quotient(f: Callable[[float], float],

                        x: float,

                        h: float) -> float:

    return (f(x + h) - f(x)) / h

 

def square(x: float) -> float:

    return x * x

 

def derivative(x: float) -> float:

    return 2 * x

 

def main():

    xs = range(-10, 11)

    actuals = [derivative(x) for x in xs]

    estimates = [difference_quotient(square, x, h=0.001) for x in xs]

    

    import matplotlib.pyplot as plt

    plt.title("Actual Derivatives vs. Estimates")

    plt.plot(xs, actuals, 'rx', label='Actual')       # red  x

    plt.plot(xs, estimates, 'b+', label='Estimate')   # blue +

    plt.legend(loc=9)

    plt.show()

    

    

    plt.close()

    

    def partial_difference_quotient(f: Callable[[Vector], float],

                                    v: Vector,

                                    i: int,

                                    h: float) -> float:

       

        w = [v_j + (h if j == i else 0)    # add h to just the ith element of v

             for j, v_j in enumerate(v)]

    

        return (f(w) - f(v)) / h

 

8.3 그래디언트 적용하기

 

v = [random.uniform(-10, 10) for i in range(3)]

    

    for epoch in range(1000):

        grad = sum_of_squares_gradient(v)    gradient at v

        v = gradient_step(v, grad, -0.01)     gradient step

        print(epoch, v)

    

    assert distance(v, [0, 0, 0]) < 0.001    

 

8.4 적절한 거리 이동하기

 

8.5  경사 하강법으로 모델 학습

 

from scratch.linear_algebra import vector_mean

    

    

    theta = [random.uniform(-1, 1), random.uniform(-1, 1)]

    

    learning_rate = 0.001

    

    for epoch in range(5000):

        

        grad = vector_mean([linear_gradient(x, y, theta) for x, y in inputs])

        

        theta = gradient_step(theta, grad, -learning_rate)

        print(epoch, theta)

    

    slope, intercept = theta

    assert 19.9 < slope < 20.1,   "slope should be about 20"

    assert 4.9 < intercept < 5.1, "intercept should be about 5"

 

8.6 미니배치와 SGD

 

theta = [random.uniform(-1, 1), random.uniform(-1, 1)]

    

    for epoch in range(1000):

        for batch in minibatches(inputs, batch_size=20):

            grad = vector_mean([linear_gradient(x, y, theta) for x, y in batch])

            theta = gradient_step(theta, grad, -learning_rate)

        print(epoch, theta)

    

    slope, intercept = theta

    assert 19.9 < slope < 20.1,   "slope should be about 20"

    assert 4.9 < intercept < 5.1, "intercept should be about 5"

 

theta = [random.uniform(-1, 1), random.uniform(-1, 1)]

    

    for epoch in range(100):

        for x, y in inputs:

            grad = linear_gradient(x, y, theta)

            theta = gradient_step(theta, grad, -learning_rate)

        print(epoch, theta)

    

    slope, intercept = theta

    assert 19.9 < slope < 20.1,   "slope should be about 20"

    assert 4.9 < intercept < 5.1, "intercept should be about 5"

    

if __name__ == "__main__": main()

 
