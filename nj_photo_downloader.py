from bs4 import BeautifulSoup as bs
import requests
import os
from concurrent.futures import ThreadPoolExecutor   # 加入 concurrent.futures 內建函式庫

# input_image = input("請輸入要下載的圖片：")
 
# response = requests.get(f"https://unsplash.com/s/photos/{input_image}")

# 改這裡
star_num = 1
end_num = 65
project_tag = "supernatural"
photo_tag = "NJ_Supernatural"

end_num = end_num + 1
# number_list = ["0"+str(num) if len(str(num)) == 1 else str(num) for num in list(range(star_num,end_num))] 
number_list = [str(num) for num in list(range(star_num,end_num))] # 個位數字照片沒有帶0開頭時

# print(number_list)

img_urls = []
for num in number_list:
    photo_url = f"https://newjeans.kr/imgs/{project_tag}/photo/{photo_tag}_{num}.jpg"
    img_urls.append([photo_url, num])
target_dir = f'C:/Users/Burgess/Downloads/NJ/{project_tag}'

def download(url):                     # 編輯下載函式
    print(url)                           # 印出網址
    jpg = requests.get(url[0])           # 使用 requests.get 取得圖片資訊
    
    
    # print(os.path.exists(target_dir))
    f = open(f'{target_dir}/{photo_tag}_{url[1]}.jpg', 'wb')    # 將圖片開啟為二進位格式 ( 請自行修改存取路徑 )
    f.write(jpg.content)                 # 存取圖片
    f.close()

if os.path.exists(target_dir):
    pass
else:
    os.mkdir(target_dir)
executor = ThreadPoolExecutor()          # 建立非同步的多執行緒的啟動器
with ThreadPoolExecutor() as executor:
    executor.map(download, img_urls) 
