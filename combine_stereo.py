import librosa
import numpy as np
import soundfile as sf
from pathlib import Path

def combine_wav(spk_number, index):
    """
    spk_number: number of spkear.
    index: number of split voice file, which is created by wav_time_change.py
    
    please set your own INPUT path of voice below ↓
    """       
    cwd = Path.cwd()    # read wave files
    channel_path_obs = Path.joinpath(cwd, "transcript_split_obs_1", "obs_" + str (index) + "_.wav") 
    channel_path_spk = Path.joinpath(cwd, "transcript_split_spk_" + str (spk_number) , "spk_" + str (index) + "_.wav")   # Path of new speaker voice file
    
    ch1, sr1= librosa.load(channel_path_obs, sr=1600)        
    ch2, sr2= librosa.load(channel_path_spk, sr=1600)   
    
    rch1_wave_data, rch2_wave_data = length_sync(ch1, ch2)
    
    # A 2D array where the left and right tones are contained in their respective rows
    stereo = np.vstack((rch1_wave_data, rch2_wave_data))   
    # Reshape 2D array so that the left and right tones are contained in their respective columns
    stereo = stereo.transpose()
    
    # please set your own OUTPUT path of voice below ↓    
    DTW_plot_output = str(Path.joinpath(cwd, "DTW_plot", "test_correct_combined_" + str(spk_number))) + '/' + str (index) + '.wav' # Path of stero voice output
    sf.write(DTW_plot_output, stereo, samplerate=1600)
    print(index, "in speaker No.", spk_number, "has finished")
    
def length_sync(ch1, ch2):
    """
    use zero value to sync length
    
    ch1, ch2: two channels of stero sound.
    """
    ch1_len = len(ch1)
    ch2_len = len(ch2)
    length = abs(ch2_len - ch1_len)
    temp_array = np.zeros(length, dtype=np.int16)
    if ch1_len < ch2_len:
        rch1_wave_data = np.concatenate((ch1, temp_array))
        rch2_wave_data = ch2
    elif ch1_len > ch2_len:
        rch2_wave_data = np.concatenate((ch2, temp_array))
        rch1_wave_data = ch1
    else:
        rch1_wave_data = ch1
        rch2_wave_data = ch2
        
    return rch1_wave_data, rch2_wave_data
   
def main():
    TOTAL_SPEAKER = 3   # number of spkear, 3 in this example
    for spk_num in range(1,TOTAL_SPEAKER + 1):  
        TOTAL_SPLIT_VOICE = 84  # number of split voice file, 84 in this example
        for index in range(1,TOTAL_SPLIT_VOICE + 1):   
            combine_wav(spk_num, index)
                
if __name__ == '__main__':    
    main()
    
