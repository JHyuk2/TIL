# -*- coding: utf-8 -*-

from PyKomoran import *
import json
import math

komoran = Komoran('EXP')

#   *** Do not modify the code ***
class Preprocess_util:
	def __init__(self):
		self.Train_Doc = dict()
		self.Total_Word = list()
		return

	def Calculate_TF_IDF_Normalization(self):
		return

	def Load_Data(self):
		print("형태소 분석중 입니다. 조금만 기다려 주세요.")
		with open('./SpeechAct_tr.json') as f:
			train_dataload = json.load(f)

		count = 0
		for i in range(len(train_dataload)):
			key = str(i+1)
			for j in range(len(train_dataload[key])):
					self.Train_Doc[count] = komoran.get_morphes_by_tags(train_dataload[key][j][1], tag_list=['NNG','NNP','VV'])
					self.Total_Word.extend(komoran.get_morphes_by_tags(train_dataload[key][j][1], tag_list=['NNG','NNP','VV']))
					count += 1

		self.Total_Word = set(self.Total_Word)
		self.Total_Word = list(self.Total_Word)

	def Output_Result(self, answer_data=None, std_name=None, std_id=None):
		path = "./" + str(std_name) + "_" + str(std_id) + "_hw4.txt"

		with open(path, mode='w', encoding="UTF-8-sig", errors="ignore") as out:
			for i in answer_data[0]:
				out.write(str(i)[:6]+' ')
				
		print("\nSave the result file : {0}".format(path))

		return
#   *** Do not modify the code ***