#!/bin/bash
set -e
origdir="./original"
shopt -s extglob nullglob

if [ ! -d "$origdir" ];
then
  echo "Creating $origdir directory."
  mkdir "$origdir"
fi

for vid in *.mkv; do 
  noext="${vid%.mkv}"   
  ffmpeg -i "$vid" -c:v dnxhd -profile:v dnxhr_lb -pix_fmt yuv422p -c:a pcm_s16le "${noext// /_}.mov"
    mv "$vid" "$origdir"
done

for vid in *.mp4; do 
  noext="${vid%.mp4}"   
  ffmpeg -i "$vid" -c:v dnxhd -profile:v dnxhr_lb -pix_fmt yuv422p -c:a pcm_s16le "${noext// /_}.mov"
    mv "$vid" "$origdir"
done
