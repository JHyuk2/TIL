# Introduction to Anomaly Detecction_r01

[Kaggle] Credit Card Fraud Detection

![Kaggle](https://user-images.githubusercontent.com/54492747/149662762-091e7f64-f283-4b5d-a169-c3a49e3c31eb.png)

필사한 노트북 주소는 다음과 같습니다.

- https://www.kaggle.com/code/ysjang0926/kor-introduction-to-anomaly-detection-r01



분석 데이터는 Kaggle의 [Credit Card Fraud Detection(신용카드 사기 검출)](https://www.kaggle.com/mlg-ulb/creditcardfraud)을 사용하였습니다.
해당 문제는 2013년 9월 유럽의 신용카드 사용자들에게 발생한 2일간의 실제 신용카드 거래내역에 대해 Fraud(사기)를 검출하는 문제이며, 데이터는 보안상 PCA로 변환하여 제공되었습니다. 총 284,807건의 거래내역이 제공되며, 이 중 사기 거래(Fraud Transaction)는 492건 밖에 되지 않습니다. 사기 거래가 정상 거래에 비해 매우 적은 0.172%로 ‘Highly unbalanced’한 특징을 가진 데이터셋이고 총 31개의 칼럼으로 이루어져 있습니다.



## 1. Anomaly Detection이란?

![Anomaly](https://user-images.githubusercontent.com/54492747/149662959-a1d9dfcd-e5c9-4fe6-8333-9ccb123b4196.png)



**Anomaly Detection(이상 탐지)**란, Normal(정상) 데이터만의 분포와 특징을 파악하여 Abnormal(비정상) 데이터를 구별해내는 문제를 의미합니다. 대부분의 데이터와 본질적인 특성이 다른 관측치를 찾아내는 Anomaly Detection 알고리즘은 오랜 시간 동안 연구되어온 분야이며, Deep Learning 방법을 적용하는 등 다양한 방향으로 발전하고 있습니다.
또한 제조업뿐만 아니라 의료 영상, Social Network, 금융 사기 등 다양한 분야에서 응용이 되고 있으며 주요 사례는 다음과 같습니다.

- Industrial Anomaly Detection
  - 산업 속 제조업 데이터에 대한 이상치를 탐지하는 사례
  - 각종 제조업 도메인 이미지 데이터에 대한 외관 검사, 장비로부터 측정된 시계열 데이터를 기반으로 한 고장 예측 등 다양한 적용 사례가 있음
  - 외관상에 발생하는 결함과 장비의 고장 등의 Abnormal 관측치가 굉장히 적은 수로 발생하지만 정확하게 예측하지 못하면 큰 손실을 유발하게 됨
- Medical Anomaly Detection
  - 의료 영상, 임상 뇌파 기록 등의 의학 데이터에 대한 희귀 현상을 탐지하는 사례
  - 주로 신호 데이터와 이미지 데이터를 다루며 X-ray, CT, MRI, PET 등 다양한 장비로부터 취득된 이미지를 다룸
- Social Networks Anomaly Detection
  - 스팸, 가짜 사용자, 악성 유저와 같이 Social Network 상의 불법 행동을 탐지하는 사례
  - 주로 Text 데이터를 다루며 Text를 통해 스팸 메일, 비매너 이용자, 허위 정보 유포자 등을 검출함
- Fraud Detection
  - 은행 거래, 보험, 신용, 금융 관련 데이터에서 불법 행위를 검출하는 사례
  - Kaggle의 [Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)과 같은 공개된 challenge도 진행된 바 있음



여기서 많은 사람들은 **이상치**라고 하는 것을 다양하게 받아들이는데 크게 1) Anomaly, 2) Novelty, 3) Outlier 로 구분할 수 있습니다. 이 3가지는 용어가 가지는 뉘앙스 차이가 조금 있다고 생각하여서 다음과 같이 정리해보았습니다.



### Anomaly 
**Anomaly**는 대부분의 데이터와 본질적인 특성이 다르며, 기존 분포에서 멀리 떨어져 있어 전혀 다른 방식으로 생성되었을 것으로 추정되는 관측치를 의미합니다. 즉, 다른 매커니즘에 의해 발생된 것처럼 다른 관측치와는 매우 다른 관측치를 말합니다. <br>
아래 그림에서 $N_1$과 $N_2$는 Normal 데이터로 고려할 수 있지만, 점 $O_1$, $O_2$, $O_3$는  $N_1$과 $N_2$의 범주에 멀리 벗어나 있기에 Anomaly 데이터로 고려할 수 있습니다. <br>
![image](https://user-images.githubusercontent.com/54492747/161285018-bacaca0d-a220-40f6-af3f-2ee26dacfdac.png)

### Novelty
**Novelty**는 본질적인 데이터는 같지만 유형이 다른 관측치를 의미합니다. 즉, 데이터에서 이전에 관찰되지 않은 새로운 패턴을 가진 관측치를 말합니다. <br>
하지만 Novelty 데이터는 Anomaly로 간주되지 않고 Normal 데이터 범주로 포함되기 때문에 차이가 있습니다.
아래 그림에서 Novel이라 표시된 백호는 Normal인 '호랑이'라는 Normal 데이터 범주로 고려되지만, 이전에 보지 못한 새로운 패턴에 해당하게 됩니다. 그에 반면, 말, 치타, 사자, 치타는 '호랑이' 범주에 속하지 않기 때문에 Anomaly 데이터로 고려할 수 있습니다. <br>
![image](https://user-images.githubusercontent.com/54492747/161286077-8fcf93e8-804d-4db2-be63-ddb0590cf186.png)

### Outlier
**Outlier**는 데이터의 전체적인 패턴에서 벗어난 관측치를 의미합니다. Outlier의 경우 보통 통계적 맥락에서 Anomaly와 비슷하게 일컫는 말입니다. 하지만 굳이 차이를 따지자면 데이터가 시계열이냐 아니냐로 구분됩니다. (시간과의 관계 여부)
* Anomaly : **시간 또는 순서**가 있는 흐름에 따른 패턴이 보편적인 패턴들과 다른 관측치
* Outlier : **시간과 관련 없이** 대상을 표현하는 관측치들의 위치를 보고 보편적인 패턴과 벗어난 관측치 <br>
![image](https://user-images.githubusercontent.com/54492747/161287940-0cd7cc7d-4705-40a1-ba29-657e984e7257.png)

<br>

이상치 탐지 시 유의할 점은 다음과 같습니다.
* class imbalance (클래스 불균형) 문제
    * 이상치가 극단적으로 적고 정상 데이터가 대부분이기 때문
* 이상치에 대한 정의는 데이터의 특성과 산업 분야에 따라 달라지기 때문에 이를 유의해서 분석해야 함

<br>

## 2. Anomaly Detection 분류
Anomaly Detection는 여러 측면에서 분류되고,  총 3가지 분류 방법으로 이 용어들을 정리하면 다음과 같습니다.

1.  학습시 **비정상 sample의 포함 여부** 및 **label 유무**에 따른 분류
    - Supervised, Semi-supervised, Unsupervised Anomaly Detection으로 나뉘어짐
2.  **비정상 sample 정의**에 따른 분류
    - 비정상적인 sample의 성격이 정상 sample과 어떻게 다른지
    - 데이터가 시간에 따라 측정되는 지 아닌 지
3.  **정상 sample의 class 개수**에 따른 분류
    - 정상 sample의 class가 Multi-class인지

이번 글에는 [학습시 비정상 sample의 포함 여부 및 label 유무에 따른 분류]를 중점으로 설명하도록 하겠습니다. 여기서 label이란 각 관측치가 Normal인지 Abnormal인지에 대한 정보를 의미합니다. 이런 label 유무에 따라 Supervised, Semi-supervised, Unsupervised Anomaly Detection으로 나뉘어집니다.

### 1) Supervised Anomaly Detection
주어진 학습 데이터 셋에 Normal 관측치와 Abnormal 관측치에 대한 Label이 **모두** 존재하는 경우 Supervised Learning 방식이며, 이를 Supervised Anomaly Detection이라 부릅니다.<br>
Supervised Learning 방식은 다른 방법 대비 정확도가 높은 특징이 있습니다. 그래서 높은 정확도를 요구로 하는 경우에 주로 사용되며, 비정상 sample을 다양하게 보유할수록 더 높은 성능을 달성할 수 있습니다.<br>
하지만 Anomaly Detection을 적용하는 분석 데이터에는 label이 모두 있는 경우가 드물고 Normal 관측치보다 Abnormal 관측치의 발생 빈도가 극히 적기 때문에, 일반적인 Supervised Learning으로 학습하게 되면 Class-Imbalance(클래스 불균형) 문제를 자주 겪게 되어 좋은 성능을 내지 못하게 됩니다.  또한 특정 데이터의 정상/이상 여부를 정확히 알지 못하게 되면 Supervised Learning 기반 방법론을 적용하는데 한계가 있기 때문에, Semi-supervised, Unsupervised Learning에 비해 잘 활용되지 않습니다.<br>
이러한 문제를 해결하기 위해 Data Augmentation(증강), Loss function 재설계, Batch Sampling 등 다양한 연구가 수행되고 있습니다. 
* 장점
	* 다른 방법 대비 정상/이상 판정 정확도가 높음
* 단점
	* Abnormal 관측치를 취득하는데 시간과 비용이 많이 들고, Class-Imbalance 문제 해결이 필요함

### 2) Semi-supervised Anomaly Detection
Supervised Anomaly Detection 방식의 가장 큰 문제는 Normal 관측치보다 Abnormal 관측치의 발생 빈도가 극히 적기 때문에 Class-Imbalnace 문제가 발생한다는 것입니다. 그렇기 때문에 정확도를 높이기 위해서는 Abnormal 관측치를 확보해야하는데 이것은 많은 시간이 비용이 든다는 단점이 있습니다. <br>
제조 데이터를 예로 들면, 제품의 외관 검사를 할 때 결점 이미지 데이터가 저장되는데 이때 정상품 이미지 또는 대표 결점의 이미지들이 수천장 취득되는 동안 특정 결점의 이미지는 겨우 1~2장 정도 발생하는 상황이 발생하게 됩니다.
이처럼 Class-Imbalance가 매우 심한 경우에는 **Normal 관측치만 가지고 모델을 학습**하기도 하는데, 이 방식을 Semi-supervised Learning이라 합니다. <br>
Semi-supervised Learning은 **Supervised Learning 방식과 Unsupervised Learning 방식의 조합**으로, Unsupervised Learning은 데이터의 대표적인 패턴을 학습하는 데 사용되고 Supervised Learning은 그 후 예측을 하기 위해 대표적인 패턴을 학습하는 데 사용됩니다. 즉, 이 학습을 통해 Normal 관측치들의 boundary를 만들어서, 이 boundary 밖에 있어 boundary에 속하지 않는 관측지들을 모두 Abnormal 관측치로 탐지하는 방법입니다.
* 장점
	* Normal 관측치만 이용하여 학습이 가능함
* 단점
	* Supervised Anomaly Detection 방법론과 비교했을 때 상대적으로 정상/이상 판정 정확도가 떨어짐

### 3) Unsupervised Anomaly Detection
Semi-supervised Anomaly Detection 방식은 Normal 관측치가 필요하며, 수많은 관측치들 중에 어떤 것이 Normal 관측치인지 Abnormal 관측치인지 정확히 알고 있어야 합니다. Nomal 여부를 정확하게 알기 어려운 상황을 고려하여, **대부분의 데이터가 Normal 관측치라는 가정을 하여 label 취득 없이 학습을 시키는** Unsupervised Anomaly Detection 방법론이 있습니다. <br>
Unsupervised Anomaly Detection은 **정상치와는 동떨어진 representation을 찾는 방법**입니다. 대표적으로 밀도를 추정하여 Abnormal 관측치를 탐지하는 Isolation Forest와 Local Outlier Factor 방법이 있으며, Principal Component Analysis(PCA, 주성분 분석)를 이용하여 차원을 축소하고 복원을 하는 과정을 통해 비정상 sample을 검출하는 방법도 있습니다. <br>
최근 수집 가능한 데이터의수가 급증하면서 기존 방법론들은 정확도에서 한계를 보이고 있어, 이에 따라 다양한 딥러닝 기반 방법론들이 활발하게 연구되고 있습니다. Deep Learning 기반으로는 대표적으로 Autoencoder 기반의 방법론이 주로 사용되고 있습니다. 
* 장점
	* 데이터의 내재적인 특성을 학습하여 데이터 내 유사성을 발견하는 작업이기에, Labeling 과정과 알고리즘 훈련이 필요하지 않음
* 단점
	* 정상/이상 판정 정확도가 높지 않고, Autoencoder의 degree of compression(차원축소를 얼만큼 해야하는지) 등과 같은 hyper-parameter에 매우 민감함 (조정 필요)
    

<br>