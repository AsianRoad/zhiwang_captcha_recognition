# zhiwang_captcha_recognition
识别中国知网的验证码
参考 问题 https://www.zhihu.com/question/33321954?sort=created 下Jayson的回答

get_captcha 下载验证码图片作处理样本及结果测试
去噪,切割并生成样本;对比图片的相似度进行识别

知网验证码特点，仅含偶数数字和偶数位的英文字母:0,2,4,6,8,B,D,F,H...
识别率在70%以上..
