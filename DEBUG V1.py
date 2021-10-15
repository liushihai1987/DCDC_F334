#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from ftplib import FTP
import os,sys
import configparser
#打开FTP，用于检测是否存在规格书等文件
#DFAD

config = configparser.ConfigParser()
config.read('cfg.ini')
section="ftp"
FTP_IP=config.get(section,"IP")
FTP_PORT=config.get(section,"Port")
FTP_User=config.get(section,"User")
FTP_PSW=config.get(section,"PSW")

ftp=FTP()
print("调试2")
ftp.connect(FTP_IP,int(FTP_PORT))
ftp.login(FTP_User,FTP_PSW) #"Adminitrator","\'"
#ftp.cwd( '/datasheets' )
dataname=ftp.nlst()
ftp.quit()
