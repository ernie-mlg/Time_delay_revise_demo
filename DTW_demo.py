import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import pandas as pd
from fastdtw import fastdtw
from pathlib import Path
from scipy import stats
from scipy.interpolate import interp1d
import librosa
import os
import wavfile
import glob
import matplotlib
import scipy
from scipy.io.wavfile import write


name_obs = input("切り離されたオブザーバー音声のフォルダ名前を入力してください。Enter the name of the splited observer folder: ") # name of observer file
name_spk = input("切り離された話者音声のフォルダ名前を入力してください。Enter the name of the splited speaker folder: ")  
wav_output = input("出力するwavファイルのフォルダ名前を入力してください。Enter the name of the output wav folder: ") 

path_obs_list = glob.glob(os.path.join(os.getcwd(), name_obs, "obs*.wav"))  # Original voice path of observer, all people
path_spk_list = glob.glob(os.path.join(os.getcwd(), name_spk, "spk*.wav"))  # Original voice path of observer, all people


def fast_DTW(index, name_obs, name_spk):

    obs = os.path.join(os.getcwd(), name_obs, "obs_" + str(index) + ".wav")
    spk = os.path.join(os.getcwd(), name_spk, "spk_" + str(index) + "_.wav")

    data_obs, sr = librosa.load(obs, sr=1600)
    data_spk, Fs1 = librosa.load(spk, sr=1600)

    plt.figure(figsize=(12, 4))

    distance_12, path_dtw = fastdtw(data_spk, data_obs) # ⬅️ THIS IS THE CORE CODE ⬅️ use left to sync right
    
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
    plt.legend(["data_obs"],["data_spk"])
    plt.title(
        f"DTW(data_obs, data_spk)" + "_" + str(index),
        fontsize=14,
    )
    data_spk_new = np.asarray(data_spk_new) 
    scipy.io.wavfile.write(os.getcwd() + wav_output + str (index) + '.wav', 1600, data = data_spk_new.astype(np.int16))    # wavfile output    data = data_spk_new.astype(np.int16)
    print("No. ", index, " finished")
    matplotlib.pyplot.close()
    plt.close()

index = 0
for path_spk in path_spk_list:
    index += 1
    fast_DTW(index, name_obs, name_spk)
