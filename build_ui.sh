#!/bin/bash
#
# generate python files based on the designer ui files. pyuic5 and pyrcc5
# should be on the path.
#

set -e

if [ ! -d "ui" ]
then
    echo "Please run this from the project root"
    exit
fi

mkdir -p sonar/forms

for i in ui/*.ui
do
    base=$(basename $i .ui)
    py="sonar/forms/${base}.py"
    if [ $i -nt $py ]; then
        echo " * "$py
        pyuic5 --from-imports $i -o $py
    fi
done
