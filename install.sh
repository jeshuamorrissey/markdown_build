#!/bin/bash

# remove previous installation
rm -rf ~/.markdown
rm -rf /usr/lib/markdown_build

echo -n 'Copying files... '
# make markdown directory
mkdir ~/.markdown

# copy these files into it
cp -r * ~/.markdown/

echo 'Done!'


echo -n 'Making link in /usr/lib/markdown_build... '
# make link to exe in /usr/lib
link ~/.markdown/markdown_build.py /usr/lib/markdown_build
echo 'Done!'

