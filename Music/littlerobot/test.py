import time
import wave
import contextlib
fname = 'littlerobot.wav'
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    print(duration)
    #time.sleep(duration)
    print(duration)