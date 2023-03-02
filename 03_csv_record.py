# This program is to record the start time and duration time of each speaker's voice in csv file
# To run this program, please change the path of speaker file and csv file
# path_spk, path_csv    line 27, 28
#
# If there are multiple speaker file, please use this program again
# Please make sure that create

import sys
import csv
import json
import glob
import os
from pathlib import Path

def create_csv(path_spk, path_csv):
    # for spk_index in range(1,index): 
        with open(path_csv,'w') as file:
            csv_write = csv.writer(file)
            csv_head = ["offset","duration"]
            csv_write.writerow(csv_head)

def write_csv(path_csv, spk_offset, spk_duration):
    with open(path_csv,'a+') as file:
        csv_write = csv.writer(file)
        csv_write.writerow([spk_offset,spk_duration])

def main():

    # make sure the path is correct
    path_spk = "./sounds_file/watanabe_00011.json"    # Voice file of speaker, which has time delay
    path_csv = "./sounds_file/speaker3.csv"
    
    create_csv(path_spk, path_csv)
    data_spk = json.load(open(path_spk, 'rb'), strict=False)
    for res_spk in data_spk['response']['results']:
        for alt_spk in res_spk['alternatives']:
            MAX_TIME_DIFFERENCE = 5    # [changeable] diff of time less than 5 sec
            if 'time_delay_start' not in alt_spk or abs(alt_spk['time_delay_start']) > MAX_TIME_DIFFERENCE or abs(alt_spk['time_delay_end']) > MAX_TIME_DIFFERENCE :
                spk_offset = round(alt_spk['words'][0]['startTime'], 1)
                spk_duration = round(alt_spk['words'][-1]['endTime']  - alt_spk['words'][0]['startTime'], 1)
            elif abs(alt_spk['time_delay_start']) <= MAX_TIME_DIFFERENCE:   # テキスト的な修正  if time delay is less than 5 sec
                spk_offset = round((alt_spk['words'][0]['startTime'] + alt_spk['time_delay_start']), 1)
                spk_duration = round(((alt_spk['words'][-1]['endTime'] + alt_spk['time_delay_end']) - spk_offset), 1)
            write_csv(path_csv, spk_offset, spk_duration)
            
if __name__ == '__main__':
    main()
