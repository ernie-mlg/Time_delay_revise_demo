import librosa 
import glob
import os
import json
import matplotlib.pyplot as plt
import soundfile as sf

def get_wav_path(file_pathname):
    path_spk_list = []
    file_pathname = file_pathname + '\\'
    for filename in os.listdir(file_pathname):
        path = os.path.join(file_pathname, filename)
        if 'observer' not in filename:
            if 'new' not in filename:
                if 'meeting.wav' in filename: 
                    path_spk_list.append(file_pathname + filename) 
    return path_spk_list
  
                   
def correct_spk_wav(path_output):
    """
    Time delay calculation
    
    path_output: path of split sound files output
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
                    startTime = alt_obs['words'][0]['startTime'] - max(0,alt_obs['time_delay_start'])
                    endTime = alt_obs['words'][-1]['endTime'] - max(0,alt_obs['time_delay_end'])
                else:
                    startTime = alt_obs['words'][0]['startTime']
                    endTime = alt_obs['words'][-1]['endTime']
                    
                start_index = startTime * sr_obs    # new start time index
                end_index = endTime * sr_obs
                wav_data = data_spk[int(start_index):int(end_index)]
                
                sf.write(path_output + '\\spk_' + str(transcript_index) + '_.wav', wav_data, sr_spk)   # output new speaker wave file                
                draw_figure(wav_data, startTime_old, endTime_old, spk_index, transcript_index)

def draw_figure(wav_data, starTime, endTime, spk_index, transcript_index): 
    """    
    wave figure drawing about observer voice, speaker voice before and after changing
    
    wav_data: splited voice wave data
    starTime, endTime: time of one transcript which calculated by correct_spk_wav
    spk_index, transcript_index: index number of speaker and trancsript
    """    
    plt.plot(data_obs[int(starTime):int(endTime)], label="data_obs", color="blue", linewidth = 0.5)
    plt.plot(data_spk[int(starTime):int(endTime)], label="data_spk", color="red", linewidth = 0.5)
    plt.plot(wav_data, label="data_spk_new", color="green", linewidth = 1)  # draw new speaker wave figure
    plt.legend()
    plt.title(
        f"transcript revise " + str(spk_index) + "_" + str (transcript_index),
        fontsize=14,
    )
    plt.savefig(text_plot + './' + str (transcript_index) + '.jpg')
    plt.close()

def split_obs_wav(path_output):
    """
    Time delay not calculated yet      
    """
    transcript_index = 0
    for obs_json in path_obs_json:
        data_obs_json = json.load(open(obs_json, 'rb'), strict=False)
        for res_obs in data_obs_json['response']['results']:
            for alt_obs in res_obs['alternatives']:
                transcript_index += 1
                
                startTime = alt_obs['words'][0]['startTime']
                start_index = startTime * sr_obs
                endTime = alt_obs['words'][-1]['endTime']
                end_index = endTime * sr_obs
                wav_data = data_obs[int(start_index):int(end_index)]    # splited wave                 
                sf.write(path_output + '\\obs_' + str(transcript_index) + '_.wav', wav_data, sr_obs)    # split observer wave  
    
# please set your own path below ↓
path_spk_list = get_wav_path(r"F:\Work\Ernie\sounds_Align\sounds_file") # Voice path of one speaker
path_obs_list = glob.glob(r"F:\Work\Ernie\sounds_Align\sounds_file\*observer*[!new]meeting_1.wav")  # Voice path of all people
path_obs_json = glob.glob(r"F:\Work\Ernie\sounds_Align\sounds_file\*observer*new.json") # Json path of observer
path_obs_out_1 = (r"F:\Work\Ernie\sounds_Align\transcript_split_obs_1") # Output path of observer voice

for path_obs in path_obs_list:
    data_obs, sr_obs = librosa.load(path_obs, sr=None)
    
spk_index = 0    
for path_spk in path_spk_list:
    spk_index += 1
    data_spk, sr_spk = librosa.load(path_spk, sr=None)
    path_spk_out = (r"F:\Work\Ernie\sounds_Align\transcript_split_spk_" + str(spk_index))
    text_plot = (r"F:\Work\Ernie\sounds_Align\text_plot_" + str(spk_index))
    correct_spk_wav(path_spk_out)
split_obs_wav(path_obs_out_1)
