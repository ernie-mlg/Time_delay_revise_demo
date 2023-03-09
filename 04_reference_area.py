# This program is color the reference area of each speaker
# To run this program, type:
#  python 04_reference_area.py 
#
# [EXAMPLE] input the path of observer and speaker like this:
# Enter the name of the original folder: 
# sounds_file
# Please input the name of speaker wav file, end with extension name '.wav': 
# observer_00011.wav

import os
import csv
import glob
import codecs
import librosa
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


name_original = input("オリジナルフォルダ名前を入力してください。Enter the name of the original folder: ")   
name_obs = input("Please input the name of speaker wav file, end with extension name '.wav': ") # name of observer file
path_obs = os.path.join(os.getcwd(), name_original, name_obs) # Wav path of observer
path_csv_list = glob.glob(os.path.join(os.getcwd(), "speaker*.csv")) # Csv path of speaker
    
def plot_obs(path_obs):
    data_obs, sr_obs = librosa.load(path_obs, sr=None)
    time = np.linspace(0, len(data_obs)/sr_obs, num=len(data_obs))
    plt.plot(time, data_obs, color="blue", linewidth = 0.5)
    ax = plt.gca()
    x_major_locator = MultipleLocator(60)
    ax.xaxis.set_major_locator(x_major_locator)
            
def plot_csv(path_csv_list):
    color_list = ["green", "red", "yellow"]
    index = 0
    for path_csv in path_csv_list:
        with codecs.open(path_csv, encoding='utf-8-sig') as f:
            for row in csv.DictReader(f, skipinitialspace=True):
                startTime = float(row['offset']) 
                endTime = startTime + float(row['duration'])  
                plt.axvspan(startTime, endTime, color = color_list[index], alpha=0.3)
                plt.legend(["observer"], loc ="upper right") # mark the name of the speaker here        
        index += 1        
            
def save_figure(path):
    plt.title(
        f"Full obs with reference area",
        fontsize=14,
    )    
    plt.xlabel('Time (s)', labelpad=10, fontweight="bold", fontfamily="serif",  linespacing=2.0)
    plt.ylabel('Amplitude')
    plt.savefig(f"{path}/reference_area.jpg", dpi = 600)
    plt.savefig(f"{path}/reference_area.svg")
    plt.close()

def main(path_obs, path_csv_list):    
    cwd = os.getcwd()    
    plot_obs(path_obs)    
    plot_csv(path_csv_list)
    save_figure(cwd)
    
if __name__ == '__main__':
    main(path_obs, path_csv_list)   
