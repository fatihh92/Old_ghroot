#!/usr/bin/env python
# _*_coding:utf-8_*_

import urllib.request

say = 1
son = 5
for say in range(1,son+1):
    urllib.request.urlretrieve("https://image.slidesharecdn.com/btrisk-zararlyazlmanalizieitimi-blm2-180114204913/95/btrisk-zararl-yazlm-analizi-eitimi-sunumu-blm-2-"+str(say)+"-638.jpg?cb=1515963270","android"+str(say)+".png")
    sonuc = (100*say)/son
    print('{:05.2f}'.format(sonuc),'% tamamlandı - {} dosya indirildi'.format(say))