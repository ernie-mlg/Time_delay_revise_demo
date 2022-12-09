import librosa 
import glob
import os
import json
import matplotlib.pyplot as plt
import soundfile as sf
import copy
import numpy as np
from pydub import effects, AudioSegment
from scipy.io import wavfile

def get_wav_path(file_pathname):
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

def get_json_path(file_pathname):
    path_spk_list = []
    file_pathname = file_pathname + '\\'
    for filename in os.listdir(file_pathname):
        path = os.path.join(file_pathname, filename)
        if 'observer' not in filename:
            if 'new' not in filename:
                if 'meeting.json' in filename: 
                    path_spk_list.append(file_pathname + filename) 
    return path_spk_list

path_spk_list = get_wav_path(r"F:\Work\Ernie\sounds_Align\sounds_file") # Open voice of one speaker
path_obs_list = glob.glob(r"F:\Work\Ernie\sounds_Align\sounds_file\*observer*[!new]meeting_1.wav")  # Open voice of all people

for path_spk in path_spk_list:
    data_spk, sr_spk = librosa.load(path_spk, sr=None)
for path_obs in path_obs_list:
    data_obs, sr_obs = librosa.load(path_obs, sr=None)

path_obs_json = glob.glob(r"F:\Work\Ernie\sounds_Align\sounds_file\*observer*new.json")
path_obs_out_1 = (r"F:\Work\Ernie\sounds_Align\transcript_split_obs")
path_spk_out_1 = (r"F:\Work\Ernie\sounds_Align\transcript_split_spk_1")


def split_obs_wav(path_output): # Time delay not calculation
    i = 0
    for obs_json in path_obs_json:
        data_obs_json = json.load(open(obs_json, 'rb'), strict=False)
        for res_obs in data_obs_json['response']['results']:
            for alt_obs in res_obs['alternatives']:
                i += 1
                startTime = alt_obs['words'][0]['startTime']
                start_index = startTime * sr_obs
                endTime = alt_obs['words'][-1]['endTime']
                end_index = endTime * sr_obs
                wav_data = data_obs[int(start_index):int(end_index)] 
                sf.write(path_output + '\\obs_' + str(i) + '_.wav', wav_data, sr_obs)
                _sound = AudioSegment.from_file(path_output + '\\obs_' + str(i) + '_.wav', "wav")
                sound = effects.normalize(_sound)
                sound.export(path_output + '\\obs_' + str(i) + '_normalized.wav', format="wav")
                   
def correct_spk_wav(path_output): # Time delay calculation
    j = 0
    for obs_json in path_obs_json:
        data_obs_json = json.load(open(obs_json, 'rb'), strict=False)
        for res_obs in data_obs_json['response']['results']:
            for alt_obs in res_obs['alternatives']:
                j += 1
                if 'time_delay_start' in alt_obs:
                    startTime = alt_obs['words'][0]['startTime'] - max(0,alt_obs['time_delay_start'])
                    endTime = alt_obs['words'][-1]['endTime'] - max(0,alt_obs['time_delay_end'])
                else:
                    startTime = alt_obs['words'][0]['startTime']
                    endTime = alt_obs['words'][-1]['endTime']
                start_index = startTime * sr_obs
                end_index = endTime * sr_obs
                wav_data = data_spk[int(start_index):int(end_index)]
                sf.write(path_output + '\\spk_' + str(j) + '_.wav', wav_data, sr_spk)
                _sound = AudioSegment.from_file(path_output + '\\spk_' + str(j) + '_.wav', "wav")
                sound = effects.normalize(_sound)
                sound.export(path_output + '\\spk_' + str(j) + '_normalized.wav', format="wav")

def normalize(path_output):
    fs, data = wavfile.read(path_output)

    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(data)

    xx = copy.deepcopy(data)
    xx = xx - np.mean(xx)
    x = xx/np.max(np.abs(xx))

    plt.subplot(2,1,2)
    plt.plot(x)
    plt.show()

split_obs_wav(path_obs_out_1)
correct_spk_wav(path_spk_out_1)
            
# plt.plot(data_obs[int(start_index):int(end_index)])
