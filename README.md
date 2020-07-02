科大讯飞语音合成web API老成的demo
=========

本项目基于官方的语音合成[demo（python3）](http://xfyun-doc.ufile.ucloud.com.cn/1587968076405500/tts_ws_python3_demo.zip)

github如果很慢，试一下鹅厂的coding.net代码托管
https://caiwuziyou.coding.net/public/sophisticated_xf_tts_webapi/sophisticated_xf_tts_webapi/git/files

提供了以下功能：
- 长文本（>=2000字）自动拼接
- 参数全部配置文件化，不用改一行代码，方便使用
- 断句换气时间可配置，默认1秒

官方的语音合成web API有一个坑，就是不能转超过2000字的文字，在朗读场景和短视频配音场景使用非常不便，

针对这个痛点，我根据每天的免费调用量有500次，制作了一个多次调用，然后合并mp3音频的demo，极大地方便了使用，

此外，没有换气的配音太像机器人，所以我增加了断句换气的参数，默认1秒，根据需要调整

欢迎大家下载使用并提出您宝贵的意见

使用说明:
--------

1. pip install -r requirements.txt
2. 把你的`科大讯飞web API控制台-语音合成应用`的`APPID`, `APIKey`, `APISecret`填入config.yaml
3. 把要转换的文本文件放到`inputs`文件夹中，修改config.yaml文件中的`text_path`为你的文本文件路径
4. 执行语音合成脚本，调用web API

win:

    ./run.bat

linux:

    ./run.sh

5. 输出在outputs文件夹下

