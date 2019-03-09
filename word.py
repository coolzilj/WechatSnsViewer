# coding: utf-8
import json
import jieba.analyse
import imageio
import sys
from wordcloud import WordCloud

import matplotlib
matplotlib.use('TkAgg')


def gen_img(texts, img_file):
    data = ' '.join(text for text in texts)
    image_coloring = imageio.imread(img_file)
    wc = WordCloud(
        background_color='white',
        mask=image_coloring,
        font_path='/Library/Fonts/Songti.ttc' # 替换成你需要的字体目录
    )
    wc.generate(data)
    wc.to_file('./outputs/word.png')
    print("成功生成词云")


if __name__ == '__main__':
    snsInfos = json.loads(open('./datas/data.json', 'r', encoding='utf-8').read())
    print('朋友圈总数：', len(snsInfos))

    words = []
    for snsInfo in snsInfos:
        words.extend(jieba.analyse.extract_tags(snsInfo['content']))
    print("总词数：", len(words))

    gen_img(words, 'assets/wechat.png')
