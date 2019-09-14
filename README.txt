The objective of this project is to cluster Steam gamers together, in order to recommend them games based off what they and their friends have played in the past. The steps are as follows:

1) Find active Steam IDs by querying Steam's API - COMPLETE
2) KMeans clustering to understand groups better. - IN PROGRESS. INITIAL SILHOUETTE SCORE - 0.55 - GOOD START, COULD BE BETTER.
3) Profiling and automated recommender system. - NOT YET BEGUN

clusterer.ipynb: KMeans clustering model
feature_selection.ipynb: Pulls Steam user_ids by querying friends of friends of friends etc.
popular_games.ipynb: takes 13k games played in 2018, queries their genres, then reduces size to 1K games, taking care to maintain the proportional size of each genre
queryer.py: The query class that contains functions for querying friends and game stats. It is used in all other notebooks

datafiles directory:
        - all_ids.csv: the 550K steam user_ids that we will be clustering on
        - game_genres.csv: an output from popular_games.ipynb - all 13K games and their genres.
        - gamesfilter.json: the 985-item-long list of game app_ids, that we will be restricting our clustering to
        - popular_games.csv: 13K games that were played in 2018 - taken from a page on Steam data. Taken from here: https://arstechnica.com/gaming/2018/07/steam-data-leak-reveals-precise-player-count-for-thousands-of-games/
        - steam_200k.csv - the original steam_id/game input file, taken from kaggle - https://www.kaggle.com/tamber/steam-video-games/downloads/steam-video-games.zip/3


Work in progress