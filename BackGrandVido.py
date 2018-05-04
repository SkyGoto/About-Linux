#!/usr/bin/env python3.6
import os
import sys
import argparse

def init(shellList , parse) : # OK 
	defaultPath = "/home/skyhuman/Backvideo"   # /home/skyhuman/Backvideo/bilibi_Cheers.mp4
	defaultShell = "xwinwrap -ni -fs -s -sp -st -b -nf -- mplayer -wid WID -quiet -loop 0 "
	nohupPath = "/home/skyhuman/temp/myout.file"
	shellList.insert(0,defaultShell)
	shellList.insert(1,defaultPath)
	shellList.insert(2,nohupPath)
	lines = [""]
	if IsExist(os.getcwd() + "/dePath.def") == 1 :
		f = open(os.getcwd() + "/dePath.def" , 'r')  # to absolute path
		lines = f.readlines() 
		shellList[1] = lines[0]
		f.close()
	parse.add_argument("-g" , dest = 'resize' , 
	help = 'Resize the video and coordinate eg : 1920 1080 0 0 ' , 
	nargs = 4 ,      
	type = int)
	parse.add_argument("-ni" , dest = 'ignore' , 
		help = 'ignore the input ' , 
		action = 'store_const' ,
		 const = '-ni' )
	parse.add_argument("-d" ,  dest = 'desktopCracked' , 
		help = 'Desktop window crack   -argb - RGB ' , 
		action = 'store_const' ,
		const = '-d')
	parse.add_argument("-fs" , dest = 'fullScreen' ,
		help = 'full screen' , 
		action = 'store_const' , 
		const = '-fs')
	parse.add_argument("-s" , dest = 'sticky' ,
		help = 'sticky ' ,
		action = 'store_const' ,
		const = '-s')
	parse.add_argument("-st" , dest = 'skipTaskbar' , 
		help = 'Skip the taskbar' ,
		action = 'store_const' ,
		const = '-st')
	parse.add_argument("-sp" , dest = 'skipSearch' , 
		help = 'Skip the search' , 
		action = 'store_const' , 
		const = '-sp')
	parse.add_argument("-a" , dest = 'top' , 
		help = 'Video stick to the top' , 
		action = 'store_const' , 
		const = '-a')
	parse.add_argument("-b" , dest = 'bottom' , 
		help = 'Set at the end' , 
		action = 'store_const' , 
		const = '-b')
	parse.add_argument("-nf" , dest = 'noFocus' , 
		help = 'No focus' , 
		action = 'store_const' , 
		const = '-nf')
	parse.add_argument("-o" , dest = 'Opacity' , 
		help = 'Screen opacity' , 
		type = float)
	parse.add_argument("-sh" , dest = 'windows' , 
		help = 'Window shape (rectangle , round or triangular )' , 
		type = str)
	parse.add_argument("-debug" , dest = 'debug' , 
		help = 'open debug information' , 
		action = 'store_const' , 
		const = '-debug')
	parse.add_argument("-vid" , dest = 'vidSelect' ,
		help = "Select player (default mplayer)" , 
		nargs = '*')
	parse.add_argument("-sy" , dest = 'synopsis' , 
		help = 'Front desk (If not need play details)' , 
		action = 'store_const' , 
		const = '-quiet')
	parse.add_argument("-loop" , dest = 'loopTimes' , 
		help = 'loop times' , 
		type = int )
	parse.add_argument("-m" , dest = 'mute' , 
		help = 'Mute play' , 
		action = 'store_const' , 
		const = '-ac mute')
	parse.add_argument("-list" , dest = 'listPlay' , 
		help = 'List play (need video folder )' , 
		type = str)
	parse.add_argument("-py" , dest = 'playWay' , 
		help = 'Play mode(need video list)', 
		type = str)
	parse.add_argument("-cd" , dest = 'changeDir' , 
		help = 'change default path' , 
		type = str)
	parse.add_argument("-restart", dest = 'restart' ,
		help = 'restart ' , 
		action = 'store_const' , 
		const = 'restart')
	parse.add_argument("-def",dest = 'default' ,
		help = 'default set' ,
		action = 'store_const' , 
		const = 'default')
	parse.add_argument("-stop",dest = 'stop' , 
		help = 'stop the soft' , 
		action = 'store_const' , 
		const = 'stop')
	args = parse.parse_args()
	return args  


def inputPath(shellList):  # make sure the video path   NOT NEED
	print ("input video path (default press Enter) :\n")
	getPath = input()
	if getPath != "" :
		os.path.exists(getPath)   #judge path is Available
		shellList.insert(1,getPath)

def softShell(shellList): # get soft operational  NOT NEED 
	print ("input operational (default press Enter) :")
	getShell = input()
	if getShell != "" :
		shellList.insert(0,'xwinwrap' + getShell )

def runSoft(args,shellList):
	shellStr = ""
	'''if args.resize :
		shellStr = shellStr + " -g " + args.resize[0] + " " + 
		args.resize[1] + " "  + args.resize[2] + " " + args.resize[3] 
	'''
	if args.default :
		if (IsExist(shellList[1]) == 2) :
			List = makeRandList(shellList[1])
			shellStr = ("xwinwrap -ni -fs -s -sp -st -b -nf -- mplayer -wid WID -quiet  -loop 0 -shuffle -playlist "+ List +" ")
		elif (IsExist(shellList[1]) == 1) :
			shellStr = 'xwinwrap -ni -fs -s -sp -st -b -nf -- mplayer -wid WID -quiet -loop 0' + shellList[1]
	if args.mute : 
		shellStr = shellStr + " -ac mute 0 "
	#print ("nohup "+ shellStr + " > " + shellList[2] + " 2>&1 &")
	#print ("Path is " + shellList[1] )
	if args.debug :
		print (shellStr)
	#print("nohup " + shellStr + " > " + shellList[2] + " 2>&1 &")
	os.system("nohup "+ shellStr + " > " + shellList[2] + " 2>&1 &")

def softStatus() :  # OK 
	softExist = os.popen ('ps -ef | grep "xwinwrap" | grep -v grep | awk \'{print $2}\' ').read()
	if softExist != '' :
		return 1 
	else :
		return 0

def killSoft():  # OK 
	#os.system("pkill -15 mplayer")
	os.system("pkill -15 xwinwrap")   # kill mplayer ?
 
def makeRandList(path) :  # OK 
	fp = open("/home/skyhuman/temp"+"/video.lst",'w')   #  fp = open(path+"/video.lst",'w')
	for root,div,files in os.walk(path) :
		for name in files :
			fp.write(os.path.join(root,name) + "\n")
	fp.close()
	return "/home/skyhuman/temp/video.lst"

def distoryFiles(Path) :  #OK  # delete created the files  # paly list , play log 
	if  IsExist(os.getcwd() + "/dePath.def") == 1 :
		os.remove(os.getcwd() + "/dePath.def")
	if IsExist("/home/skyhuman/temp"+"/video.lst") == 1 :
		os.remove("/home/skyhuman/temp"+"/video.lst")
	if IsExist(Path[2]) == 1 :
		os.remove(Path[2])


def IsExist(Path) :
	Path = Path.rstrip()
	if os.path.exists(Path) :
		if os.path.isfile(Path) :
			return 1 
		elif os.path.isdir(Path) :
			return 2 
		else :
			return 0
	else :
		return -1

def main() :
	shellList = []
	parse = argparse.ArgumentParser()
	args = init(shellList,parse)
	#if isinstance(args , int ) :
	#	return 0 
	status = softStatus()   # stop soft 
	if status == 1 :
		if args.stop : 
			killSoft() 
			distoryFiles(shellList)
			#if args.restart : 
				#statusPath = IsExist(shellList[1])
				#if statusPath > 0 :
				#	runSoft(args,shellList)		
		if args.restart :
			killSoft() 
			distoryFiles(shellList)
			statusPath = IsExist(shellList[1])
			if statusPath > 0 :
				runSoft(args,shellList)		

	else : # start the soft 
		distoryFiles(shellList)
		statusPath = IsExist(shellList[1])
		if statusPath > 0 :
			runSoft(args,shellList)
			#os.system("nohup xwinwrap -ni -fs -s -sp -st -b -nf -- mplayer -wid WID -quiet  -loop 0 -shuffle -playlist /home/skyhuman/temp/video.lst  -ac mute 0  > /home/skyhuman/temp/myout.file 2>&1 &")
		else :
			print("Error to exit")
			return -1




if __name__ == '__main__':
	main()
	#os.system("nohup xwinwrap -ni -fs -s -sp -st -b -nf -- mplayer -wid WID -quiet  -loop 0 -shuffle -playlist /home/skyhuman/temp/video.lst  -ac mute 0  > /home/skyhuman/temp/myout.file 2>&1 &")
