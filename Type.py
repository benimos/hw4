# -*- coding: UTF-8 -*-
#参照されている数を入力
number = input('Enter number : ')

referCntList = []
referredCntList = []
manyReferredList = []
TerminalCheckList = []
TerminalCheckListTmp = []
manyReferredListTmp = []

#referCnt.txtから参照した回数を取得
for line in open('referCnt.txt', 'r'):
	referList = line[:-1].split('\t')
	referCntList.append(int(referList[1]))

#referredCnt.txtから参照された回数を取得
for line in open('referredCnt.txt', 'r'):
	referredList = line[:-1].split('\t')
	referredCntList.append([int(referredList[0]),int(referredList[1])])
referredCntList.sort(key=lambda x:x[1], reverse=True)

#inputよりも多く参照されているものはmanyReferredListへ
for i in range(len(referredCntList)-1):
	if int(referredCntList[i][1]) >= int(number):
		manyReferredList.append([int(referredCntList[i][0]),int(referredCntList[i][1])])
		
#ターミナル駅型のページを検索
for i in range(30):
	TerminalCheckList.append([referredCntList[i][0],(referCntList[i] + referredCntList[i][1])])
TerminalCheckList.sort(key=lambda x:x[1], reverse=True)

#先頭からとってきて、pageListからページの名前撮ってくる！
for line in open('pages.txt', 'r'):
	pageList = line[:-1].split('\t')
	if TerminalCheckList != []:
		for i in range(0,len(TerminalCheckList)-1):
			if int(pageList[0]) == TerminalCheckList[i][0]:
				TerminalCheckListTmp.append([pageList[1],TerminalCheckList[i][1]])
TerminalCheckListTmp.sort(key=lambda x:x[1], reverse=True)	

for line in TerminalCheckListTmp:
	print(line)


print('\n')
print("↑TerminalType ///////////////////↓FrequentryReferredType///////////////")
print('\n')
#よく引用されているページを検索
for line in open('pages.txt', 'r'):
	pageList = line[:-1].split('\t')
	if manyReferredList != []:
		for i in range(0,len(manyReferredList)-1):
			if int(pageList[0]) == manyReferredList[i][0]:
				manyReferredListTmp.append([pageList[1],manyReferredList[i][1]])
manyReferredListTmp.sort(key=lambda x:x[1], reverse=True)	

for line in manyReferredListTmp:
	print(line)	

