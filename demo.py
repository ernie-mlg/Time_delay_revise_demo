# -- coding: utf-8 --
import json

path_all = (r"F:\Work\Ernie\sounds_Align\sounds_file\00005_04_observer_kojima_meeting_1.json")
path_yama = (r"F:\Work\Ernie\sounds_Align\sounds_file\00005_01_onoyama_meeting.json")     # Open local files

yama = open(path_yama, 'rb')    # read json file, voice of Onoyama , encoding='utf-8-sig'
data_yama = json.load(yama, strict=False)    # return data in dict, strict check close
print(type(data_yama))

All = open(path_all,'rb')     #  , encoding='utf-8-sig'  , errors='ignore'
data_wata_1 = json.load(All)  #, strict=False


for res in data_yama['response']['results']:

     for alt in res['alternatives']:
          print('-----------------------------------------------------------------------------')
          print('transcript:', alt['transcript'])
          print('words[0]:', alt['words'][0]['word'], alt['words'][0]['startTime'])
          print('words[-1]:', alt['words'][-1]['word'],  alt['words'][-1]['endTime'])
          print('')
             
          for res_1 in data_wata_1['response']['results']:

                    for alt_1 in res_1['alternatives']:
                         # print('transcript_1:', alt_1['transcript'])
                         # print('words[0]:', alt_1['words'][0]['word'], alt_1['words'][0]['startTime'])
                         # print('words[-1]:', alt_1['words'][-1]['word'],  alt_1['words'][-1]['endTime'])
                         # print('')
                         # print('Onoyama: ',alt['transcript'])
          
                         if alt_1['transcript'] == alt['transcript']:
                              alt['time_delay_start'] = alt_1['words'][0]['startTime'] - alt['words'][0]['startTime']
                              print('time_delay_start is: ', alt['time_delay_start'])
                              alt['time_delay_end'] = alt_1['words'][-1]['endTime'] - alt['words'][-1]['endTime']
                              print('time_delay_end is: ', alt['time_delay_end'])
                              print(type(alt['transcript']))
                                                          
path_yama_new = open(path_yama + '_new.json', 'w', encoding="utf-8")  # Open new file in unicode, encoding='utf-8-sig'
json.dump(data_yama, path_yama_new, ensure_ascii=False)     #  ensure_ascii=False

print('Onoyama finished.')
