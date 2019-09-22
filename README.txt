Collaborative recommender project in two phases:

Phase 1:
    - Using dataset from Kaggle, group Steam users into clusters based on games played - SILLHOUETTE SCORE .55, BUT ONLY 9K PLAYERS

Phase 2:
    - Generate new dataset by querying Steam's API
        - Gather user ids - COMPLETED - 1.7M USERS
        - Gather games that we are interested in clustering on - COMPLETED - 985 GAMES
        - Gather games played for each user - IN PROGRESS
        - Rerun clustering model on new data set - NOT STARTED
        - Profile clusters - NOT STARTED

---------------------

datafiles directory:
        - idlist.txt: a list of input ids obtained by website scraping - approx 1.7M ids
        - all_ids.csv: the 550K steam user_ids that we will be clustering on
        - game_genres.csv: an output from popular_games.ipynb - all 13K games and their genres.
        - gamesfilter.json: the 985-item-long list of game app_ids, that we will be restricting our clustering to
        - popular_games.csv: 13K games that were played in 2018 - taken from a page on Steam data. Taken from here: https://arstechnica.com/gaming/2018/07/steam-data-leak-reveals-precise-player-count-for-thousands-of-games/
        - steam_200k.csv - the original steam_id/game input file, taken from kaggle - https://www.kaggle.com/tamber/steam-video-games/downloads/steam-video-games.zip/3


Work in progress