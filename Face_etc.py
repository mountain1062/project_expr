import random
import urllib.request
from bs4 import BeautifulSoup
import os
import sys
import requests
import webbrowser
import cv2

Celeb_name = ['강호동','유재석','신동엽','전현무','이병헌','하정우']
#Celeb_name = ['신동엽']

##크롤링 주소##
#url ="https://ko.wikipedia.org/wiki/"
url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query="
name_tmp = random.choice(Celeb_name)
make_url = url + name_tmp
local_img_src = name_tmp+'.jpg'

html = requests.get(make_url)
source = html.text

soup = BeautifulSoup(source,'html.parser')

#attr = {'class':'infobox vcard'}
attr = {'class':'big_thumb'}
#img_src = soup.find('table',attrs=attr).find_all('img')
img_src = soup.find('div',attrs=attr).find_all('img')

#이미지 소스 추출 및 다운로드
for img in img_src:
    src_tmp = img.get('src')
    save_path = "C:/skill/"#이미지 저장 경로
    img_name = name_tmp+'.png'
    urllib.request.urlretrieve(src_tmp,save_path+img_name)
    #print(src_tmp)

#얼굴인식 api
client_id = "vNEwGyCthoBIMnBiKi2m"
client_secret = "IQw1fuTEFc"
url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
files = {'image': open("C:/skill/"+name_tmp+'.png', 'rb')}#사진 파일 경로 지정
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
if(rescode==200):
    print(name_tmp)
    print (response.text)
else:
    print("Error Code:" + rescode)



