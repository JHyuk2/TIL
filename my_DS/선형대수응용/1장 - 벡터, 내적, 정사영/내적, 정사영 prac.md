

```python
# 문제 1
'''
# random_vector prac
    a = random_vector(ZZ, 10, x = -20, y = 20)  -- 정수(ZZ, num_of_elem, num_range - xy)
    z = random_vector(RR, 10, min = -20, max = 20) -- 실수(RR, num_of_elem, num_range - minMax)
'''

# 1) -20 ~ 20 사이의 10개의 random_elements들 생성
x = random_vector(10, -20, 20)
y = random_vector(10, -20, 20)
print("x: {}".format(x))
print("y: {}".format(y))


# 2) x.inner_product(y) = ||x|| * ||y|| * cos(theta)
x_norm = x.norm()
y_norm = y.norm()
xy = x.inner_product(y) 
cos_theta = xy / (x_norm * y_norm)
print("cos_theta: {}, {:6f}".format(cos_theta, float(cos_theta)))

# 3) 사잇각 계산
theta = arccos(cos_theta)
print("theta: {}, rad: {:6f}, angle:{:6f}".format(theta.simplify(), float(theta), float(theta * 180) ))
```

1) 차원을 늘리기 위해 random_vector를 사용하여 x, y 생성 

2) 두 벡터의 사잇각은 v1**·**v2 = |v1| |v2| cos(theta) 를 통해 구할 수 있다.

\- 각 벡터 x, y에는 norm() (default =2) 적용

\- 두 벡터의 내적_xy = x.inner_product(y)

\- cosine에 대한 식으로 정리하여 cosine(theta)값을 구함

3) arccos – cosine값에 따른 theta값 반환



```python
# 문제 2 - projection

# 1) 벡터 생성 range(-20 ~ 20)
x = random_vector(ZZ, 10, -20, 20)
y = random_vector(ZZ, 10, -20, 20)
print("x: {}".format(x))
print("y: {}".format(y))

# 2) 내적 이용
# 2-1) p : proj_xy  => px = p.inner_product(x), (y-px).inner_product(x) = 0 (직교)
# 2-2) 정리 ~  p = y.inner_product(x) / x.inner_product(x)*x
# 2-3) w = y - p
yx = y.inner_product(x)
xx = x.inner_product(x)
p = yx/xx * x
w = y - p

print("p: {}, \nw: {}".format(p, w))
```



**□ 설명**

1) 차원을 늘리기 위해 random_vector를 사용하여 x, y 생성

2) y에서부터 x선(L)으로의 수선의 발을 긋는다.

\- 수선의발의 높이: w /정사영 xy : p

3) 계산

  \- 1) p = | y | | cos_theta(x,y) : x, y의 사잇각) |                                         -- (a)

\- 2) p의 방향은 x와 같다(평행) => x / |x|                                           -- (b)

​    방향이 반전되는 경우가 있기 때문에 cos_theta(x, y) / |cos_theta(x, y)| 를 붙여준다. -- (c)

  \- 3) 즉, p의 방향은 b * c로 설정할 수 있다. 

  \- 4) 여기서, c => cos_theta(x,y)) = x·y / |x||y| 로 쓸 수 있고,

  \- 5) a * b * c (Y_vec *방향)를 연결시켜 써서 다음과 같이 정리할 수 있다.

**P = a \* b \* c** 

**= | y | | cos_theta(x, y) |** 

**= | y | \* cos_theta(x, y) / | cos_theta(x, y) | \* ( x / |x| )** 

**= | y | \* | y** **· x | / | y |\*| x |  \*  y · x / | y \* x |  \* x / | x |** 

**= y****·x / |x|^2 \* x**

**== y.inner_product(x) / x.inner_product(x) \* x**

 

**W = y – p**