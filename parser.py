import requests
from bs4 import BeautifulSoup

import os
import json
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'tasteHouse_Choice.settings')

import django

django.setup()

from house.models import Houses


def parse_house():
    store_title = []
    store_category = []
    store_img = []
    store_price = []
    store_tags = []
    store_Review = []
    store_address = []

    store_result = []

    page_num = 21
    x = 0
    while True:
        url = 'https://m.store.naver.com/sogum/api/businesses?filterId=r13130&page=1&query=%EA%B5%B0%EC%82%B0%EB%A7%9B%EC%A7%91&x=126.9783880&y=37.5666100&start={0}&display=10&deviceType=mobile'.format(
            page_num)

        json_string = requests.get(url).text
        json_request = requests.get(url).status_code

        if json_request == 500:
            break

        data_list = json.loads(json_string)

        for data in data_list['items']:

            store_title.append(data['name'])

            store_category.append(data['category'])

            if 'imageSrc' in data:
                store_img.append(data['imageSrc'])
            else:
                store_img.append(None)

            if 'tags' in data:
                #            print(data['tags'])
                store_tags.append(data['tags'])
            else:
                store_tags.append(None)

            if 'priceCategory' in data:
                store_price.append(data['priceCategory'])
            else:
                store_price.append(None)

            if 'microReview' in data:
                store_Review.append(data['microReview'])
            else:
                store_Review.append(None)

            if 'roadAddr' in data:
                store_address.append(data['roadAddr'])
            else:
                store_address.append(None)

            # 모든결과 저장
            # store_result.append([data['name'],data['category'],data['imageSrc'],data['tags'],data['priceCategory'],data['microReview'],data['roadAddr'],])
            store_result.append([store_title[x], store_category[x],store_img[x],store_Review[x],store_price[x],store_address[x],store_tags[x]])
            x += 1

        page_num += 10

        time.sleep(2)

    return store_result

if __name__ == '__main__':
    house_list = parse_house()
    for t,c,i,r,p,a,g in house_list:
        Houses(store_title=t,store_category=c,store_review=r,store_price=p,store_address=a,store_tags=g,store_img=i).save()

