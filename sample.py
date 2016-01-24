# encoding=utf8
__author__ = 'wang'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# 前面设置是为了可以在文件中输入中文

import nlpirt.nlpir as nlpir

print __name__
p = "Big News: @解放日报 [最右]【呼市铁路局原副局长被判死缓 最头痛藏钱】"
for t in nlpir.Seg(p):
    s = '%s\t%s\t%s' % (t[0],t[1],nlpir.translatePOS(t[1]))
    print(s)