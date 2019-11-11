# Steam Recommender

### WIP

##### Topline
We use a KMeans clustering model to group Steam users together based on the games that they have played, and then recommend to them they games that they haven't played, but their cluster has.

##### Stage 1: Query API
To generate the dataset, we query the Steam API directly. There are two stages: stage one - create a list of user IDs by querying friends of a known user ID. Stage 2 - query games played for each user ID.

##### Stage 2: Cluster Users
Convert games played into dummy variables, so we have approximately 1,000 features. Using a KMeans model we group users together based on the games that they played.

##### Stage 3: Recommend games
We rank the games for each cluster by the number of users that have played it. Then we recommend for each user the games in their cluster that they haven't played, in order of descending popularity.

##### Codes Contents:
queryer.py: contains all the functions used by the other codes.
query_user_ids.py: takes a .txt of user_ids, finds all friends, and all their friends, and so on, up until a predefined limit.
query_users_games.py: iterates through each user ID, finds their games, and updates the master dataframe.
clusterer.ipynb: clusters users together
