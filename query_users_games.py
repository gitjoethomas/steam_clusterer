
import pandas as pd
from queryer import QueryApi
from requests.exceptions import ConnectionError
# import keyring
import time
import logging

                                                    ##### SETUP #####

log = logging.getLogger()
log.setLevel(logging.INFO)
log.addHandler(logging.FileHandler('query_games.log', mode = 'w+'))

password = keyring.get_password(service_name = 'steam', username = 'IcyJoseph')
api = QueryApi(password) # instantiate and authenticate


                                                    ##### IMPORT #####

# import ids to pull games for
all_ids = pd.read_csv('datafiles/all_ids.csv', index_col = 'id', keep_default_na = False, dtype = {'games_played':str}) 
# just the 1,000 games we're interested in - to keep features low
gamesfilter = pd.read_csv('datafiles/gamesfilter.csv')
    
ids_still_to_query = all_ids[all_ids['games_played'] == ''].copy()

total_ids = all_ids.shape[0]
ids_to_go = ids_still_to_query.shape[0]
progress = round(ids_to_go / total_ids, 1)

log.info(f"we are {progress}% done")

if len(ids_still_to_query) >= 1000:
    ids_still_to_query = ids_still_to_query[:1000]
    
ids_to_run = list(ids_still_to_query.index) # only going to run on the ids we haven't run on yet


                                                ##### DO THE ACTUAL QUERYING #####


for id_num in ids_to_run:
    try:
        newgames = api.get_users_games(id_num) # get all games
        restrictedgames = [i for i in newgames if i[0] in gamesfilter['app_id']] 
                                            # just the 1,000 most important games - otherwise it'll be too many features
        game_names = [i[1] for i in restrictedgames]

        all_ids.at[id_num,'games_played'] = game_names
        log.info(game_names)
        
#     except KeyError:
#         all_ids.at[id_num,'games_played']= 'no games'
#         game_names = 'no games'
#         log.info(game_names)
#         continue
        
    except Exception as e:
        all_ids.at[id_num,'games_played']= 'no games'
        log.info("no games")
        continue
        
    finally:
        time.sleep(5)

all_ids.to_csv(f'datafiles/all_ids.csv')