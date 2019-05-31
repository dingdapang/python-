import requests
import re
from requests.exceptions import MissingSchema

url = []
def get_page():

    url = 'https://www.duitang.com/napi/blog/list/by_search/?kw=%E8%9C%9C%E6%A1%83%E7%8C%AB&type=feed&start=0&limit=100'

    try:
        resp = requests.get(url)
        #print(url)
        if 200  == resp.status_code:
            #print(resp.json())
            return( resp.json())
    except requests.ConnectionError:
        return None


def get_images(json):

    if json.get('data'):
        data = json.get('data')
        #print(data)
        object_list = data.get('object_list')
        for list in object_list:
            image2 = list.get("photo")
            images = image2.get("path")
            save_image(images)



def save_image(url):


    response = requests.get(url)
    picture = response.content
    "https://b-ssl.duitang.com/uploads/item/201903/13/20190313105834_vtvmt.jpeg"
    abc = re.match("^http.*?_(.*?)$",str(url))
    #print("aa")
    #print(abc.group(1))
    num = abc.group(1)
    path = "d:/py/duitangmitaomao/p/"+str(num)
    with open(path, "wb") as f:
        f.write(picture)






def main():

        json = get_page()
        get_images(json)
        save_image(url)

main()