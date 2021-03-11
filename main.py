import soundfile as sf
import pydub
import numpy as np
# import subprocess

def write(f, sr, x, normalized=False):
    """numpy array to MP3"""
    channels = 2 if (x.ndim == 2 and x.shape[1] == 2) else 1
    if normalized:  # normalized array - each item should be a float in [-1, 1)
        y = np.int16(x * 2 ** 15)
    else:
        y = np.int16(x)
    song = pydub.AudioSegment(y.tobytes(), frame_rate=sr, sample_width=2, channels=channels)
    song.export(f, format="wav", bitrate="320k")


x, sr = sf.read('AudioTest1.raw', channels=1, samplerate=44100,
                subtype='FLOAT')

print(x, sr)
write('outAudioTest1.wav', sr, x)
