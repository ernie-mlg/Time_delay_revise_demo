# -- coding: utf-8 --
import json
import editdistance

path_all = (r"F:\Work\Ernie\sounds_Align\sounds_file\00005_04_observer_kojima_meeting_1.json")      # Voice of all people
path_yama = (r"F:\Work\Ernie\sounds_Align\sounds_file\00005_01_onoyama_meeting.json")     # Open local files of one person

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
               time_delay_start_list = list() # Create a new list for calculating minimum time error, start time
               time_delay_end_list = list() # For end time               
               transcript_split_value = list()
               transcript_split_word = list()

               for alt_1 in res_1['alternatives']:
                    
                    def simirallity (trans1, trans2):
                         simi = editdistance.eval(trans1, trans2)
                         return simi   
                    if len(alt_1['transcript']) <= 9:
                         tolerance = len(alt_1['transcript']) - 3
                         if tolerance <= 0:
                              tolerance = 1
                    else :
                         tolerance = 10

                    if simirallity (alt_1['transcript'], alt['transcript']) < tolerance:
                         
                         TDS = alt_1['words'][0]['startTime'] - alt['words'][0]['startTime']
                         time_delay_start_list.append(TDS) # Recording in list of start time
                         alt['time_delay_start'] = alt_1['words'][0]['startTime'] - alt['words'][0]['startTime']
                         # print('time_delay_start is: ', alt['time_delay_start'])
                         TDE = alt_1['words'][-1]['endTime'] - alt['words'][-1]['endTime']
                         time_delay_end_list.append(TDE) # Recording in list of end time
                         alt['time_delay_end'] = alt_1['words'][-1]['endTime'] - alt['words'][-1]['endTime']
                         # print('time_delay_end is: ', alt['time_delay_end'])

                         ##################################################
                         minabs_s = abs(time_delay_start_list[0])  # Find the minimum time delay of start time
                         minele_s = time_delay_start_list[0]  # and return in original value
                         for l in time_delay_start_list:
                              if abs(l) < minabs_s:
                                   minabs_s = abs(l)
                                   minele_s = l
                         alt['time_delay_start'] = minele_s
                         # print('minimum start time delay is:', alt['time_delay_start'])   
                                            
                         minabs_e = abs(time_delay_end_list[0])  # Find the minimum time delay of end time
                         minele_e = time_delay_end_list[0]  # and return in original value
                         for l in time_delay_end_list:
                              if abs(l) < minabs_e:
                                   minabs_e = abs(l)
                                   minele_e = l
                         ##################################################

                         alt['time_delay_end'] = minele_e
                         # print('minimum end time delay is:', alt['time_delay_end'])    
                    
                    i = 0
                    similarity_list = []

                    while (i <= abs(len(alt_1['transcript'])-len(alt['transcript']))):
                        similarity_list.append(editdistance.eval(alt_1['transcript'][i:len(alt['transcript'])+i], alt['transcript']))
                        i = i + 1
                    position = similarity_list.index(min(similarity_list)) # Position of minimum similarity 
                    print('Split transcript in list No.', position, ', content ', alt_1['transcript'][position:position + len(alt['transcript'])]) 
                    print('similarity_list is: ', similarity_list)

                    transcript_split_value.append(min(similarity_list))    # Value of minimum similarity 
                    transcript_split_word.append(alt_1['transcript'][position:position + len(alt['transcript'])])  # Content of minimum similarity
                    mini_value = transcript_split_value.index(min(transcript_split_value))
                    alt['transcript_split'] = transcript_split_word[mini_value] # Recording of content in dictionary, json file
                    print('transcript_split_value: ', transcript_split_value)
            
path_yama_new = open(path_yama + '_new.json', 'w', encoding="utf-8")  # Open new file in unicode, encoding='utf-8-sig'
json.dump(data_yama, path_yama_new, ensure_ascii=False)     #  ensure_ascii=False

print('\n Onoyama finished.')
