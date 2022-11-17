import json
import editdistance

def similarity(str1, str2):
    simi = editdistance.eval(str1, str2) / len(str2)
    return 1 - simi


def find_suit_position(trans_obs, trans_spk):
    similarity_list = []
    i = 0
    while (i <= abs(len(trans_obs) - len(trans_spk))):
        similarity_list.append(similarity(trans_obs[i:len(trans_spk) + 1], trans_spk))
        i += 1

    pos_idx = similarity_list.index(max(similarity_list))
    return pos_idx, similarity_list


def get_time_delay(alt_obs, alt_spk):
    TDS = alt_obs['words'][0]['startTime'] - alt_spk['words'][0]['startTime']
    TDE = alt_obs['words'][-1]['endTime'] -alt_spk['words'][-1]['endTime']
    return TDS, TDE

def get_min_time_delay(time_delay_list):
    min_abs = abs(time_delay_list[0])
    min_ele = time_delay_list[0]

    for l in time_delay_list:
        if abs(l) < min_abs:
            min_abs = abs(l)
<<<<<<< HEAD
            min_ele = l 
    return min_ele                               

def get_trans_time(alt_obs):
    k = 0
    j = 0
    len_word = 0
    for j in alt_obs['words']:
        if len_word >= len(alt_obs['transcript_list'][j]):
            TDS_split = alt_obs['words'][k]['startTime'] - alt_obs['words'][k+len_word]['startTime']
            TDE_split = alt_obs['words'][k]['endTime'] - alt_obs['words'][k+len_word]['endTime']
        else :
            len_word += len(alt_obs['words'][k]['word'])
            k += 1

            return TDS_split, TDE_split
=======
            min_ele = l

    
    return min_ele                               
>>>>>>> 33612f7d8fff76c5cdc551c2a3d2496f32d4a5bd


def main():
    path_obs = (r"./edited_wav/00005_edit/00005_04_observer_kojima_meeting_1.json")      # Voice of all people
    path_spk = (r"./edited_wav/00005_edit/00005_01_onoyama_meeting.json")     # Open local files of one person

    data_obs = json.load(open(path_obs, 'rb'), strict=False)
    data_spk = json.load(open(path_spk, 'rb'), strict=False)

    for res_obs in data_obs['response']['results']:
        for alt_obs in res_obs['alternatives']:

<<<<<<< HEAD
            print('---------------------------------')
            print('Observer [{} to {}] : {} '.format(alt_obs['words'][0]['startTime'], alt_obs['words'][-1]['endTime'], alt_obs['transcript']))
            alt_obs['transcript_list'] = []
           
        
            for res_spk in data_spk['response']['results']:
=======
            print('transcript of all:', alt_obs['transcript'])
            alt_obs['transcript_list'] = []
           
        
        for res_spk in data_spk['response']['results']:
>>>>>>> 33612f7d8fff76c5cdc551c2a3d2496f32d4a5bd
                time_delay_start_list = []
                time_delay_end_list = []
                transcript_split_value = []
                transcript_split_word = []
                for alt_spk in res_spk['alternatives']:
                    time_diff = abs(alt_spk['words'][0]['startTime'] - alt_obs['words'][0]['startTime'])
                    # if diff of time is less than 40 sec
                    if time_diff <= 40:
                        i = 0
<<<<<<< HEAD
=======

>>>>>>> 33612f7d8fff76c5cdc551c2a3d2496f32d4a5bd
                        pos_idx, similarity_list = find_suit_position(alt_obs['transcript'], alt_spk['transcript'])
                        trans_obs_sub = alt_obs['transcript'][pos_idx:pos_idx + len(alt_spk['transcript'])]
                        transcript_split_value.append(max(similarity_list))
                        transcript_split_word.append(trans_obs_sub)
<<<<<<< HEAD
                        min_value = transcript_split_value.index(max(transcript_split_value))
                        #print('Speaker [{} to {}] : {} '.format(alt_spk['words'][0]['startTime'], alt_spk['words'][-1]['endTime'], alt_spk['transcript']))
                        if similarity(trans_obs_sub, alt_spk['transcript']) > 1 / 3:
                                print('Speaker [{} to {}] : {} '.format(alt_spk['words'][0]['startTime'], alt_spk['words'][-1]['endTime'], alt_spk['transcript']))
                                #obs_sub_startTime =
                                #obs_sub_endTime =
                                [word_info['word'] for word_info in  alt_obs['words']] 
                                if similarity(alt_obs['transcript'], alt_spk['transcript']) > 0.8 :
                                
                                    spk_startTime = alt_obs['words'][0]['startTime']
                                    spk_endTime = alt_obs['words'][-1]['endTime']
                                else:
                                    spk_startTime = None
                                    spk_endTime = None
                                    print('!!!!!!!!!!!!!!!!!!!!!')
                                print('>>> Speaker in observer [{} to {}] : {} '.format(spk_startTime, spk_endTime, alt_spk['transcript']))
=======
                        max_value = transcript_split_value.index(max(transcript_split_value))
                        
                        if similarity(trans_obs_sub, alt_spk['transcript']) > 2 / 3:
>>>>>>> 33612f7d8fff76c5cdc551c2a3d2496f32d4a5bd
                                TDS, TDE = get_time_delay(alt_obs, alt_spk)
                                time_delay_start_list.append(TDS)
                                time_delay_end_list.append(TDE)
                               
                                minele_s = get_min_time_delay(time_delay_start_list)
                                minele_e = get_min_time_delay(time_delay_end_list)
                                
                                alt_obs['time_delay_start'] = minele_s
                                alt_obs['time_delay_end'] = minele_s

                                alt_obs['transcript_split'] = alt_spk['transcript']
                                
<<<<<<< HEAD
                                alt_obs['transcript_list'].append(transcript_split_word[min_value])
                                #transcript_split_word = []
                                break
=======
                                alt_obs['transcript_list'].append(transcript_split_word[max_value])
                                transcript_split_value = list()    
                                transcript_split_word = list()     # reset word and value list

>>>>>>> 33612f7d8fff76c5cdc551c2a3d2496f32d4a5bd
    path_obs_new = open(path_obs.replace('.json', '_new.json'), 'w', encoding='utf-8')
    json.dump(data_obs, path_obs_new, ensure_ascii=False)

    print('wrote json to:', path_obs_new)

if __name__ == '__main__':    
    main()

