import editdistance

alt_1 = {}
alt = {}
alt_1['transcript'] = "音声を読み上げた、えっと、その読み読み上げるなんだろう台本とえーっとそのそれを読み上げたWAVファイルのセットをセットにしてデータにして、なんかパッケージにできるみたいなといった、その学習用のデータを収集するアプリの開発についてはここかなとえ思っています。"
alt['transcript'] = "セリフ台本台本とえーっとそのそれを読み上げたWAVファイルのセットをセットにしてデータにして、なんかパッケージにできるみたいな。"
alt['transcript_split'] = "音声を読み上げた、えっと、その読み読み上げるなんだろう"
# alt['words']['startTime'] = 325.41
# alt['words']['word'] = "音声"

#生成一个字典
d = {
    "session_id": "b4c9389d38d647ac8be690e9658f3c44",
    "metadata": {
        "model": "assets.ja.goi_addr.v8.0318.k2graph",
        "startTime": "2022-09-05T05:46:47.451627",
        "updateTime": "2022-09-05T05:51:51.238527",
        "remove_filler": "off",
        "convert_numbers": "on",
        "punctuate": "on",
        "summary": "off"
    },
    "done": "true",
    "response": {
        "results": [
            {
                "alternatives": [
                                        {
                        "transcript": "音声を読み上げたえーっとその読み読み上げるなんだろう。",
                        "filler_transcript": "音声を読み上げたえーっとその読み読み上げるなんだろう。",
                        "speech_info": {
                            "intonation": 20.510408403327947,
                            "speed": 3.346203346203354,
                            "duration": 7.769999999999982
                        },
                        "pitch_info": [
                            {
                                "vowels_num": 26,
                                "duration": 7.769999999999982,
                                "speed": 3.346203346203354,
                                "pitch_ave": 129.83241192307693,
                                "pitch_delta_ave": 22.50704059391672
                            }
                        ],
                        "words": [
                            {
                                "startTime": 325.41,
                                "endTime": 325.92,
                                "word": "音声",
                                "pitch": [
                                    [
                                        325.41,
                                        325.5,
                                        "o",
                                        167.9442,
                                        22.57697442668006
                                    ],
                                    [
                                        325.5,
                                        325.65,
                                        "N",
                                        146.7849,
                                        22.518844154074007
                                    ],
                                    [
                                        325.74,
                                        325.83,
                                        "e",
                                        155.063,
                                        22.46166244141839
                                    ],
                                    [
                                        325.83,
                                        325.92,
                                        "i",
                                        146.7849,
                                        22.403673118429875
                                    ]
                                ],
                                "is_filler": "false",
                                "confidence": 1.0
                            },
                            {
                                "startTime": 325.92,
                                "endTime": 326.01,
                                "word": "を",
                                "pitch": [
                                    [
                                        325.92,
                                        326.01,
                                        "o",
                                        130.2255,
                                        22.345000529391896
                                    ]
                                ],
                                "is_filler": "false",
                                "confidence": 1.0
                            },
                            {
                                "startTime": 326.01,
                                "endTime": 326.58,
                                "word": "読み上げ",
                                "pitch": [
                                    [
                                        326.07,
                                        326.16,
                                        "o",
                                        138.2575,
                                        22.302191848321844
                                    ],
                                    [
                                        326.19,
                                        326.31,
                                        "i",
                                        130.2255,
                                        22.32165436423814
                                    ],
                                    [
                                        326.31,
                                        326.4,
                                        "a",
                                        116.1118,
                                        22.340950563337724
                                    ],
                                    [
                                        326.46,
                                        326.58,
                                        "e",
                                        107.2061,
                                        22.360538512813957
                                    ]
                                ],
                                "is_filler": "false",
                                "confidence": 0.9821610331193384
                            },
                            {
                                "startTime": 327.09,
                                "endTime": 327.45,
                                "word": "た",
                                "pitch": [
                                    [
                                        327.18,
                                        327.45,
                                        "a",
                                        130.8766,
                                        22.37861861610739
                                    ]
                                ],
                                "is_filler": "false",
                                "confidence": 1.0
                            },
                            {
                                "startTime": 329.0,
                                "endTime": 329.2,
                                "word": "えーっと",
                                "pitch": [
                                    [
                                        328.83,
                                        329.01,
                                        "e:",
                                        126.3862,
                                        22.397777932886743
                                    ],
                                    [
                                        329.07,
                                        329.16,
                                        "o",
                                        130.8766,
                                        22.416973201614105
                                    ]
                                ],
                                "is_filler": "false",
                                "confidence": 0.9323938196280732
                            },
                            {
                                "startTime": 329.2,
                                "endTime": 329.68,
                                "word": "その",
                                "pitch": [
                                    [
                                        329.22,
                                        329.28,
                                        "o",
                                        121.4426,
                                        22.436348811541148
                                    ],
                                    [
                                        329.37,
                                        329.64,
                                        "o",
                                        123.2734,
                                        22.458954878924548
                                    ]
                                ],
                                "is_filler": "false",
                                "confidence": 0.9792189648466981
                            },
                            {
                                "startTime": 330.03,
                                "endTime": 330.39,
                                "word": "読み",
                                "pitch": [
                                    [
                                        330.12,
                                        330.18,
                                        "o",
                                        142.4574,
                                        22.482572657975226
                                    ],
                                    [
                                        330.24,
                                        330.39,
                                        "i",
                                        138.9488,
                                        22.50934805508841
                                    ]
                                ],
                                "is_filler": "false",
                                "confidence": 1.0
                            },
                            {
                                "startTime": 330.39,
                                "endTime": 331.35,
                                "word": "読み上げる",
                                "pitch": [
                                    [
                                        330.48,
                                        330.57,
                                        "o",
                                        154.2915,
                                        22.536320442409554
                                    ],
                                    [
                                        330.6,
                                        330.72,
                                        "i",
                                        155.8383,
                                        22.56326434526901
                                    ],
                                    [
                                        330.72,
                                        330.81,
                                        "a",
                                        170.476,
                                        22.58921287402311
                                    ],
                                    [
                                        330.87,
                                        330.96,
                                        "e",
                                        188.3582,
                                        22.61404181982986
                                    ],
                                    [
                                        331.02,
                                        331.35,
                                        "u",
                                        165.4501,
                                        22.638609711999955
                                    ]
                                ],
                                "is_filler": "false",
                                "confidence": 1.0
                            },
                            {
                                "startTime": 332.76,
                                "endTime": 333.18,
                                "word": "なんだろう",
                                "pitch": [
                                    [
                                        332.88,
                                        332.94,
                                        "a",
                                        87.3798,
                                        22.660040919736467
                                    ],
                                    [
                                        332.94,
                                        332.97,
                                        "N",
                                        75.61279,
                                        22.679094539975218
                                    ],
                                    [
                                        333.03,
                                        333.06,
                                        "a",
                                        63.50137,
                                        22.70414581479484
                                    ],
                                    [
                                        333.09,
                                        333.15,
                                        "o",
                                        74.48985,
                                        22.727419860176752
                                    ],
                                    [
                                        333.15,
                                        333.18,
                                        "u",
                                        87.3798,
                                        22.75882100077648
                                    ]
                                ],
                                "is_filler": "false",
                                "confidence": 0.9920319144601087
                            },
                            {
                                "startTime": 333.18,
                                "endTime": 333.18,
                                "word": "。",
                                "pitch": [],
                                "is_filler": "false",
                                "confidence": 1.0
                            }
                        ],
                        "transcript_split": "音声を読み上げた、えっと、その読み読み上げるなんだろう"}]
                        }]}}

word_number = []
for res in d['response']['results']:
    for alt in res['alternatives']:
        for words in alt['words']:
            print(words['word'])
            word_number.append(len(words['word']))
        print (word_number)
        j = 0   # j = position
        k = 0   # Word list position
        while (len(alt['transcript']) > j):
            j += word_number[k]
            k += 1          
        print ("end time is", alt['words'][k-1]['endTime'], "\nword is (", alt['words'][k-1]['word'], ")")

print ("length is ", len(word_number))

        # #打印返回值，其中d.keys()是列出字典所有的key
        # if 'time_delay_start' in alt:
        #     print ("yes")
        # else:
        #     print ("No")
        # #两个的结果都是返回True
