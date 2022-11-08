# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup 
import lxml
import requests
import json 
import datetime

 
video_info = { 'title':'', 'video_link':'', 'img_link':'', 'play_time':'', 'hits' : '', 'updated_time':'', 'description':'', 'reg_time':'' } 


def get_video_link(target_url): 
	response = requests.get(target_url) 
	soup = BeautifulSoup(response.text, "lxml") 
	lis = soup.find_all('li', {'class' : 'channels-content-item yt-shelf-grid-item'}) 

	for li in lis : 
		title = li.find('a', {'title' : True})['title'] 
		video_link = 'https://www.youtube.com' + li.find('a', {'href' : True})['href'] 
		img_link = li.find('img', {'src' : True})['src'] 

		#<span class="video-time" aria-hidden="true"><span aria-label="8분, 55초">8:55</span></span>		
		play_time = li.find('span', {'class' : 'video-time'}).text 

		#<ul class="yt-lockup-meta-info"><li>조회수 2,902,617회</li><li>6개월 전</li></ul>
		hits = li.find_all('li')[2].text 
		updated_time = li.find_all('li')[3].text 
		video_info = { 
			'title' : title, 
			'video_link' : video_link, 
			'img_link' : img_link, 
			'play_time' : play_time, 
			'hits' : hits, 
			'updated_time' : updated_time 
		}
		print(video_info)

	return video_info 



def get_hot_video_info(target_url): 
	response = requests.get(target_url) 
	soup = BeautifulSoup(response.text, "lxml") 
	lis = soup.find_all('li', {'class' : 'expanded-shelf-content-item-wrapper'}) 

	for li in lis : 
		# exception
		try : 
			title = li.find('a', {'title' : True})['title'] 
			video_link = 'https://www.youtube.com' + li.find('a', {'href' : True})['href'] 
			img_info = li.find('img', {'data-thumb' : True})

			if img_info != None :
				img_link = img_info['data-thumb'] 

			else : 
				img_link = li.find('img', {'src' : True})['src'] 
                

			#<span class="video-time" aria-hidden="true"><span aria-label="8분, 55초">8:55</span></span>		

			#play_time = li.find('span', {'class' : 'video-time'}).text 

			play_time_info = li.find('span', {'class' : 'video-time'})

			if play_time_info != None :
				play_time = play_time_info.text

			else :
				play_time = None

			#<ul class="yt-lockup-meta-info"><li>조회수 2,902,617회</li><li>6개월 전</li></ul>
			hits = li.find_all('li')[3].text 
			updated_time = li.find_all('li')[2].text 
			description_info = li.find('div',{'class':True, 'class':'yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2'})

			if description_info != None :
				description = description_info.text

			else :
				description = None

			now = datetime.datetime.now()
			video_info = { 
				'title' : title, 
				'video_link' : video_link, 
				'img_link' : img_link, 
				'play_time' : play_time, 
				'hits' : hits, 
				'updated_time' : updated_time,
				'description' : description,
				'reg_time' : now.strftime('%Y-%m-%d %H:%M:%S')
			}

			print(video_info) 


		except BaseException as e : 
			print(e)
	return video_info 



target_url = 'https://www.youtube.com/user/CJENMMUSIC/videos' 
target_url2 = 'https://www.youtube.com/feed/trending'

# 특정 채널

#get_video_link(target_url)
# 인기 리스트

get_hot_video_info(target_url2)