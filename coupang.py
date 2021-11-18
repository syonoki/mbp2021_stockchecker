# Press the green button in the gutter to run the script.
import datetime
from time import sleep

import pygame
import requests
from bs4 import BeautifulSoup

pygame.init()

audio_volume = 0.5

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
url_coupang = 'https://www.coupang.com/np/promotion/105353'
url_ss = 'https://brand.naver.com/applestore/shoppingstory/detail?id=2002372618'

sound1 = pygame.mixer.Sound('alarmaudio/1.wav')
sound2 = pygame.mixer.Sound('alarmaudio/2.wav')
sound1.set_volume(audio_volume)
sound2.set_volume(audio_volume)


def _check_coupang(data_vendor_item_id, sound):
    prod = soup.select_one(f"li[data-vendor-item-id='{data_vendor_item_id}']")
    out_of_stock = prod.find('div', class_='out-of-stock')
    now = datetime.datetime.now()
    print(now, ' : ' , out_of_stock)
    if out_of_stock is None:
        sound.play()


if __name__ == '__main__':
    while True:
        sleep(4)

        # 쿠팡
        res = requests.get(url_coupang, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        # 프로 16 스그
        data_vendor_item_id = '79005406343'
        _check_coupang(data_vendor_item_id, sound1)

        # 프로 16 실버
        data_vendor_item_id = '79005406321'
        _check_coupang(data_vendor_item_id, sound2)