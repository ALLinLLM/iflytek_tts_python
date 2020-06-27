科大讯飞语音合成web API老成的demo
=========

本项目基于官方的语音合成[demo（python3）](http://xfyun-doc.ufile.ucloud.com.cn/1587968076405500/tts_ws_python3_demo.zip)

提供了以下功能：
- 长文本（>=2000字）自动拼接
- 【开发中】语速控制
- 【开发中】断句换气

官方的语音合成web API有一个坑，就是不能转超过2000字的文字，在朗读场景和短视频配音场景使用非常不便，

针对这个痛点，我根据每天的免费调用量有500次，制作了一个多次调用，然后合并mp3音频的demo，极大地方便了使用，欢迎大家下载使用并提出宝贵的意见

使用说明:
--------

1. pip install -r requirements.txt
2. 把你的科大讯飞web API的APPID, APIKey, APISecret填入config.yaml
3. 把要转换的文字复制到text.txt中，注意用换行分句
4. 执行语音合成，调用web API

win:

    ./run.bat

linux:

    ./run.sh

5. 输出在outputs文件夹下

