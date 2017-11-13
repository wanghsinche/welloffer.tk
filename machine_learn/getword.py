# -*- coding: utf-8 -*-
import re
txtfile = open('data.txt','r')
txtlist = txtfile.readlines()
txt = ''
txt = txt.join(txtlist)

reg = re.compile(ur'[\u4e00-\u9fff]+', re.M)
matchobj = re.findall(reg, txt.decode('UTF-8'))
print ', '.join(matchobj).encode('UTF-8')