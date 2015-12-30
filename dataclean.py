#!/usr/local/bin/python

#coding:-*-utf-8-*-

#*******************************************************************************
# data_clean.py
#
# Update Similarity Clusters  
# 
# Usage: 
#     Parameters: rawdata, outdata, colindex 
# 
#                                                Author: dzn    Date: 29-11-2015
#*******************************************************************************

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import itertools
import getopt
import logging
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)

def Cleaning(inpath, outpath, cindex, rundate):
    print cindex
    outfile = open(outpath+'/'+rundate+'.txt', 'a')    
    for line in open(inpath):
        line = line.replace('\n','')
        text = line.strip().split('|')[int(cindex)]
        outfile.writelines(text.encode('utf-8')+'\n')
    outfile.close()    

def validateopts(opts):
	for option, value in opts:
		if option  in ["-h", "--help"]:
			tips()
		elif option in ["--inpath", "-i"]:
			inpath = value
		elif option in ["--outpath", "-o"]:
			outpath = value
		elif option in ["--cindex", "-c"]:
			cindex = value
		elif option in ["--rundate", "-r"]:
		    rundate = value
		elif option == "-u":
			print "usage -u"
	return inpath, outpath, cindex, rundate

def tips():
	"""Display the usage tips"""
	print "Please use: "+sys.argv[0]+" [options]"
	print "usage:%s --inpath=value --outpath=value --cindex=value --rundate=value"
	print "usage:%s -i value -o value -c value -r value"
	sys.exit(2)

def main():
	try:
		opts,args = getopt.getopt(sys.argv[1:],"hi:o:c:r:u",["inpath=","outpath=","cindex=","rundate=","help"])
	except getopt.GetoptError:
		tips()
	if len(opts) >= 4:
		inpath, outpath, cindex, rundate = validateopts(opts)
	else:
		print "ErrorMessage: Please Check What Your Input !"
		tips()
		raise SystemExit	

	if not (os.path.isfile(inpath)):
		print "ErrorMessage: Please Check Your Input files !"
		raise SystemExit

	if not (os.path.isdir(outpath)):
		print "ErrorMessage: Please Check Your Output Folder!"
		raise SystemExit
			
	print '*****************************************'
	print 'inpath    = ' + inpath
	print 'outpath   = ' + outpath
	print 'cindex    = ' + cindex
	print 'rundate   = ' + rundate	
	print '*****************************************'

	Cleaning(inpath, outpath, cindex, rundate)

if __name__ == '__main__':
	main()


             


