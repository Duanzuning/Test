#!/bin/bash

dictdir="/home/aaa/hd/corpus"
pytools="/home/aaa/py_tools"
query=恒大夺冠

${pytools}/gensim_query.py -i ${dictdir}/seedindex.txt -c ${dictdir}/seedcorpus.txt -s ${query} -n 5 > ${dictdir}/query.log



