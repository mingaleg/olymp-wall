#!/usr/bin/bash
# vim: set sw=4 sts=4 et tw=80 :

DIR=gens

ID=$1
SURNAME=$2
NAME=$3
GRAD=$4

python region.py "$ID" "$SURNAME" "$NAME" "$GRAD" > $DIR/$ID.txt

convert  -background black -fill white -font Terminus.ttf -pointsize 7 \
label:@$DIR/$ID.txt -crop 1280x1024+0+0 -alpha copy $DIR/$ID.png

composite -compose Dst_In $DIR/$ID.png back.png $DIR/$ID.png

convert $DIR/$ID.png -alpha off $DIR/$ID.png

rm $DIR/$ID.txt
