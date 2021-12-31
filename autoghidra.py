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
def exe2asm():
    #執行Headless Analyzer指令
    cmd =['./analyzeHeadless','/Users/upload','test1104','-postScript','/Users/upload/ghidra2asm.py','/Users/upload/txt/','-import','/Users/upload/danger/*.danger','-deleteProject']
    #cmd =['./analyzeHeadless','/path/專案存取位置','專案名稱','-postScript','/腳本位置/ghidra2asm.py','/path/腳本轉換後的資料路徑/','-import','/path/欲處理資料路徑/*.danger','-deleteProject']
    #指定到Ghidra路徑
    os.chdir('/Users/ghidra_10.0.4_PUBLIC/support/')
    print(os.getcwd())
    subprocess.Popen(cmd)

if __name__ == '__main__':
    exe2asm()
