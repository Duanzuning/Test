#!/bin/bash

for((i=1;i>=1;i--));do

run_date=`date +%Y-%m-%d --date="-${i} day"`
rundate=`date +%Y%m%d --date="-${i} day"` 
day=`date +%d --date="-${i} day"`
month=`date +%m --date="-${i} day"`
week_day=`date +%w --date="-${i} day"`
week_number=`date +%W --date="-${i} day"`
week=`date +%W --date="-${i} day"`

shelldir="/home/aaa/py_tools"

inpath1="/home/aaa/Templates/sina_comment_detail.txt"
#inpath2="/home/aaa/Templates/sina_comment_stats.dat"
#inpath3="/home/aaa/Templates/sina_news_detail.dat"
outpath="/home/aaa/sinanews/20151129"
rm -rf ${outpath}
mkdir ${outpath}
cindex1=0
#cindex2=3
#cindex3=7

${shelldir}/dataclean.py -i ${inpath1} -o ${outpath} -c ${cindex1} -r ${rundate} > /home/aaa/dataclean.log
#${shelldir}/dataclean.py -i ${inpath2} -o ${outpath} -c ${cindex2} -r ${rundate} >> /home/aaa/dataclean.log
#${shelldir}/dataclean.py -i ${inpath3} -o ${outpath} -c ${cindex3} -r ${rundate} >> /home/aaa/dataclean.log

#if [ $? == 0 ];then
${shelldir}/jieba_extract.py -i ${outpath} -t 500 > /home/aaa/extract.log
#fi


done



