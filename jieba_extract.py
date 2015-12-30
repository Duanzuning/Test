#!/usr/local/bin/python 

#coding:-*-utf-8-*-

#******************************************************************
# jieba_extract.py
# Use jieba to extract keywords from an artical, and also return a 
# freq_weight for each keywords.
#
# Author: dzn    Date: 02-11-2015
#******************************************************************

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import shutil
import jieba.analyse
import getopt
import logging
logging.basicConfig(format='%(asctime)s:, %(levelname)s:, %(message)s', level=logging.INFO)


#Get all files's name, and save contents into a new file 
def SaveNewFile(dirname, outfile):
	files    = os.listdir(dirname)
	out_file = dirname + "/" + outfile + ".txt" 
	out      = open(out_file, 'w')					
	for name in files:
		fullname = os.path.join(dirname,name)
		if (os.path.isfile(fullname)):
			f = open(fullname)
			contents = f.read()
			out.write(contents + "\n")
			f.close()
		else:
			print ("cannot open the file %s for writing" % fullname)
			break		
	out.close()					

def GetTopK(infile, outfile, topk):
	infile  = open(infile, "r")
	outfile = open(outfile, "w")
	contents= infile.read()	
	infile.close()		
	tags = jieba.analyse.extract_tags(contents, topK = topk, withWeight = True)
	
	for tag in tags:
		outfile.write("%s, %f \n" % (tag[0], tag[1]))

	outfile.close()

def tips():
	"""Display the usage tips"""
	print "Please use: "+sys.argv[0]+" [options]"
	print "usage:%s --input=value --topk=value"
	print "usage:%s -input value -topk value"
	sys.exit(2)

def validateopts(opts):
	Topk = 20  #default value
	for option, value in opts:
		if option  in ["-h", "--help"]:
			tips()			
		elif option in ["--input", "-i"]:
			Input = value
		elif option in ["--topk", "-t"]:
			Topk  = int(value)
		elif option == "-d":
			print "usage -d"
	return Input,Topk
	
def main():

	try:
		opts,args = getopt.getopt(sys.argv[1:],"hi:t:d",["input=","topk=","help"])
	except getopt.GetoptError:
		tips()

	if len(opts) >= 1:
		dirname,topk = validateopts(opts)
	else:
		print "ErrorMessage: Please Check what's your input !"		
		raise SystemExit
		tips()

	if not os.path.isdir(dirname):
		print "ErrorMessage: Please Check your dirname !"
		raise SystemExit

	outfile = "jieba_extract"
	SaveNewFile(dirname, "_tmp_")  # extract files's keywords into a _tmp_.txt file
	infile  = dirname+"/"+"_tmp_"+".txt"
	outdir  = dirname+"/"+outfile

	if os.path.isdir(dirname+"/"+outfile):
		shutil.rmtree(dirname+"/"+outfile)

	os.mkdir(dirname+"/"+outfile)
	outfile = dirname+"/"+outfile+"/"+outfile+".txt"
	GetTopK(infile, outfile,topk)  # Get top K topics from document and save into an OUTFILE.txt
	os.remove(infile)
	
if __name__ == '__main__':
	main()
				


