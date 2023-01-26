import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import pandas as pd
from fastdtw import fastdtw
from pathlib import Path
from scipy import stats
import librosa
import wavfile
import os
import glob
import matplotlib

def get_file_path(file_pathname):
    path_spk_list = []
    file_pathname = file_pathname + '\\'
    for filename in os.listdir(file_pathname):
        path = os.path.join(file_pathname, filename)
        if 'observer' not in filename:
            if 'new' not in filename:
                if 'meeting.wav' in filename: 
                    path_spk_list.append(file_pathname + filename) 
                    # print(path_spk_list)
    return path_spk_list    

# path_spk_list = get_file_path(r"F:\Work\Ernie\sounds_Align\transcript_split_spk_1")
# path_spk_list = glob.glob(r"F:\Work\Ernie\sounds_Align\transcript_split_spk_1\*.wav")  # Voice of all people
# path_obs_list = glob.glob(r"F:\Work\Ernie\sounds_Align\transcript_split_obs_2\*.wav")  # Voice of all people

def fast_DTW(path_obs_index, path_spk_index, spk_num):
    
    cwd = Path.cwd()
    path_obs_list = Path(Path.joinpath(cwd, 'transcript_split_obs_1', 'obs_' + str (path_obs_index) + '_.wav'))
    path_spk_list = Path(Path.joinpath(cwd, 'transcript_split_spk_'+ str(spk_num), 'spk_' + str (path_spk_index) + '_.wav'))

    data_spk, Fs1 = librosa.load(path_spk_list, sr=1600)
    data_obs, sr = librosa.load(path_obs_list, sr=1600)

    plt.figure(figsize=(12, 4))

    # THIS IS THE CORE CODE ⬇
    distance_12, path_dtw = fastdtw(data_spk, data_obs) # use left to sync right
    
    max_dtw = []
    data_spk_new = [data_spk]
    i = 0    
    while i < len(path_dtw)-1:
        # if path_dtw[i][0] != path_dtw[i+1][0]:
        #     if path_dtw[i][1] != path_dtw[i+1][1]:
        #         data_spk_new.append(data_spk[path_dtw[i][0]])          
        # else: 
        #     data_spk_new.append(0)
        max_dtw.append(path_dtw[i][1] - path_dtw[i][0])
        i += 1

    np.mean(max_dtw)    # 平均値
    np.median(max_dtw)  # 中央値
    stats.mode(max_dtw)[0][0]   # 最頻数
    
#     if stats.mode(max_dtw)[0][0] < 0:
#         data_spk_new.insert(stats.mode(max_dtw)[0][0], data_spk_new[::])
#     else:
#         mode = -stats.mode(max_dtw)[0][0]
#         data_spk_new.insert(mode, data_spk_new[::])
    
    plt.plot(data_obs, label="data_obs", color="blue", linewidth = 1)
    plt.plot(data_spk, label="data_spk", color="red", linewidth = 1)
    plt.plot(data_spk_new, label="data_spk_new", color="green", linewidth = 1)
    plt.legend()
    plt.title(
        f"DTW(data_obs, data_spk)" + "_" + str(index),
        fontsize=14,
    )
    # data_spk_new = np.asarray(data_spk_new) 
    # wavfile.write(DTW_plot + './wav_output/' + str (index) + '.wav', 1600, data_spk_new.astype(np.int16)) 
    # sf.write(DTW_plot + './wav_output_0' + str(spk_num) + '/' + str (index) + '.wav', data_spk_new, 1600)  # wavfile output
    plt.show()
    print("finish")

DTW_plot = (r"F:\Work\Ernie\sounds_Align\DTW_plot")
# index = 63
# fast_DTW(index, index)
# plt.savefig(DTW_plot + './' + str (index) + '.jpg')
    
for spk_num in range(1,4): 
    for index in range(1,85):
        if index <= 84:
            fast_DTW(index, index, spk_num)
            plt.savefig(DTW_plot + './' + str (index) + '.jpg')
            print("No. ", index, " finished")
            index += 1
            matplotlib.pyplot.close()
            plt.close()
