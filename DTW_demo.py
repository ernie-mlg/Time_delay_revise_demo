import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from fastdtw import fastdtw
from pathlib import Path
import librosa
import os
import glob

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

def fast_DTW(path_obs_index, path_spk_index):
    
    cwd = Path.cwd()
    path_obs_list = Path(Path.joinpath(cwd, 'transcript_split_obs_2', 'obs_' + str (path_obs_index) + '_.wav'))
    path_spk_list = Path(Path.joinpath(cwd, 'transcript_split_spk_1', 'spk_' + str (path_spk_index) + '_.wav'))

    data_spk, Fs1 = librosa.load(path_spk_list, sr=1600)
    data_obs, sr = librosa.load(path_obs_list, sr=1600)

    plt.figure(figsize=(12, 4))

    # 波形をプロット
    plt.plot(data_obs, label="data_obs", color="k")
    plt.plot(data_spk, label="data_spk", color="r")
    plt.legend()
    # plt.show()

    distance_12, path_dtw = fastdtw(data_spk, data_obs) # use left to sync right

    # 対応するポイントを線で結ぶ
    plt.figure(figsize=(12, 4))
    # for x_12 in path_dtw:
        # plt.plot(x_12, [data_obs[x_12[0]], data_spk[x_12[1]]], color="green", linestyle="dotted", linewidth = 0.1)
    
    data_spk_new = []    
    for i in range(0,len(path_dtw)):
        data_spk_new.append(data_spk[path_dtw[i][0]])
    # 波形をプロット
    plt.plot(data_obs, label="data_obs", color="blue", linewidth = 0.1)
    plt.plot(data_spk, label="data_spk", color="red", linewidth = 0.1)
    plt.plot(data_spk_new, label="data_spk_new", color="green", linewidth = 0.1)
    plt.legend()
    plt.title(
        f"DTW(data_obs, data_spk)",
        fontsize=14,
    )
    plt.show()
    # print("finish")

DTW_plot = (r"F:\Work\Ernie\sounds_Align\DTW_plot")
index = 1
fast_DTW(index, index)
plt.savefig(DTW_plot + './' + str (index) + '.jpg')
    
# for index in range(1,85):
#     if index <= 84:
#         fast_DTW(index, index)
#         plt.savefig(DTW_plot + './' + str (index) + '.jpg')
#         print("No. ", index, " finished")
#         index += 1
