import wave
import os
import librosa
import numpy as np
import soundfile as sf
from pathlib import Path
import pyaudio
   
def combine_wav(index):   
# read wave files
    cwd = Path.cwd()
    ch1_path = Path.joinpath(cwd, "transcript_split_obs_2", "obs_" + str (index) + "_.wav")
    ch2_path = Path.joinpath(cwd, "transcript_split_spk_2", "spk_" + str (index) + "_.wav")
    ch2_new_path = Path.joinpath(cwd, "DTW_plot", "wav_output_02", str (index) + ".wav")
    
    ch1, sr1 = librosa.load(ch1_path, sr=1600)
    # ch2, sr2 = librosa.load(ch2_path, sr=1600)   
    ch2, sr2 = librosa.load(ch2_new_path, sr=1600)   
    
    ch1_len = len(ch1)
    ch2_len = len(ch2)
    # 对不同长度的音频用数据零对齐补位
    if ch1_len < ch2_len:
        length = abs(ch2_len - ch1_len)
        temp_array = np.zeros(length, dtype=np.int16)
        rch1_wave_data = np.concatenate((ch1, temp_array))
        rch2_wave_data = ch2
    elif ch1_len > ch2_len:
        length = abs(ch2_len - ch1_len)
        temp_array = np.zeros(length, dtype=np.int16)
        rch2_wave_data = np.concatenate((ch2, temp_array))
        rch1_wave_data = ch1
    else:
        rch1_wave_data = ch1
        rch2_wave_data = ch2
    
# A 2D array where the left and right tones are contained in their respective rows
    stereo = np.vstack((rch1_wave_data, rch2_wave_data))   
# Reshape 2D array so that the left and right tones are contained in their respective columns
    stereo = stereo.transpose()   
    sf.write(DTW_plot + './wav_output_combined/' + str (index) + '.wav', stereo, samplerate=1600)

DTW_plot = (r"F:\Work\Ernie\sounds_Align\DTW_plot")

for index in range(1,85):
    if index <= 84:
        combine_wav(index)
        index += 1
        
