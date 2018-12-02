#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Filename: md2pdf.py
# Created Date: Sunday, December 2nd 2018, 6:36:57 pm
# Author: Aero
# Usage: 
#        
#        
# -----
# Last Modified: Sun Dec 02 2018
# Modified By: Aero
# ----------------------------
# --->
# HISTORY:
# Date      	By   	Comments
# ----------	-----	----------------------------------------------------------
###


import os,sys

if __name__ == "__main__":
    str_filename_full = sys.argv[1]
    if '.md' not in str_filename_full:
        print "Invalid file type"
    else:
        str_filename = str_filename_full.strip('.md')
        str_cmd = "pandoc " + str_filename_full + " -o " + str_filename + ".pdf" + " --pdf-engine=xelatex --template=/home/aero/pandoc/template.latex"
        os.system(str_cmd)
    pass