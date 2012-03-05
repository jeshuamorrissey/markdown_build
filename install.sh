#!/bin/bash

# remove previous installation
rm -rf ~/.markdown
sudo rm -rf /usr/bin/markdown_build

echo -n 'Copying files... '
# make markdown directory
mkdir ~/.markdown

# copy these files into it
cp -r * ~/.markdown/
echo 'Done!'

echo -n 'chmoding files... '
chmod a+rx ~/.markdown/markdown_build.py
chmod -R a+rx ~/.markdown
echo 'Done!'

echo -n 'Making link in /usr/bin/markdown_build... '
# make link to exe in /usr/bin
sudo link ~/.markdown/markdown_build.py /usr/bin/markdown_build
echo 'Done!'

