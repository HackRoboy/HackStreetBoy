#!/bin/bash

if [ "$1" == "-h" ];then
	echo "generate_wav.sh <filetype> <song name> [play] \n Converts file into wav using ecantorix."
	exit
fi
type="$1"
song="$2"
if [ "$song" == "" ];then
	echo "Please specify Song"
fi

if [ "$type" == "" ];then
	echo "Please specify extension to convert(abc/midi)"
fi

if [ "$type" == "abc" ];then
	abc2midi "./Music/$song/$song.abc" -o "./Music/$song/$song.midi" 
	type="midi"
fi

if [ "$type" == "mxl" ];then
	python ./xml2abc/xml2abc.py "./Music/$song/$song.mxl" -o "./Music/$song" -x
	abc2midi "./Music/$song/$song.abc" -o "./Music/$song/$song.midi" 
	type="midi"
fi


if [ "$type" == "midi" ] || [ "$type" == "mid" ];then
	mkdir ./ecantorix-cache
	perl ./ecantorix/ecantorix.pl -O wav -o "./Music/$song/$song.wav" "./Music/$song/$song.$type" -c ./ecantorix-cache
	rm -rf ./ecantorix-cache
	type="wav"
fi
if [ "$type" == "wav" ];then
	if [ "$3" == "dont_play" ];then
		echo "Done!"
	else
		python "./play_and_animate_syscalls.py" "./Music/$song/$song.wav"
	fi
	echo "Song extension unknown!"
fi
