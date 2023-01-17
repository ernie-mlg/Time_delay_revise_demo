# Time_delay_revise_demo


-------------2023-Jan.13----Update-------------

    21. DTW_demo now avaliable at lots of situations

-------------2023-Jan.13----Update-------------

    HAPPY NEW YEAR!
    20. Use transcript time revise for 1st step, DTW as 2nd step

------------------Dec.16----Update-------------

    19. New spk data were not sync well

------------------Dec.14----Update-------------

    17. DTW_demo created and start to test.
    18. Splited transcript still have some error.

------------------Dec.8----Update-------------

    15. Splited wav file into several different transcripts by new wav_time_change.py program
    16. Try to compare obs file with spk file

------------------Nov.24----Update-------------


    13. Start to use codespace
    14. Start to learn Dynamic Time Warping
    

------------------Nov.18----Update-------------

 
    12. read other speaker file by glob and for loops.
    

------------------Nov.17----Update-------------

It's a great honor for me that Miss shiori-w joined this issue today.

------------------Nov.15----Update-------------

demo_refactored was created.

------------------Nov.14----Update-------------
 
 
    11. Need to reset transcript_split_value after one pair finished
    
       
------------------Nov.11----Update-------------
  
  
    10. Onoyama's short transcript cannot pair with Kojima's long transcript
    
       
------------------Nov.10----Update-------------


    9. Creat a word and time list for observer(kojima) file.

Old project changed.
    
------------------Nov.8----Update-------------


    8. Find the end word and time difference between transcript_split in onoyama file and kojima file. 
    
New demo file "split_word_time.py" updated.

------------------Nov.1----Update-------------


    7. Find the time difference between transcript_split in onoyama file and kojima file. 

------------------Oct.31----Update-------------

Problem 5 fixed. Different transcript has paired.

    6. Calculation of time difference for long transcript. 

------------------Oct.28----Update-------------

Problem:

Problem 4. fixed. 

    5. If the transcript is way more longer than the other one, 
       for example transcript A have others vioce, time difference cannot be calculated.

------------------Oct.21----Update-------------

Problem:
    
    4. If the contents have a little bit error, time difference cannot be calculated.

-------------------Oct.20-------------------------------

Oct.20 first edition, still have some problems 
  
The value of key "time_delay_start" and "time_delay_end" can be correctly output at the end of "alternatives" list.

Problems:

    1. In new json file, all the value of time delay were output at the top first lane.
    2. In new json file, the value of transcript and word were output in Unicode.
    3. Key before alternatives are lost.

