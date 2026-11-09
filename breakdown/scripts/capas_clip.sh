#!/bin/bash
# $1 = carpeta, $2 = salida, resto = imagenes en orden
set -e
dir=$1; out=$2; shift 2
hold=1.6; fade=0.6
inputs=(); i=0
for f in "$@"; do inputs+=(-loop 1 -t $(echo "$hold+$fade" | bc) -framerate 25 -i "$dir/$f"); i=$((i+1)); done
n=$i
filter=""; prev="[0:v]"; off=$hold
for ((k=1;k<n;k++)); do
  filter+="${prev}[$k:v]xfade=transition=fade:duration=$fade:offset=$off[v$k];"
  prev="[v$k]"; off=$(echo "$off+$hold" | bc)
done
filter+="${prev}format=yuv420p,scale=1920:1080[out]"
ffmpeg -y -loglevel error "${inputs[@]}" -filter_complex "$filter" -map "[out]" -r 25 -c:v libx264 -crf 16 -preset slow "$out"
