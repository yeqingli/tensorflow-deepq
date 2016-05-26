#!/bin/bash

# stop script on error and print it
set -e
# inform me of undefined variables
set -u
# handle cascading failures well
set -o pipefail

SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )


images_directory=${1:-}
if [[ -z "$images_directory" ]]
then
    echo "Usage $0 images_directory"
    exit 1
fi

for img in $images_directory/*.svg
do
    if [ ! -f $img.png ]; then
        echo "Converting $img."
        inkscape -z -e $img.png -b white $img
    fi
done
if [ "$(uname)" == "Darwin" ]; then
    # Do something under Mac OS X platform        
    echo "You will need gsort to run this script properly. Try 'brew install coreutils'"
    convert -delay 3 -loop 0 $(ls $images_directory/*.png | gsort -V ) animation.gif
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    # Do something under GNU/Linux platform
    convert -delay 3 -loop 0 $(ls $images_directory/*.png | sort -V) animation.gif
fi
