<Copy of Dacon-Deeplearning >



# 텐서 변환

## 1. 텐서의 변환

### 1.1. 텐서의 형태 변환 (reshape)

**reshape()** 함수는 텐서의 형태를 변경하는 데 사용되는 함수로, 주어진 형태가 원본 텐서의 원소 수와 일치할 때 사용할 수 있다. 이는 데이터의 차원을 재구성하거나, 특성 연산에 적합한 형태로 텐서를 조정할 필요가 있을 때 매우 유용하다.

```python
import torch

x = torch.arange(16) # 0에서 15까지 숫자를 포함하는 텐서, python의 range와 닮았다.
reshaped_x = x.reshape(4, 4) # 4x4 텐서로 변경
```



### 1.2. 텐서의 형태 변경 (view)

**view()** 함수는 원본 텐서의 데이터를 공유하는 '새로운 형태의 텐서'를 반환한다.

데이터의 실제 메모리 레이아웃을 변경하지 않으며, 새로운 인덱싱 뷰를 제공한다.

> 만약 원본 텐서가 메모리상 연속적이지 않은 경우, reshape()함수를 사용하거나, contiguous()메소드를 호출한 후 view()를 사용해야 한다.
>
> > #### Contiguous ?
> >
> > contiguous는 "인전합, 근접한"의 뜻을 가지고 있다.
> >
> > contiguous는  tensor에 사용하며, 메모리 tensor를 인접하게 재정의 하는 것을 의미한다.
> >
> > 만약 narrow(), expand(), view(), transpose() 를 통해 tensor의 모양을 변화시킬 경우, 새로운 텐서를 생성하는 것이 아닌, tensor memory주소는 그대로 둔 채 모양만 바꾼다.
> >
> > 즉, original tensor와 modified tensor의 메모리는 같이 고유한 상태이다.
> >
> > ```python
> > a = torch.randn(2, 3)
> > a.transpose_(0, 1)
> > 
> > for i in range(3):
> >     for j in range(2):
> >         print(a[i][j].data_prt())
> >         
> > """
> > ~~~80
> > ~~~92
> > ~~~84
> > ~~~96
> > ~~~88
> > ~~~00
> > """
> > 
> > print("is a contiguous?", a.is_contiguous()) # is a contiguous? False
> > ```
> >
> > 이 때, contiguous 혹은 reshape을 통해 수정을 하면 다시 순서대로의 메모리 순서로 돌아올 수 있다.



### 1.3. 차원 축소 (squeeze)

**squeeze()** 함수는 텐서에서 크기가 1인 차원을 찾아 그 차원을 제거한다. 이는 데이터의 형태를 바꾸지 않으면서 텐서를 더 효율적으로 만들어준다.

```python
tensor = torch.tensor([[[1, 2, 3, 4]]]) # shape (1, 1, 4)

# dim을 지정하지 않는 squeeze
squeezed_tensor = tensor.squeeze()
print("squeezed shape: ", squeezed_tensor) # squeezed shape: torch.Size([4])

# dim을 지정하는 squeeze
test_tensor = torch.tensor([[[1], [2], [3], [4]]]) # shape (1, 4, 1)
squeezed_test = test_tensor.squeeze(dim=0)
print("squeezed_test shape: ", squeezed_test.shape) # squeezed_test shape : torch.Size([4, 0])
```

- argument 요소 중 하나인 dim을 지정해주지 않으면, 1인 크기의 모든 차원을 제거하지만, dim을 지정해주면 특정 차원만 줄일 수 있다.

- 하지만 만약 지정한 dim이 축소할 수 없는 경우 (ex. 차원의 크기가 4), squeeze는 무효화된다.



### 1.4. 차원 확장 (unsqueeze)

**squeeze()**가 상자에서 불필요한 공간을 제거한다면, **unsqueeze()**는 상자에 조금 더 공간을 추가하는 것과 비슷하다. (지정된 위치에 새로운 차원을 추가)

squeeze() 함수는 dim이 선택사항이었지만, unsqueeze 함수는 사용을 위해선 dim을 반드시 지정해주어야 한다. 만약 dim을 지정해 주지 않는 경우, `TypeError`가 발생한다.

```python
tensor = torch.tensor([1, 2, 3, 4,]) # shape (4,)

# 첫 번째 차원을 추가하여 차원 확장
unsqueeze_tensor = tensor.unsqueeze(dim=0) # shape (1, 4)

# 마지막 차원을 추가하여 차원 확장
unsqueeze_tensor_last_dim = tensor.unsqueeze(dim=-1) # shape (4, 1)
```



### 1.5. 텐서의 차원 변환 (transpose)

**transpose()** 함수는 행렬의 행과 열을 바꾸는 것과 유사하다. 텐서의 두 차원을 서로 바꾸는 역할을 한다.

>  선형대수에서는 전치행렬, 즉  x, y축을 서로 바꾸는 것을 transpose라 부르는데, 이것과 마찬가지로 `두 개의 축`을 바꾸기 위해 사용되는 것이라 생각하면 좋을 것 같다.
>
> 3x4 사이즈의 matrix_a => T_matrix_a (4 x 3)

```python
# uniform distribution의 shape (2, 3, 4,) tensor 생성
tensor = torch.rand(2, 3, 4) 

# 더 알아보기 쉽게 하기 위해, tensor를 다음과 같이 변경
tensor = torch.arange(2*3*4).reshap(2, 3, 4) 

""" 
> 원본 텐서

tensor([[[ 0,  1,  2,  3],
         [ 4,  5,  6,  7],
         [ 8,  9, 10, 11]],

        [[12, 13, 14, 15],
         [16, 17, 18, 19],
         [20, 21, 22, 23]]])
"""


transposed_tensor = tensor.transpose(0, 1) # shape (3, 2, 4)

"""
> 변형된 텐서 (transposed)

tensor([[[ 0,  1,  2,  3],
         [12, 13, 14, 15]],

        [[ 4,  5,  6,  7],
         [16, 17, 18, 19]],

        [[ 8,  9, 10, 11],
         [20, 21, 22, 23]]])
"""
```



### 1.6. 텐서의 차원 교환 (permute)

**permute()**는 사실 transpose와 거의 유사하다. 다만, transpose는 두 차원끼리의 교환에 불과했다면, permute는 세 차원 이상의 교환에 유리하며, 순서 역시 마음대로 지정할 수 있다.

> 위에서 정의된 (2,3,4) 크기의 차원을 가진 tensor를 가지고 permute를 다시 사용해보자.

```python
# 차원 순서 재배열
permuted_tensor = tensor.permute(2, 0, 1) # 기존 dim (2, 3, 4) -> (4, 2, 3)

"""
> 변형된 텐서 (permuted)

tensor([[[ 0,  4,  8],
         [12, 16, 20]],

        [[ 1,  5,  9],
         [13, 17, 21]],

        [[ 2,  6, 10],
         [14, 18, 22]],
"""
```



## 2. 텐서의 결합과 분할

### 2.1. 텐서 결합 (cat)

**cat()** 함수는 `concatenate(연결)` 의 줄임말이다. 같은 크기의 텐서끼리 내부에서 연결지어 길이를 확장시킬 수 있다. 

> mat_a = (2 x 2) 
>
> mat_b = (2 x 3)  
>
> torch.cat(mat_a, mat_b) = (2 x 5)

```python
# 각각 사이즈가 (2, 2), (2, 3)인 텐서 생성
tensor_1 = torch.tensor([[1, 2], [3, 4]])
tensor_2 = torch.tensor([[5, 6, 7], [8, 9 , 10]])

cat_tensor = torch.cat((tensor_1, tensor_2), dim=1) # 1번 차원을 따라 결합
```

만약 dim을 지정해주지 않으면 dim=0에서 결합을 처리하게 되는데

만약 `0차원에서의 텐서 크기가 서로 다르다면 RuntimeError가 발생`하게 된다.



### 2.2. 텐서 결합 (stack)

**stack()** 함수는 `쌓다` 라는 뜻처럼, 크기가 같은 여러 개의 텐서를 합쳐, 새로운 차원을 쌓아 올린다.

단, cat과는 다르게, 모든 텐서에 대해 새로운 차원이 생기므로 텐서들은 그 크기가 동일해야 하며, 데이터를 구조적으로 정리하고 싶을 때 유용하게 사용된다.

> mat_a = (2 x 2)
>
> mat_b = (2 x 2)
>
> mat_c = (2 x 2)
>
> torch.stack((mat_a, mat_b, mat_c), dim=0) => (2 x 3)

```python
# 2x2 행렬 생성
tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[5, 6], [7, 8]])
tensor3 = torch.tensor([[9, 10], [11, 12]])

# stack 함수 사용 예제
stack_tensors = torch.stack((tensor1, tensor2, tensor3), dim=0) # shape (3, 2, 2)

# --- 아래와 같은 텐서끼리는 연산이 아예 불가능
tensor4 = torch.tensor([[1, 2, 3], [4, 5, 6]]) # (2 x 3)
tensor5 = torch.tensor([[7, 8, 9], [10, 11, 12], [11, 12, 13]]) # (3 x 3)

# dim1의 사이즈가 같지만 RuntimeError가 발생한다.
stack_tensors_45 = torch.stack((tensor4, tensor5), dim=1) 
```

- stack은 기본적으로 dim=0에서 차원계산이 이루어지는데, 만약 사이즈가 맞지 않는다면 어떻게 될까?
  - tensor끼리의 사이즈가 같지 않다며 RuntimeError가 발생한다.



### 2.3. 텐서 분할 (chunk)

**chunk()** 함수는 큰 텐서를 여러 개의 작은 텐서로 나누는 데 사용된다. 이 함수는 두 개의 argument를 받는다. 

1) 자르고 싶은 사이즈(size)
2) 자르고 싶은 차원(dim)

```python
# (2, 6, 10) 차원의 텐서 생성
tensor = torch.arange(2*6*3).reshape(2,6,3) 

# (2, 2, 3) 사이즈 3개의 텐서를 가진 chunked_tensors 생성
chunked_tensors = torch.chunk(tensor, 3, dim=1)

for i, chunk in enumerate(chunked_tensors):
    print(f"Chunk {i}: {chunk}, {chunk.shape}")
    
"""
Chunk 0: tensor([[[ 0,  1,  2],
         [ 3,  4,  5]],

        [[18, 19, 20],
         [21, 22, 23]]]), torch.Size([2, 2, 3])
         
Chunk 1: tensor([[[ 6,  7,  8],
         [ 9, 10, 11]],

        [[24, 25, 26],
         [27, 28, 29]]]), torch.Size([2, 2, 3])
         
Chunk 2: tensor([[[12, 13, 14],
         [15, 16, 17]],

        [[30, 31, 32],
         [33, 34, 35]]]), torch.Size([2, 2, 3])
"""
```



### 2.4. 텐서 분할 (split)

**split()**함수는 **chunk()** 와 비슷하지만, 조각의 크기를 더 세밀하게 지정할 수 있다.

- 예를 들어 사이즈 10의 텐서를 (4 : 6) 으로 나누고 싶다면, 그렇게 자를 수 있게 해준다.
- 마찬가지로 기본 차원은 dim=0을 기준으로 한다.

```python
# 10 * 3짜리 텐서 생성
tensor = torch.aranage(10*3).reshape(10, 3)

split_sizes = (4, 6) # 사이즈 조정
splits = tensor.split(split_sizes, dim=0)
"""
splits[0]: torch.Size([4, 3])
splits[1]: torch.Size([6, 3])s
"""
```

> chunk와 비슷하게, 나눠진 결과값은 `splits - split class`에 담기게 되는데, 
>
> 이 오브젝트는 iterable한 객체로, splits[0] 과 같이 데이터에 접근할 수 있다.



## 3. 텐서 인덱싱과 슬라이싱

> 이 부분은 판다스 넘파이와 거의 유사하며 이미 배운 내용이기에 생략.



## 4. 고급 인덱싱 기법

### 4.1. gather



