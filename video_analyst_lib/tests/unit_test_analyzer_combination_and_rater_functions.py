import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import video_analyst_lib

scoresheet_dataframe = pd.read_csv(
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'input_scoresheet.csv')),
    delimiter='\t')
analysts_to_rate = ['sun_tzu', 'einstein']
questions_to_rate_over = ['war_question']
subject_id_column_name = 'subject'

print(scoresheet_dataframe)
print(video_analyst_lib.rate_analysts_against_eachother(
    scoresheet_dataframe=scoresheet_dataframe,
    analysts_to_rate=analysts_to_rate,
    questions_to_rate_over=questions_to_rate_over,
    subject_id_column_name=subject_id_column_name,
))
