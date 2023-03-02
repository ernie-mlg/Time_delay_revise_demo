# Author: Ernie MLG
# This program is color the reference area of speaker and observer
# To run this program, type:
#  python 04_reference_area.py 
#
# change the path of observer and speaker like this:    (line 19)
# ./sounds_file/00005_04_observer_kojima_meeting_1.wav ./csv_file/00005_04_observer_kojima_meeting_1.csv ./csv_file/00005_04_speaker_kojima_meeting_1.csv
#

import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import glob
import librosa
import csv
import codecs
import os
import numpy as np

path_obs = ("./sounds_file/observer_00011.wav") # Wav path of observer
    
def plot_obs(path_obs):
    data_obs, sr_obs = librosa.load(path_obs, sr=None)
    time = np.linspace(0, len(data_obs)/sr_obs, num=len(data_obs))
    plt.plot(time, data_obs, color="blue", linewidth = 0.5)
    ax=plt.gca()
    x_major_locator=MultipleLocator(60)
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
                plt.legend(["observer", "honda"], loc ="upper right") # mark the name of the speaker, now can only mark one speaker        
                # plt.legend(["observer", "Onoyama", "watanabe"], loc ="upper right") # mark the name of the speaker, now can only mark one speaker        
        index += 1        
            
def save_figure(path):
    plt.title(
        f"Full obs with reference area",
        fontsize=14,
    )    
    plt.xlabel('Time (s)', labelpad=10, fontweight="bold", fontfamily="serif",  linespacing=2.0)
    plt.ylabel('Amplitude')
    # plt.show()
    plt.savefig(f"{path}/reference_area.jpg", dpi = 600)
    plt.savefig(f"{path}/reference_area.svg")
    plt.close()

def main(path_obs):
    
    cwd = os.getcwd()    
    path_csv_list = glob.glob(r"F:\Work\Ernie\sounds_Align\sounds_file\speaker*.csv") # Json path of observer
    plot_obs(path_obs)    
    plot_csv(path_csv_list)
    save_figure(cwd)
    
if __name__ == '__main__':
    main(path_obs)   
# Path: reference_area.py
