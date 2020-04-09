# Steam Recommender

### WIP

##### Topline
Steam is an application and marketplace that users can purchase video games from. I have queried Steam's API to gather data on 500k users and the games that they have played. This is a recommender system which clusters users together, looks at users with a cluster and recommends games that they haven't played but that are popular within their 

##### Stage 1: Data Gathering
To generate the dataset, we query the Steam API directly. We first pull friends of a known ID (and then friends of friends and so on), and then pull games played by this list of IDs. Due to GDPR you can only pull information on profiles that have a privacy setting of 'public' (and it's 'private' by default).

##### Stage 2: Cluster & Recommendation
Using hashed-user-id and games-played, we create a sparse matrix (rows = users, columns = games, value of 1 = user played game). From there we run KMeans clustering and top games to be recommended are games which most people in their cluster have played, but that they have not.


##### Codes Contents:
queryer.py: contains all the functions used by the other codes.  
query_user_ids.py: takes a .txt of user_ids, finds all friends, and all their friends, and so on, up until a predefined limit.  
query_users_games.py: iterates through each user ID, finds their games, and updates the master dataframe.  
clusterer.ipynb: clusters users together, and make recommendations
