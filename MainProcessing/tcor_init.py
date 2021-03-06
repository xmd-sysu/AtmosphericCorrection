#!/usr/bin/env python
# coding:utf-8
# cd /Volumes/Transcend/SCAN_PROGRAM3/SceneName
#	SceneName: ETM02063010832,...
# python ../PROGRAM/tcor_init.py FolderName funcName ClassName 
#	FolderName: Mar??+???_?
#		Mar : Arbitary Name such as Mar, Con, Urb, New 
#		?? : initial optical depth * 100
#		+ : for selection of class representation
#			P : Mode
#			M : Median
#		??? : initial optical depth * 100
#		? : deccelaration coeff * 10
#	funcName: function name fMar20, fCon00, ...
#	className: cls640J

import os
import os.path as path
import sys
#import numpy as np
import subprocess

fscene=os.getcwd()

os.chdir('../Utility')
cwd=os.getcwd()
sys.path.append(cwd)
import rtc_util as ut
import tcor_util as tc

os.chdir(fscene)

#----------------------------
#  Initialize
#----------------------------
print "#### Initialize ####"
# parameter input

fold=sys.argv[1]
subf,tdec=fold.split('_')
depth=float(subf[3:5])/100
nmax=int(subf[6:])
dec=float(tdec)/10.0
model=subf[5]
print 'depth:',depth
print 'dec:',dec
print 'nmax:',nmax

func_name=sys.argv[2]
cls_name=sys.argv[3]

os.chdir('DATA')
f=open(func_name[1:]+'_1.txt')
lines=f.readlines()
f.close()
n_line=len(lines)
temp=lines[n_line-5].split()[1:4]
print temp
ntau=int(temp[0])+1
nhigh=int(temp[1])+1
nsang=int(temp[2])+1
print ntau,nhigh,nsang
r_set0=lines[n_line-4].split()[2]
os.chdir('..')

if path.exists(fold) == False:
    line='mkdir '+ fold
    subprocess.call(line,shell=True)
    f=open('aparm.txt')
    lines=f.readlines()
    f.close()
    g=open(fold + '/aparm.txt','w')
    for line in lines:
        if line.find('depth =') != -1:
            line = '  depth =   ' + str(depth) +'\n'
        if line.find('dec =') != -1:
            line = '  dec =     ' + str(dec) +'\n'
        print line,
        g.write(line)
    g.write(str(ntau)+' '+str(nhigh)+' '+str(nsang)+'\n')
    g.write(r_set0+'\n')
    g.write(func_name+'\n')
    g.write(cls_name+'\n')
    g.close()
else: print '*** '+fold+' exists !!!'

exit()