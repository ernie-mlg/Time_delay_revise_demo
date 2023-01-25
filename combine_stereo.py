import wave
import os
import librosa
import numpy as np
import soundfile as sf
from pathlib import Path
import pyaudio
   
def combine_wav(spk_index, index):   
    # read wave files
    cwd = Path.cwd()
    ch1_path = Path.joinpath(cwd, "transcript_split_obs_2", "obs_" + str (index) + "_.wav") #
    ch2_path = Path.joinpath(cwd, "transcript_split_spk_" + str (spk_index) , "spk_" + str (index) + "_.wav")
    ch2_new_path = Path.joinpath(cwd, "DTW_plot", "wav_output_02", str (index) + ".wav")
    
    ch1, sr1 = librosa.load(ch1_path, sr=1600)        
    ch2, sr2 = librosa.load(ch2_path, sr=1600)   
    
    ch1_len = len(ch1)
    ch2_len = len(ch2)
    # use zero value to autocomplete length
    length = abs(ch2_len - ch1_len)
    temp_array = np.zeros(length, dtype=np.int16)
    if ch1_len < ch2_len:
        rch1_wave_data = np.concatenate((ch1, temp_array))
        rch2_wave_data = ch2
    elif ch1_len > ch2_len:
        rch2_wave_data = np.concatenate((ch2, temp_array))
        rch1_wave_data = ch1
    else:
        rch1_wave_data = ch1
        rch2_wave_data = ch2
    
    # A 2D array where the left and right tones are contained in their respective rows
    stereo = np.vstack((rch1_wave_data, rch2_wave_data))   
    # Reshape 2D array so that the left and right tones are contained in their respective columns
    stereo = stereo.transpose()
    DTW_plot_output = Path.joinpath(cwd, "DTW_plot", "test_correct_combined_" + str(spk_index)) # speaker path output
    sf.write(str(DTW_plot_output) + '/' + str (index) + '.wav', stereo, samplerate=1600)
    print(index, "in speaker No.", spk_index, "has finished")


for spk_index in range(1,4):
    for index in range(1,85):
        if index <= 84:
            DTW_plot = (r"F:\Work\Ernie\sounds_Align\DTW_plot")
            combine_wav(spk_index, index)
            index += 1
