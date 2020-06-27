科大讯飞语音合成web API老成的demo
=========

本项目基于官方的语音合成[demo（python3）](http://xfyun-doc.ufile.ucloud.com.cn/1587968076405500/tts_ws_python3_demo.zip)
提供了以下功能：
- 长文本（>=2000字）自动拼接
- 【开发中】语速控制
- 【开发中】断句换气

使用说明:
--------

1. pip install -r requirements.txt
2. 把你的科大讯飞web API的APPID, APIKey, APISecret填入config.yaml
3. 把要转换的文字复制到text.txt中，注意用换行分句
4. 执行语音合成，调用web API

win:

    `./run.bat` 

linux:

    `./run.sh`

5. 输出在outputs文件夹下

