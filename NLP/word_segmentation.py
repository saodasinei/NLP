import jieba
import jieba.analyse

f = open('wenan', 'r')
content = f.read()

# 分词
# 精准分词
# seg_list = jieba.cut(content)
# print("Default Model:" + "/".join(seg_list))

# 全模式
# seg_list = jieba.cut(content, cut_all=True)
# print("Full Model:" + "/".join(seg_list))

# 搜索引擎分词
# seg_list = jieba.cut_for_search(content)
# print(",".join(seg_list))

# paddle模式
# import jieba
#
# jieba.enable_paddle()  # 启动paddle模式。 0.40版之后开始支持，早期版本不支持
# strs = ["我来到北京清华大学", "乒乓球拍卖完了", "中国科学技术大学"]
# for str in strs:
#     seg_list = jieba.cut(str, use_paddle=True)  # 使用paddle模式
#     print("Paddle Mode: " + '/'.join(list(seg_list)))

tags = jieba.analyse.extract_tags(content, topK=20, withWeight=False, allowPOS=())
