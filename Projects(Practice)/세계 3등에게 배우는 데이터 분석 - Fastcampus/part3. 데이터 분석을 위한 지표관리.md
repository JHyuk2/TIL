## Part3. 데이터 분석을 위한 지표관리

### 비즈니스 지표 관리 Framework: AARRR

AARRR은 다음의 다섯 순서의 약자를 의미한다.

### 획득 - 활성화 - 매출 - 유지 - 추천

(act/acquisition - activation - revenue - retention - advocate/ referral)



> 5A라고 불리는 유저의 여정 탐색방법도 있다.

결국 유저의 여정은 각각의 단계가 정해져 있고, 우리는 각각의 단계에서 바라봐야 할 지표같은 게 있다.

ex)

시작단계 => CTR(클릭율), CPM, CPA 등..

acquisition => 단계에선  CAC, MAU, DAU 등...



1-4. 실습 솔루션 소개

Amplitude 라는 툴을 사용 / Product Analysis

Amplitude는 기본적으로 event기반 로그분석.

> Sementation(이벤트 분석)
>
> - 로그분석임
>
> Funnel (깔대기 - 전환율 및 이탈률 분석)



시각화를 통해 insight를 얻어낼 수 있는데,

1) 먼저 일자별로 unique id기준으로 구매가 몇 건 이루어졌느지 확인하고
2) 각 브랜드별로 매출이 얼마나 나왔는지를 보니, 연두색과 보라색이 높아질 때 치솟더라 (가설 생성) > 브랜드에 의한 매출 변동 패턴 있음
3) 가설 세부 > 브랜드의 프로모션이나 상품에 대한 고객 구매 민감도가 높음
4) 브랜드별 프로모션을 진행해보면서 프로모션에 따른 브랜드의 매출증분을 알아보자.



## 1) Acquisition: 획득

- #### Daily Active User (DAU)

- #### Monthly Active User (MAU)

- #### Customer Acquisition Cost (CAC)



#### MAU

1. Active User(활성 유저)의 정의는 무엇인가?

   - 일반적으로는 유니크 유저
     - 로그인한 유저
     - 방문한 유저
       - 웹 : cookie, 앱: Device ID

2. MAU는 월 마감이 되어야만 확인 가능한가요?

   - Rolling Window를 계산하면 매일매일의 MAU를 구할 수 있다.

     <img src='https://images.ctfassets.net/5s247im0esyq/5fcoNku3nAA2qHu0vbt8My/7c99634fa390bcd61e9632eae1f5dc83/WAU_metrics.png'/>

   - MAU 트렌드를 통해 서비스의 유저 수 건전성을 확인 가능하다.

   

3. MAU의 단순 성장 vs 실질 성장의 구분

   - MAU의 구성요소를 쪼개서, 지난달 대비 건전하게 성장하는지를 확인해야 한다.

   - MAU를 다시 쪼개보면, 

     (신규 유저 + 지난 달 이전에 비활성화였다가 부활한 유저)

     = 신규유저 + 복귀유저(resurrected) + 지난 달 유지 유저

     = 다음 달 이탈 유저(churned) + 다음 달 유지 유저(retained)

     > <지난 달 기준>
     >
     > MAU(t-1) = new(t-1) + retained(t-1) + resurrected(t-1)
     >
     >  				= retained(t) + churned(t)
     >
     > 
     >
     > <이번 달 기준>
     >
     > MAU(t) = new(t)  + retained(t) + resurrected(t)

   

   **즉, MAU의 성장은 지난달 MAU 대비 이번달 MAU의 성장으로 볼 수 있다.**

   ```markdown
   MAU(t) - (MAU(t-1)) > 0 **(성장)**
   MAU(t) - (MAU(t-1)) = 0 **(유지)**
   MAU(t) - (MAU(t-1)) < 0 **(감소)**
   ```

   > MAU(t) = new(t) + retained(t) + resurrected(t)
   >
   > MAU(t-1) = retained(t) + churned(t)
   >
   > ---
   >
   > MAU(t) - MAU(t-1) = new(t) + resurrected(t) - churned(t)

   ​	(근데 생각해보면 당연한거를 수식어로 만들어놨을 뿐...)



#### Quick Ratio

- 여기서, (new+resurrected / churned) 를 `Quick ratio` 라고 한다.

단순히 MAU의 성장률이 몇 퍼센트인지 보는 것보다, Quick ratio로 보는 것이 훨씬 더 구체적으로 판단이 가능하다. (다음 달 성장 예측)



#### CAC (Customer Acquisition Cost)

- `유저 획득 단가`를 의미한다.
- 유저 획득의 기준은?
  - 회원 가입
  - 첫 구매
- 비용의 기준은?
  - 매체비
  - 매체비, 인건비, 제작비 등
- 오가닉 유저와 페이드 유저 중 어떤 유저를?
  - 전체 유저 기준
  - 페이드 유저 기준 -- 일반적으로는 페이드 유저 기준을 잡는다.



ex) 매체 광고비 1억 /  웹사이트 회원가입 5,000명 = 20,000원 (CAC 계산 끝)

> 광고 채널에 대한 효율을 비교해서 보는 게 가장 좋다.
>
> ~ 채널 성과 비교용으로 활용하기 가능

그러면, 20,000원이 비싼건가? => 이거에 대해선 LTV와 함께 비교해봐야 한다.



#### LTV / CAC ratio

- LTV, Lifetime Value : 유저 평생 가치.
  - 고객이 서비스에서 평생동안 지불하는 총 금액(가치)
  - 가치 = 총 사용한 금액 - 고객 유치 및 유지 비용 (Gross Margin)

- 건전한 기준은 3~4의 수치를 갖고, 그 때 공격적인 마케팅을 할 수 있다.

**즉, 고객 획득 비용보다 LTV가 높다면 적당한 비용을 준 게 맞다.**



## 2. Activation: 활성화
