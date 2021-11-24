# -*- coding: utf-8 -*-

from HW4_util import *

class HW3(Preprocess_util):
	def Calculate_TF_IDF_Normalization(self):
		"""
        *** 여기에 코드를 작성하시면 됩니다. ***

        *** TF,IDF,Normalized 3가지를 구현하시면 됩니다. ***

		1) self.Train_Doc 은 발화에 명사와 동사를 추출한 사전입니다.
            {0: ['아름', '자'], 1: ['자'], 2: ['아름', '일정', '확인', '하'], 3: ['일정', '확인']
            ...중략...
             5823: ['아름', '수고'], 5824: []}

		2) self.Total_Word는 아래와 같이 모든 발화(문서)의 전체 단어가 포함된 리스트입니다. (전체 단어 개수: 791개)
			['9월 1일', '윤정', '부부',
			...중략...
			'필요', '시험', '미용실']
	
             
		3) 5825개의 발화의 Normalized TF-IDF 값이 포함된 2차원 리스트(5825x791)로 return 합니다. 
		아래의 리스트안에 포함된 값은 예시일 뿐, 정답과 무관합니다.
		Ex)
		   [
			[0, 0, 0.2342, 0, 0, ... , 0],

			 ...중략...

			[0, 0, 0, 0, 0, ..., 0.7631]
		   ]

		4) 계산과정에서 발생하는 소수 값은 반올림, 올림, 버림 하지 않습니다.
		"""
		return 

if __name__=="__main__":
	preprocess = HW3()

	# 데이터를 로드합니다.
	raw_data = preprocess.Load_Data()
	print(raw_data)
	# TF, IDF, Normailization 을 계산합니다.
	# answer = preprocess.Calculate_TF_IDF_Normalization() 
	# 정답을 출력합니다.
	# preprocess.Output_Result(answer, std_name="StudentName", std_id="StudentID")
