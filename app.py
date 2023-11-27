import pandas as pd
from result_collector import final_results
from give_me_q import q_generator

try:
    print('----------------Excecution Begins----------------')
    name_list=q_generator()
except Exception as e:
    print(f'Error in reading list: {e}')
else:
    results = final_results(name_list)
    print('---------------Excecution Complete---------------')