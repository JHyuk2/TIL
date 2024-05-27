# 딥 러닝 기초 - 역전파

가장 간단한 `y = WX + b` 형태의 딥 러닝 모델을 생각해보자.

딥 러닝은 기본적으로 세 개의 층으로 이루어진다.

- 입력층 (Input layer)
- 은닉층 (Hidden layer)
- 출력층 (Output layer)



#### 순전파

- 순전파란, 우리가 생성한 모델이 예측값을 만들어내기 위한 과정으로, 훈련 데이터를 모델에 넣으면 모델이 가중치를 통해 다음 층으로 넘겨주고, 거기에 편향(bias)을 더해 예측값을 산출하게 된다. 



#### 역전파

- 역전파(Backpropagation)란, 말 그대로 순전파의 반대 방향으로 계산을 하는 것으로,

  순전파가 예측값을 산출하기까지의 과정이었다면, 역전파는 최고의 예측을 위한 가중치와 편향을 찾아나가는 과정이라고 볼 수 있다.



#### 옵티마이저

역전파에서 가장 중요한 것은 **'옵티마이저'**이다.

옵티마이저는 '최적의 W와 b를 찾아나가기 위한 도구' 라고 생각하면 된다. 그리고 기본적인 경사하강법인 Gradient Descent 방법을 사용하여 우리에게 필요한 최적의 가중치(W)와 편향(b)을 얻을 수 있는데, 이 방법을 쓰게 되면 전체 학습 세트를 전부 사용하여 가중치를 계산하기에 많은 시간과 메모리가 필요하게 된다.

이러한 단점을 보완하기 위해 나온 것이 SGD(Stochastic Gradient Descent)이다.

> SGD는 한 번의 반복 당 하나의 데이터 포인트를 사용하여 손실 함수의 기울기를 계산하기 때문에 조금은 불안정하지만 계산 비용을 대폭 줄여주며, 대규모 데이터 세트에서 매우 효과적인 방법이다.

---



#### 역전파 과정

역전파 과정은 크게 네 단계로 나누어 볼 수 있다.

1) 오차 계산
   - 오차는 실제 값과 예측값의 차이이다.
   - 그리고 loss function은 예시에서는 mse loss를 사용하였다.
2) 가중치 계산
3) 가중치 업데이트
4) 1-2를 반복



### 예시

```python
import torch
import torch.optim as optim

# 훈련셋
x_train = torch.tensor([[1], [2], [3]], dtype=torch.float)
y_train = torch.tensor([[3], [6], [9]], dtype=torch.float)

# 가중치와 편향 0 초기화
W = torch.zeros(1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)

# 옵티마이저 설정 및 전체 에폭 수를 정의
optimizer = optim.SGD([W, b], lr=0.01) # 초기 SGD의 파라미터는 0, 0, 학습률 0.01
epochs = 1000

# -------------------------------------------------------------

# 계산 과정
for epoch in range(epochs):
    # 1) 오차 계산 -순전파 모델을 통해 예측값을 계산합니다.
    pred = x_train * W + b # -- 순전파를 통해 얻어진 예측값
    loss = torch.mean((pred - y_train) ** 2) # 예측값 - 실제값
    
    # 2) 역전파: 손실 함수의 기울기(gradient)를 계산한다.
    optimizer.zero_grad()  # 기울기를 0으로 초기화
    loss.backward()  # 역전파 수행
    
    # 3) 역전파 파라미터 업데이트 
    optimizer.step()
    
    # 4) 반복, 일정 에폭마다 학습 상태를 출력한다.
    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], W: {W.item():.3f}, b: {b.item():.3f}, Loss: {loss.item():.4f}')
        
# -------------------------------------------------------------
## 평가단계
# 평가 단계에서는 gradient가 변하면 안되기 때문에, no_grad를 통해 통제해준다.

test_x = torch.tensor([[10]], dtype=torch.float)

with torch.no_grad():
    pred_y = test_x * W + b
    print("훈련 후 입력이 10일 때의 예측값 :", pred_y.item())
```



