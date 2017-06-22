# -*- coding: UTF-8 -*-
ALL_PAGES = 1483277
ALL_LINKS = 52973671

#ページ数サイズのリスト
referCntList = [0 for i in range(ALL_PAGES)]

#links.txtから参照元のみを取得してカウント
for line in open('links.txt', 'r'):
	referList = line[:-1].split('\t')
	i = referList[0]
	referCntList[int(i)-1] += 1

#referredCnt.txtというファイルに参照元が何ページにリンク飛ばしているかを書き込む
f = open('referCnt.txt', 'w')
cnt = 1
for i in referCntList:
	f.write(str(cnt))
	f.write('\t')
	f.write(str(i))
	f.write('\n')
	cnt += 1
f.close()