#!/bin/bash

cat rectangles | while read i; do a1=`echo $i | cut -d, -f1`; a2=`echo $i | cut -d, -f2`; python make_header.py $a1 $a2 > header_${a1}_${a2}.h; done

for i in header_*.h
do
    cd Dantz/Dantz
    ln -sf ../../$i DantzLoad.h
    make DantzLoad
    ./DantzLoad > output_$i
    cd ../..
done
