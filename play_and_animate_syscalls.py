#!/usr/bin/env python2.7
from pydub import AudioSegment, silence
from pydub.playback import play
from time import sleep
from os import system #migrate to pydub playback with threadspawn
import sys
import numpy as np
import rospy
from std_msgs.msg import String

faceTopic = rospy.Publisher(
	'roboy/cognition/face/emotion',
	String, 10)

if sys.argv[1] == "":
	print("Please specify a wav file.")

file = sys.argv[1]
if not file.endswith(".wav"):
	print("Incorrect file format. Please provide wav file.")
	exit(1)

#os.spawnl(os.P_DETACH, 'cvlc ' + file)
#system("cvlc " + file + " &")
song = AudioSegment.from_wav(file)
voiceSegments = silence.detect_silence(song, 100, -30, 1)
toggleTimings = []

for segment in voiceSegments:
	toggleTimings.append(segment[0])
	toggleTimings.append(segment[1])

print(toggleTimings)

toggleState = 1

system("rosservice call /roboy/cognition/face/emotion \"emotion: 'blabla_start'\"")
system("cvlc --play-and-exit " + file + " &")
for i in range(toggleTimings[-1]):
	if (i == toggleTimings[0]):
		toggleTimings = toggleTimings[1:]
		toggleState = not toggleState
		#print(toggleState, i)
		if(toggleState):
			#faceTopic.publish(String("emotion: 'blabla_start'"))
			print("Start!")
			###system("rosservice call /roboy/cognition/face/emotion \"emotion: 'blabla_start'\"")
		else:
			#faceTopic.publish(String("emotion: 'blabla_stop'"))
			print("Stop!")
			###system("rosservice call /roboy/cognition/face/emotion \"emotion: 'blabla_stop'\"")
	i += 1
	sleep(0.0009)

system("rosservice call /roboy/cognition/face/emotion \"emotion: 'blabla_stop'\"")
# for segment in voice_segments:
# 	toPlay = segment[1] - segment[0]
# 	while toPlay > 150:
# 		#roboy open mouth
# 		print("Mouth.open()")
# 		sleep(150)
# 		#roboy close mouth
# 		print("Mouth.close()")
# 		toPlay -= 150
# 	if toPlay > 50:
# 		#roboy open mouth
# 		print("Mouth.open()")
# 		sleep(toPlay)
# 		#roboy close mouth
# 		print("Mouth.close()")

# print("Face.happy()")
