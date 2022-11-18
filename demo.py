__updated__ = '2022-11-18 16:12:36'

import json
import editdistance
import glob
from collections import Counter

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
    TDE = alt_obs['words'][-1]['endTime'] - alt_spk['words'][-1]['endTime']
    return TDS, TDE

def get_min_time_delay(time_delay_list):
    min_abs = abs(time_delay_list[0])
    min_ele = time_delay_list[0]

    for l in time_delay_list:
        if abs(l) < min_abs:
            min_abs = abs(l)
            min_ele = l
    
    return min_ele     

# def get_trans_time(alt_obs, alt_spk):
    
    list_index = 0  # index in transcript_list
    last_index = 0

    for trans_list in alt_obs['transcript_list']: # loop of "transcript_list"
        # for index in range(len(alt_obs['transcript_list'])-1):
        words_num = 0   # index in list 'words', 'はい' = 0
        len_word = 0    # length of word composition, 'はい' + '。' = 3
        while list_index < len(alt_obs['transcript_list']): # 
            while words_num <= len(alt_obs['words']):
                if len_word < len(trans_list):
                    len_word += len(alt_obs['words'][words_num]['word'])
                else:
                    TDS_split = alt_obs['words'][last_index]['startTime'] - alt_spk['words'][last_index]['startTime']
                    TDE_split = alt_obs['words'][words_num-1]['endTime'] - alt_spk['words'][words_num-1]['endTime']
                    list_index += 1
                    last_index = words_num
                words_num += 1
        
    return TDS_split, TDE_split

def main():

    path_obs_list = glob.glob(r"F:\Work\Ernie\sounds_Align\sounds_file\*observer*[!new]meeting_1.json")  # Voice of all people
    path_spk_list = glob.glob(r"F:\Work\Ernie\sounds_Align\sounds_file\*[!observer]*meeting.json")     # Open local files of one person in list
    for path_obs in path_obs_list:
        data_obs = json.load(open(path_obs, 'rb'), strict=False)
        for path_spk in path_spk_list:
            data_spk = json.load(open(path_spk, 'rb'), strict=False)
        
            for res_obs in data_obs['response']['results']:
                for alt_obs in res_obs['alternatives']:
                
                    print('---------------------------------')
                    print('Observer:', alt_obs['transcript'])
                    alt_obs['transcript_list'] = []
                   
                
                    for res_spk in data_spk['response']['results']:
                        time_delay_start_list = []
                        time_delay_end_list = []
                        transcript_split_value = []
                        transcript_split_word = []
                        for alt_spk in res_spk['alternatives']:
                            time_diff = abs(alt_spk['words'][0]['startTime'] - alt_obs['words'][0]['startTime'])
                            # if diff of time is less than 40 sec
                            if time_diff <= 40:
                                pos_idx, similarity_list = find_suit_position(alt_obs['transcript'], alt_spk['transcript'])
                                trans_obs_sub = alt_obs['transcript'][pos_idx:pos_idx + len(alt_spk['transcript'])]
                                transcript_split_value.append(max(similarity_list))
                                transcript_split_word.append(trans_obs_sub)
                                max_value = transcript_split_value.index(max(transcript_split_value))
                                if similarity(trans_obs_sub, alt_spk['transcript']) > 2 / 3:
                                        print('Speaker in observer >>>>',trans_obs_sub)
                                        TDS, TDE = get_time_delay(alt_obs, alt_spk)
                                        time_delay_start_list.append(TDS)
                                        time_delay_end_list.append(TDE)
                                       
                                        minele_s = get_min_time_delay(time_delay_start_list)
                                        minele_e = get_min_time_delay(time_delay_end_list)
                                        
                                        alt_obs['time_delay_start'] = minele_s
                                        alt_obs['time_delay_end'] = minele_e
        
                                        alt_obs['transcript_split'] = alt_spk['transcript']
                                        
                                        alt_obs['transcript_list'].append(transcript_split_word[max_value])
        
                                        print('Observer [{} to {}] : {} '.format(alt_obs['words'][0]['startTime'], alt_obs['words'][-1]['endTime'], alt_obs['transcript']))
                                        print('time_delay_start ', alt_obs['time_delay_start'])
                                        print('time_delay_end ', alt_obs['time_delay_end'])
        
                                        # TDS_split, TDE_split = get_trans_time(alt_obs, alt_spk)
                                        # print('Observer [{} to {}] : {} '.format(TDS_split, TDE_split, alt_obs['transcript']))
                                        transcript_split_value = []
                                        transcript_split_word = []  # reset word and value list


    path_obs_new = open(path_obs.replace('.json', '_new.json'), 'w', encoding='utf-8')
    json.dump(data_obs, path_obs_new, ensure_ascii=False)

    print('wrote json to:', path_obs_new)

if __name__ == '__main__':    
    main()

