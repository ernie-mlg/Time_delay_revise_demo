# This program is to record the start time and duration time of each speaker's voice in csv file
#
# To run this program, type:
#   python 03_csv_record.py
#
# If there are multiple speaker file, please use this program again
# [EXAMPLE] input the path of observer and speaker like this:
# オリジナルフォルダ名前を入力してください。Enter the name of the original folder: 
# sounds_file
# Please input the name of speaker json file, end with extension name '.json': 
# watanabe_00011.json 
# Please input the name of csv, end with extension name '.csv': 
# speaker1.csv  

import os
import csv
import json

def create_csv(path_csv):
    with open(path_csv,'w') as file:
        csv_write = csv.writer(file)
        csv_head = ["offset","duration"]
        csv_write.writerow(csv_head)

def write_csv(path_csv, spk_offset, spk_duration):
    with open(path_csv,'a+') as file:
        csv_write = csv.writer(file)
        csv_write.writerow([spk_offset,spk_duration])

def main(MAX_TIME_DIFFERENCE): # [changeable] difference of time less than a setting second
    name_original = input("オリジナルフォルダ名前を入力してください。Enter the name of the original folder: ")   
    spk_json = input("Please input the name of speaker json file, end with extension name '.json': ") # name of speaker file
    path_spk = os.path.join(os.getcwd(), name_original, spk_json)  # Voice file of speaker
    file_csv = input("Please input the name of csv, end with extension name '.csv': ") # name of csv file
    path_csv = os.path.join(os.getcwd(), file_csv)  # Voice file of speaker
    create_csv(path_csv)
    data_spk = json.load(open(path_spk, 'rb'), strict=False)
    for res_spk in data_spk['response']['results']:
        for alt_spk in res_spk['alternatives']:   
            if 'time_delay_start' not in alt_spk or abs(alt_spk['time_delay_start']) > MAX_TIME_DIFFERENCE or abs(alt_spk['time_delay_end']) > MAX_TIME_DIFFERENCE :
                spk_offset = round(alt_spk['words'][0]['startTime'], 1)
                spk_duration = round(alt_spk['words'][-1]['endTime']  - alt_spk['words'][0]['startTime'], 1)
            elif abs(alt_spk['time_delay_start']) <= MAX_TIME_DIFFERENCE:   # テキスト的な修正  if time delay is less than 5 sec
                spk_offset = round((alt_spk['words'][0]['startTime'] + alt_spk['time_delay_start']), 1)
                spk_duration = round(((alt_spk['words'][-1]['endTime'] + alt_spk['time_delay_end']) - spk_offset), 1)
            write_csv(path_csv, spk_offset, spk_duration)
            
if __name__ == '__main__':
    main(5)
