#!/usr/bin/env python
'''
@author : Arvind A. de Menezes Pereira <arvind.pereira@gmail.com>
@date   : May 31, 2013
@summary: This is a nifty little script for fixing some of the more common
          formatting errors in our BibTex entries.

          Right now it fixes capitalization as well as author name lists. 
	  Will try to add some more capabilities as and when I get the time to.
'''
import os, sys, re
from optparse import OptionParser

parser = OptionParser()
parser.add_option( "-s", "--source-filename", dest="source_filename", help="Filetype to convert from.", metavar="SRC_FILETYPE")
parser.add_option( "-t", "--target-filename", dest="target_filename", help="Filetype to convert to.", metavar="DEST_FILETYPE" )

(options,args)=parser.parse_args()


''' Replaces Commas in the Authors list in Bibtex with 'and'
'''
def replComma(m):
	if m.group(0) == ',': return ' and'


''' Forces Capitalization of Bibtex entries such that they're capitalization
    is enforced during compilation
'''
def forceCaps(m):
	if re.match( '[A-Z]{1}[A-Z]+', m.group(0) ): 
	  return '{{%s}}'%(m.group(1))
	else: return m.group(0)

if options.source_filename and options.target_filename:
	   print options.source_filename
	   f=open( options.source_filename, 'r' )
	   lines=f.readlines()
	   f.close()
	   print lines
	   FindAuthorStr='[\s]*Author[\s]*=[\s]*\{([\w,\. ~]+)\},'

	   f2=open( options.target_filename, 'w' )
	   for line in lines:
		m=re.match(FindAuthorStr,line)
		# Try to maintain capitalizations
		for m2 in re.finditer('[^{]{2}([A-Z]{1}[A-Z]+)[^}]{2}',line):
		   print 'Found All Caps: %02d-%02d: %s'%(m2.start(), m2.end(), m2.group(0))
		   mCaps = re.sub('([A-Z]{1}[A-Z]+)',forceCaps,line)
		   print 'PreForceCaps:%s, PostForceCaps:%s'%(line,mCaps)
		   line = mCaps

		if m:
		    preSubst = m.group(1)
		    print 'Matched: %s'%(preSubst)
		    postSubst= re.sub('[,]*,',replComma,preSubst)
		    print 'After Subst: %s\n'%(postSubst)
		    f2.write('Author = {%s},\n'%(postSubst)) 
		else:
	 	  f2.write(line)
		  pass #print 'Did not match: %s'%(line)
           f2.close()
else:
	print parser.format_help()
