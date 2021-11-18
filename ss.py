# Press the green button in the gutter to run the script.
from datetime import datetime
from time import sleep

import pygame
import requests
from bs4 import BeautifulSoup

pygame.init()

audio_volume = 0.5

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
url_ss = 'https://brand.naver.com/applestore/shoppingstory/detail?id=2002372618'

sound1 = pygame.mixer.Sound('alarmaudio/3.wav')
sound2 = pygame.mixer.Sound('alarmaudio/4.wav')
sound1.set_volume(audio_volume)
sound2.set_volume(audio_volume)


def _check_ss(href, sound):
    prod = soup.find('a', attrs={'href': href})
    prod = prod.parent
    out_of_stock = prod.text.find('일시품절')
    now = datetime.now()
    print(now, ' : ', out_of_stock)
    if out_of_stock is None:
        sound.play()


if __name__ == '__main__':
    while True:
        sleep(5)

        # 쇼핑스토리
        res = requests.get(url_ss, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        # 프로 16 스그
        href = "/applestore/products/5988228765"
        _check_ss(href, sound1)

        # 프로 16 실버
        href = "/applestore/products/5988235489"
        _check_ss(href, sound2)
