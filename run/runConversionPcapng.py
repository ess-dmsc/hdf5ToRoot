#!/usr/bin/python
import os
import subprocess
import re
import sys
	
try:	
	args = ['../build/convertFile', '-f', 'example.pcapng', '-vmm', '[[1,0,2,0],[1,0,2,1],[1,0,2,2],[1,0,2,3],[1,1,2,6],[1,1,2,7],[1,1,2,8],[1,1,2,9]]',
'-axis', '[[1,0],0],[[1,1],0]', '-bc', '40', '-tac', '60', '-th','0', '-cs','1', '-ccs', '3', '-dt', '200', '-mst', '1', '-spc', '500', '-dp', '200', '-coin', 'center-of-masss', '-crl', '0.2', '-cru', '10', '-save', '111', '-json','0', '-algo', '0', '-info', 'EXAMPLE']	
	subprocess.call(args)


except OSError:
	pass




