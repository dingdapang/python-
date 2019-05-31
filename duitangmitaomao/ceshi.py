import requests
import os
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def download(url, filename):
    if os.path.exists(filename):
        print('file exists!')
        return
    try:
        r = requests.get(url, stream=True, timeout=60)
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
        return filename
    except KeyboardInterrupt:
        if os.path.exists(filename):
            os.remove(filename)
        raise KeyboardInterrupt
    except Exception:
        traceback.print_exc()
        if os.path.exists(filename):
            os.remove(filename)


# 创建保存目录
if os.path.exists('yugui') is False:
    os.makedirs('yugui')

# 打开浏览器
browser = webdriver.Chrome()
# 进入图片详细查看页
url = 'https://www.duitang.com/blog/?id=1005406113'
browser.get(url)

# 设置下载数量
start = 1
end = 133
for i in range(start, end + 1):
    #	定位图片
    img = browser.find_elements_by_xpath("//img[@id='mbpho-img']")
    for ele in img:
        target_url = ele.get_attribute("src")
        print(target_url)
        img_name = target_url.split('/')[-1]
        filename = os.path.join('yugui', img_name[-25:])
        download(target_url, filename)
    # 显示进度
    print('%d / %d' % (i, end))
    #   下一页
    if i - end == 0:
        break
    next_page = browser.find_element_by_class_name("shownext").click()
    time.sleep(3)

# 关闭浏览器
browser.quit()