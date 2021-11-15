#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 10:32:23 2021

@author: yilnhsieh
"""
import os
import subprocess
# import shlex
# from threading import Timer
# from subprocess import Popen, PIPE, call, STDOUT, check_output
import logging
import configparser
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileDir='/Users/yilnhsieh/csti-malware-classify/20211008/upload/'
def exe2asm():
    #執行Headless Analyzer指令
    cmd =['./analyzeHeadless','/Users/yilnhsieh/csti-malware-classify/20211008/upload','test1104','-postScript','/Users/yilnhsieh/csti-malware-classify/20211008/upload/ghidra2asm.py','/Users/yilnhsieh/csti-malware-classify/20211008/upload/txt/','-import','/Users/yilnhsieh/csti-malware-classify/20211008/upload/danger/*.danger','-deleteProject']
    #指定到Ghidra路徑
    os.chdir('/Users/yilnhsieh/csti-malware-classify/ghidra_10.0.4_PUBLIC/support/')
    print(os.getcwd())
    subprocess.Popen(cmd)

if __name__ == '__main__':
    exe2asm()
