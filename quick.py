
# Usefull Python Functions

# 1.0 ----Read---- 

f = open('/home/aaa/py_tools/stopwords.txt', 'r')
result = list()  
for line in f.readlines():
    print line
    result.append(line)

f.close()   
print result
texts_tokenized = [[word.lower() for word in word_tokenize(document.decode('utf-8'))] for document in courses]

# 2.0 ---- python利用jieba分词进行分词，去停止词（停用词）----
 
#coding:utf-8
 
import jieba,csv
fenci=open(r'fenci_ddc.csv','w')  #数据写入到fenci_key里
stopkey=[line.strip().decode('utf-8') for line in open('/home/aaa/py_tools/stopwords.txt').readlines()]  
	#读取停止词文件并保存到列表stopkey
key=csv.reader(file('key_ddc.csv','rb'))  #读取需要处理的词库：key_ddc.csv
list1=[]
i=0
for keys in key:
	if i==0:	
		i=1
		jiebas=jieba.cut_for_search(keys[0]) #jieba.cut_for_search() 结巴分词搜索引擎模式		
		fenci_key="/".join(list(set(jiebas)-set(stopkey))) #使用join链接字符串输出
		list1.append(fenci_key.strip())  #将数据添加到list1列表
		print u'程序处理中，请等待...'
	else:
		jiebas=jieba.cut_for_search(keys[0]) 
		fenci_key="/".join(list(set(jiebas)-set(stopkey))) 
		list1.append(fenci_key.strip()) 

zidian={}.fromkeys(list1).keys()    #字典去重的方法
for zd  in zidian:
	try:
		print zd
	except:
		pass
	fenci.writelines(zd.encode('utf-8'))      #需要转换成utf-8格式输出
	fenci.writelines('\n')
fenci.close()

# 3.0 ---- 计算文章权重TF-IDF ----
 
#coding:utf-8
import jieba
import jieba.analyse    #计算tf-idf需要调用此模块jieba.analyse
stopkey=[line.strip().decode('utf-8') for line in open('stopkey.txt').readlines()] 
#将停止词文件保存到列表stopkey，停止词在网上下载的。
neirong = open(r"ceshi1.txt","r").read()  #导入需要计算的内容
zidian={}
fenci=jieba.cut_for_search(neirong)   #搜索引擎模式分词
for fc in fenci:
        if fc in zidian:                
                zidian[fc]+=1           #字典中如果存在键，键值加1，
        else:
                zidian.setdefault(fc,1)   #字典中如果不存在键，就加入键，键值设置为1
quanzhong=jieba.analyse.extract_tags(neirong,topK=20)       #计算tf-idf，输出前20的权重词。
for qg in quanzhong:
        if qg in stopkey:       #如果qg存在停止词stopkey里面，则pass
                pass
        else:                                        #不存在的话就输出qg和出现qg的次数
                print qg+","+`zidian[qg]`       #输出权重词和权重词出现的次数


# 4.0 ---- python jieba实现关键词提取 ----
## http://blog.csdn.net/lsj19910408/article/details/40969791

 

 



