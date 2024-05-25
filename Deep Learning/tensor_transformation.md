<Copy of Dacon-Deeplearning >



# 텐서 변환

## 1. 텐서의 변환

### 1.1. 텐서의 형태 변환 - reshape

**reshape()** 함수는 텐서의 형태를 변경하는 데 사용되는 함수로, 주어진 형태가 원본 텐서의 원소 수와 일치할 때 사용할 수 있다. 이는 데이터의 차원을 재구성하거나, 특성 연산에 적합한 형태로 텐서를 조정할 필요가 있을 때 매우 유용하다.

```python
import torch

x = torch.arange(16) # 0에서 15까지 숫자를 포함하는 텐서, python의 range와 닮았다.
reshaped_x = x.reshape(4, 4) # 4x4 텐서로 변경
```



### 1.2. 텐서의 형태 변경 - view

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