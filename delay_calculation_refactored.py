import json
import editdistance
import glob
import os
from collections import Counter

def similarity(string_1, string_2):
    similarity = editdistance.eval(string_1, string_2) / len(string_2)
    return 1 - similarity


def find_suit_position(trans_obs, trans_spk):
    similarity_list = []
    count = 0   # compare the similarity of two transcripts from start to end
    while (count <= abs(len(trans_obs) - len(trans_spk))):
        similarity_list.append(similarity(trans_obs[count:len(trans_spk) + 1], trans_spk))
        count += 1

    position_index = similarity_list.index(max(similarity_list))    # find the most similar transcript
    return position_index, similarity_list  # return the position of transcript


def get_time_delay(alt_obs, alt_spk):
    time_delay_start = alt_obs['words'][0]['startTime'] - alt_spk['words'][0]['startTime']
    time_delay_end = alt_obs['words'][-1]['endTime'] - alt_spk['words'][-1]['endTime']
    return time_delay_start, time_delay_end

def get_min_time_delay(time_delay_list):
    min_abs = abs(time_delay_list[0])
    min_ele = time_delay_list[0]

    for l in time_delay_list:   # keep time delay in positive number
        if abs(l) < min_abs:
            min_abs = abs(l)
            min_ele = l
    
    return min_ele     

def get_file_path(file_pathname):
    path_spk_list = []
    file_pathname = file_pathname + '\\'
    for filename in os.listdir(file_pathname):
        path = os.path.join(file_pathname, filename)
        if 'observer' not in filename:
            if 'new' not in filename:
                if 'meeting.json' in filename: 
                    path_spk_list.append(file_pathname + filename) 
                    print(path_spk_list)
    return path_spk_list    


def main():

    # please set your own path below ↓
    path_spk_list = get_file_path(r"F:\Work\Ernie\sounds_Align\sounds_file")    # Voice file of all people in speaker, which has time delay
    path_obs_list = glob.glob(r"F:\Work\Ernie\sounds_Align\sounds_file\*observer*[!new]meeting_1.json")  # Voice file of all people in obsever, as standard
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
                                                        
                            MAX_TIME_DIFFERENCE = 40    # [changeable] diff of time less than 40 sec
                            if time_diff <= MAX_TIME_DIFFERENCE:
                                pos_idx, similarity_list = find_suit_position(alt_obs['transcript'], alt_spk['transcript'])
                                trans_obs_sub = alt_obs['transcript'][pos_idx:pos_idx + len(alt_spk['transcript'])]
                                transcript_split_value.append(max(similarity_list))
                                transcript_split_word.append(trans_obs_sub)
                                max_value = transcript_split_value.index(max(transcript_split_value))
                                
                                MINIMUM_SIMILARITY = 2/3    # [changeable] similarity of transcript is over than 2/3
                                if similarity(trans_obs_sub, alt_spk['transcript']) > MINIMUM_SIMILARITY:
                                        print('Speaker in observer >>>>',trans_obs_sub)
                                        TDS, TDE = get_time_delay(alt_obs, alt_spk) # TDS = time delay start, TDE = time delay end
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
        
                                        transcript_split_value = []
                                        transcript_split_word = []  # reset word and value list


    path_obs_new = open(path_obs.replace('.json', '_new.json'), 'w', encoding='utf-8')
    json.dump(data_obs, path_obs_new, ensure_ascii=False)

    print('write json to path:', path_obs_new)

if __name__ == '__main__':    
    main()

