# WechatSnsViewer
朋友圈备份浏览工具 [👉不知道朋友圈备份文件哪来？](https://mp.weixin.qq.com/s?__biz=Mzg4MDExMTUwMw==&mid=2247483679&idx=1&sn=12f73bf7f92f94b12ec057e64913b0f8&chksm=cf7b7bfff80cf2e9afa369117e5da5733854f4823e70dddce64a5537a7de3c24bb1b121727cb&token=1469653834&lang=zh_CN#rd)

## 需要的工具
- python3.x

## 使用说明
1. 克隆代码到本地
```
git clone git@github.com:coolzilj/WechatSnsViewer.git
```

2. 解压邮件接收到的备份压缩包到 `WechatSnsViewer` 目录下，并把解压后的目录更改为 `datas`，这时候 `WechatSnsViewer` 目录结构如下：
```
- assets
- outputs
- datas
 - xxx图片
 - xxx图片
 - ......
 - data.json
index.html
serve.sh
word.py
......
```

3. 启动服务器，然后打开 `http://localhost:3345`
```
./serve.sh
```
![](https://raw.githubusercontent.com/coolzilj/WechatSnsViewer/master/screenshots/screenshot.png)

## One More Thing
简单地做一个词频分析，生成词云

```
pip3 install jieba imageio wordcloud
python3 ./word.py
# 非 MacOS 或者提示找不到字体，请自行打开 `word.py`，找到 `font_path='/Library/Fonts/Songti.ttc'` 替换成你需要的字体目录
```

然后 `outputs` 目录下的 `word.png` 会更新
![](https://raw.githubusercontent.com/coolzilj/WechatSnsViewer/master/outputs/word.png)

## 欢迎关注我的个人公众号
![](https://raw.githubusercontent.com/coolzilj/WechatSnsViewer/master/screenshots/qrcode.png)
