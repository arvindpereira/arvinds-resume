#!/bin/bash
#
#
detailed='Arvind_Pereira_CV_Detailed.pdf'
short='Arvind_Pereira_CV.pdf'
upload='ampereir@robotics.usc.edu:/home/ampereir/public_html/'

res1=`scp ${detailed} ${upload}`
res2=`scp ${detailed} ${upload}`
