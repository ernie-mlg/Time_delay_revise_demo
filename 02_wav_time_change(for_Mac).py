# To run this program, type:
#   python3 02_wav_time_change(for_Mac).py
#
# [EXAMPLE] Input the path of observer and speaker like this:
#
# オリジナルフォルダ名前を入力してください。Enter the name of the original folder: 
# sounds_file
# オブザーバーの出力フォルダ名前を入力してください。Enter the name of the observer output folder: 
# observer
# 話者の出力フォルダ名前を入力してください。Enter the name of the speaker output folder: 
# speaker_
# 図の出力フォルダ名前を入力してください。Enter the name of the plot output folder: 
# plot_
# 
# This program can do serval things:
#   1. Read the sound file
#   2. Split the sound file into several parts
#   3. Plot the wave of each part
#   4. Save the wave plot of each part
#   5. Save the sound file of each part


import os
import glob
import json
import librosa 
import matplotlib.pyplot as plt
import soundfile as sf
 
def correct_spk_wav(path_output):
    """
    This function is used to correct the time delay of each speaker by json text file
    """    
    transcript_index = 0
    for obs_json in path_obs_json:
        data_obs_json = json.load(open(obs_json, 'rb'), strict=False)
        for res_obs in data_obs_json['response']['results']:
            for alt_obs in res_obs['alternatives']:
                transcript_index += 1
                
                startTime_old = alt_obs['words'][0]['startTime'] * sr_obs
                endTime_old = alt_obs['words'][-1]['endTime'] * sr_obs
                if 'time_delay_start' in alt_obs:
                    startTime = alt_obs['words'][0]['startTime'] - alt_obs['time_delay_start']
                    endTime = alt_obs['words'][-1]['endTime'] - alt_obs['time_delay_end']
                else:
                    startTime = alt_obs['words'][0]['startTime']
                    endTime = alt_obs['words'][-1]['endTime']
                
                start_index = startTime * sr_obs    # new start time index
                end_index = endTime * sr_obs
                spk_wave = data_spk[int(start_index):int(end_index)]
                
                sf.write(path_output + '//spk_' + str(transcript_index) + '_.wav', spk_wave, sr_spk)   # output new speaker wave file                
                draw_figure(spk_wave, startTime_old, endTime_old, spk_index, transcript_index, startTime)

def draw_figure(wav_data, startTime, endTime, spk_index, transcript_index, Title_startTime): 
    """    
    wave figure drawing about observer voice, speaker voice before and after changing
    This function is used to double check the error of each voice by figure 
    
    wav_data: splited voice wave data
    startTime, endTime: time of one transcript which calculated by correct_spk_wav
    spk_index, transcript_index: index number of speaker and trancsript
    """    
    plt.plot(data_obs[int(startTime):int(endTime)], label="data_obs", color="blue", linewidth = 0.5)
    plt.plot(data_spk[int(startTime):int(endTime)], label="data_spk", color="red", linewidth = 0.5)
    plt.plot(wav_data, label="data_spk_new", color="green", linewidth = 1)  # draw speaker wave figure after changing
    plt.legend()
    plt.title(
        f"Speaker" + str(spk_index) + "_" + str(transcript_index) + ", start time" + str(Title_startTime),
        fontsize=14,
    )
    plt.savefig(text_plot + '/' + str (transcript_index) + '.jpg')
    plt.close()

def split_obs_wav(name_obs_output):
    """
    Time delay not calculated yet
    This function is used to double check the error of each voice by voice  
    """
    obs_index = 1
    create_dir(name_obs_output, obs_index)
    path_output = os.path.join(os.getcwd(), name_obs_output)
    transcript_index = 0
    for obs_json in path_obs_json:
        data_obs_json = json.load(open(obs_json, 'rb'), strict=False)
        for res_obs in data_obs_json['response']['results']:
            for alt_obs in res_obs['alternatives']:
                transcript_index += 1
                
                startTime = alt_obs['words'][0]['startTime']
                endTime = alt_obs['words'][-1]['endTime']
                
                start_index = startTime * sr_obs
                end_index = endTime * sr_obs
                obs_wave = data_obs[int(start_index):int(end_index)]    # splited wave                 
                sf.write(path_output + str(obs_index) + '//obs_' + str(transcript_index) + '.wav', obs_wave, sr_obs)    # split observer wave  
                
def create_dir(folder_name, index):        
    name = os.path.join(os.getcwd(), folder_name + str(index))
    if not os.path.exists(name):
        os.makedirs(name)
        print(f"Folder '{name}' created successfully!")
    else:
        print(f"Folder '{name}' already exists!")
       
def get_wav_path(file_pathname):
    """
    Please change the keyword if the file name is different
    This function is used to get all the path of speaker voice  
    """
    path_spk_list = []
    file_pathname = file_pathname + '//'
    for filename in os.listdir(file_pathname):
        if 'observer' not in filename:  # exclude observer voice, please change the keyword if the file name is different
            if 'new' not in filename:
                if '00011.wav' in filename: # please change the keyword for matching the speaker file name
                    path_spk_list.append(file_pathname + filename) 
    return path_spk_list


name_original = input("オリジナルフォルダ名前を入力してください。Enter the name of the original folder: ")
name_obs_output = input("オブザーバーの出力フォルダ名前を入力してください。Enter the name of the observer output folder: ")
name_spk_output = input("話者の出力フォルダ名前を入力してください。Enter the name of the speaker output folder: ")
name_text_plot = input("図の出力フォルダ名前を入力してください。Enter the name of the plot output folder: ")
path_spk_list = get_wav_path(os.path.join(os.getcwd(), name_original)) # Original voice path of one speaker

path_obs_list = glob.glob(os.path.join(os.getcwd(), name_original, "*observer*[!new].wav"))  # Original voice path of observer, all people
path_obs_json = glob.glob(os.path.join(os.getcwd(), name_original, "*observer*_new_new_new.json")) # Json path of observer, the number of "_new" behind are as many as speakers
                  
for path_obs in path_obs_list:
    data_obs, sr_obs = librosa.load(path_obs, sr=None)

spk_index = 0
for path_spk in path_spk_list:
    spk_index += 1
    data_spk, sr_spk = librosa.load(path_spk, sr=None)
    create_dir(name_spk_output, spk_index)
    create_dir(name_text_plot, spk_index)
    path_spk_out = os.path.join(os.getcwd(), name_spk_output + str(spk_index)) # Output path of speaker voice
    text_plot = os.path.join(os.getcwd(), name_text_plot + str(spk_index)) # Output path of wave figure
    correct_spk_wav(path_spk_out)
split_obs_wav(name_obs_output)
