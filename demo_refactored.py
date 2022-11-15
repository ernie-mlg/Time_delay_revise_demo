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
            min_ele = l

    
    return min_ele                               


def main():
    path_obs = (r"./edited_wav/00005_edit/00005_04_observer_kojima_meeting_1.json")      # Voice of all people
    path_spk = (r"./edited_wav/00005_edit/00005_01_onoyama_meeting.json")     # Open local files of one person

    data_obs = json.load(open(path_obs, 'rb'), strict=False)
    data_spk = json.load(open(path_spk, 'rb'), strict=False)

    for res_obs in data_obs['response']['results']:
        for alt_obs in res_obs['alternatives']:

            print('transcript of all:', alt_obs['transcript'])
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
                        i = 0

                        pos_idx, similarity_list = find_suit_position(alt_obs['transcript'], alt_spk['transcript'])
                        trans_obs_sub = alt_obs['transcript'][pos_idx:pos_idx + len(alt_spk['transcript'])]
                        transcript_split_value.append(max(similarity_list))
                        transcript_split_word.append(trans_obs_sub)
                        max_value = transcript_split_value.index(max(transcript_split_value))
                        
                        if similarity(trans_obs_sub, alt_spk['transcript']) > 2 / 3:
                                TDS, TDE = get_time_delay(alt_obs, alt_spk)
                                time_delay_start_list.append(TDS)
                                time_delay_end_list.append(TDE)
                               
                                minele_s = get_min_time_delay(time_delay_start_list)
                                minele_e = get_min_time_delay(time_delay_end_list)
                                
                                alt_obs['time_delay_start'] = minele_s
                                alt_obs['time_delay_end'] = minele_s

                                alt_obs['transcript_split'] = alt_spk['transcript']
                                
                                alt_obs['transcript_list'].append(transcript_split_word[max_value])
                                transcript_split_value = list()    
                                transcript_split_word = list()     # reset word and value list

    path_obs_new = open(path_obs.replace('.json', '_new.json'), 'w', encoding='utf-8')
    json.dump(data_obs, path_obs_new, ensure_ascii=False)

    print('wrote json to:', path_obs_new)

if __name__ == '__main__':    
    main()

