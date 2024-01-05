import pandas as pd
from result_collector import final_results
from give_me_q import q_generator
import time
import sys

def main(sport):
    try:
        print('----------------Excecution Begins----------------')
        name_list=q_generator(sport)
    except Exception as e:
        print(f'Error in reading list: {e}')
    else:
        results = final_results(name_list,sport)
        print('---------------Excecution Complete---------------')

if __name__ == "__main__":
  sport = sys.argv[1]
  main(sport)