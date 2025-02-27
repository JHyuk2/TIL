# Lecture 11. CNN 이해하기

### (Convolutional Neural Network)



## 1) Computer's input/output

슬래시 / 백슬래시를 인식하는 방법.

2 x 2형태의 픽셀로 인식한다.

하지만 처음 들어온 그림이라면, 컴퓨터는 어떻게 이해할 수 있을까? => 학습

![image-20200226104740835](../../assets/slash.png)



각 픽셀에 대해 일정한 가중치를 부여하게 되면 결과값들이 서로 다르게 나오는데, 

CNN의 기본은 이를 이용한 것. 

![image-20200226104740835](../../assets/CNN_slash.jpg)



2x2 CNN을 적용할 때면, pow(2, 4) = 16가지의 경우의 수가 존재하는데 이 중 가장 효과적인 레이어를 사용하여 합치는 것이 필요하다.

![image-20200226104740835](../../assets/CNN_choices.jpg)





최적의 weight를 찾는 방법은 보통 로지스틱 회귀를 사용하여 찾는다.

![image-20200226104740835](../../assets/CNN_find_weight.jpg)



## 2) Gradient Descent (경사하강법)

가중치를 찾아나가는 방법 중 가장 많이 쓰이는 방법은 경사하강법이다.

(보통 adam을 가장 많이 사용한다!)



### 경사하강법

> 이 부분은 따로 정리해야 할 만큼 중요한 부분이기 때문에 추후 작성 예정.
>
> 신경망에서는 보통 역전파(Back-propagation)를 사용하여 이를 찾아나가게 된다.



더 큰 그림에 지금같은 mask를 씌워서 조금씩 축소시켜나간 후 우리가 알고 있는 그림으로 만들어주면 어떨까?



![image-20200226104740835](../../assets/CNN_masking.jpg)

즉, **CNN**의 핵심은 mask를 씌워서 **사이즈를 줄여나가는것**이고, 이 과정을 `풀링(Pooling)`이라 부른다.



3x3행렬에 slash / reversed_slash 각각의 룰을 적용해서 4인 값들에 선을 그어주면 각각 다른 그림이 나오는 걸 확인할 수 있다.

각각 X, O, /, \ 의 형태를 구했다면, 이를 Fully Connected Layer로 바꿔준다.

### X => [\\, /, /, \\]

[Slash & Reversed slash] convolution filter

| \     | 1      | -1    | -1    | 1      |
| ----- | ------ | ----- | ----- | ------ |
| **/** | **-1** | **1** | **1** | **-1** |

3x3 의 레이어가 있고, 계산된 결과값들은 총 4개의 룰(서로 다른 4개의 이미지)  중 가장 높은 값을 갖는 결과를 선택하게 된다.

![image-20200226104740835](../../assets/CNN_rule.jpg)

각각의 필터를 적용하면서 룰 베이스에 가장 잘 맞는 필터를 찾아나가고, 그 결과값을 통해 서로 다른 이미지를 인식할 수 있다.



## 3) 정리

- CNN 쉽게 이해하기

> 슬래쉬, 역슬래쉬 인식을 통해 컴퓨터는 O, X 분류가 가능하다
>
> 이 때, 값들이 슬래쉬와 역슬래쉬로 변하는 과정을 CNN에서의 Convolution Layer / Pooling Layer라고 판단할 수 있고 X, O라고 인식하는 과정을 Fully Connected Layer로 판단할 수 있다.



- X 의 이미지를 인식할 때, 필터를 적용하여 가장 큰 값이 있는 행과 열에 선을 그어 인식한다.
