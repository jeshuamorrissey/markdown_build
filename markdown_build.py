#!/usr/bin/python

import os
import commands
import argparse

# some default values
MARKDOWN_DIR = os.path.join('/home', commands.getoutput('whoami').strip(), '.markdown')
DEFAULT_OUTPUT = 'out.html'
DEFAULT_HEADER = os.path.join(MARKDOWN_DIR, 'content', 'markdown.header.html')
DEFAULT_FOOTER = os.path.join(MARKDOWN_DIR, 'content', 'markdown.footer.html')
TEMP_FILE = os.path.join('/tmp', 'md.tmp')

## register the arguments we take ##
# top-level description
_description_ = 'Convert a markdown file to an HTML file, adding syntax highlighting and a header/footer.'
parser = argparse.ArgumentParser(description=_description_)

# required arguments
parser.add_argument('markdown_file', metavar='MARKDOWN_FILE', type=str, nargs='+',
					help='A string filename of the markdown file to parse.')

# optional arguments
parser.add_argument('-o', nargs=1, metavar='HTML_FILE', default=['out.html'], dest='html_file',
					help='A string filename of the output HTML file.')

# flags
parser.add_argument('-v', action='store_const', const=True, default=False, dest='verbose',
					help='If this flag is present, the proram will run in verbose mode.')

# parse the args!
args = parser.parse_args()

html_file = args.html_file[0]
header = DEFAULT_HEADER
footer = DEFAULT_FOOTER
markdown_file = args.markdown_file
verbose = args.verbose

# add header to output file
outfile = open(html_file, 'w')
outfile.write(open(header, 'rU').read().replace('$MARKDOWN_BUILD_DIR', MARKDOWN_DIR))
outfile.close()

# build output file
for in_file in markdown_file:
	if not in_file.endswith('.md'):
		if verbose: print "Ignoring non-markdown file '%s'..." % in_file
		continue

	# check for non-existant file
	if not os.path.exists(in_file):
		if verbose: print "Error: file '%s' doesn't exist!" % in_file
		continue

	if verbose: print "Generating markdown for '%s'..." % in_file,
	os.system('markdown %s >> %s' % (in_file, html_file))
	if verbose: print 'Done!'

# add footer to output file
outfile = open(html_file, 'a')
outfile.write(open(footer, 'rU').read().replace('$MARKDOWN_BUILD_DIR', MARKDOWN_DIR))
outfile.close()

if verbose: print 'Cleaning up...',
os.system('rm -rf %s' % TEMP_FILE)
if verbose: print 'Done!'

