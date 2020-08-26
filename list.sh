#!/bin/bash
rootdir=/home/tor/rsc/math-foundation
dlist[0]=algebra/ebook
dlist[1]=calculus/ebook
dlist[2]=optim/ebook
dlist[3]=stat-prob/ebook
dlist[4]=stat-prob/ecourse
dlist[5]=zmisc/etalk
dlist[6]=zmisc/ebook
dlist[7]=zmisc/ecourse

for dir in "${dlist[@]}"
do
    echo '>>> listing: '$dir
    ls -1 -R $rootdir/$dir > $rootdir/$dir/LIST.txt
done

