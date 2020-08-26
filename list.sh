#!/bin/bash
rootdir=/home/tor/rsc/math-foundation
dlist[0]=algebra/ebook
dlist[1]=calculus/ebook
dlist[2]=optim/ebook
dlist[3]=stat-prop/ebook
dlist[4]=stat-prop/ecourse
dlist[5]=talk/etalk
dlist[6]=zmisc/ebook

for dir in "${dlist[@]}"
do
    echo '>>> listing: '$dir
    ls -1 -R $rootdir/$dir > $rootdir/$dir/LIST.txt
done

