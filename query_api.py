#!/usr/bin/env python
# coding: utf-8

# In[1]:


# this could be a class, instantiated with the user's steam key to connect to the api


# In[2]:


import pandas as pd
import numpy as np
import requests
import keyring
from IPython.display import clear_output


# In[3]:


# keyring.set_password('steam',username = 'IcyJoseph',password = 'E0152C2E7BF8A5AA0361A4DADCCE2287') # password config
# keyring.get_password('steam', 'IcyJoseph')


# In[18]:


number_ids_you_want = 1000000 # how many unique steam ids do you want? the API queryer will stop when it has more than
                              # this many


# In[5]:


password = keyring.get_password(service_name = 'steam', username = 'IcyJoseph')
steam_id = '76561198985648791' # this is my steam_id
new_id = '76561198020258797' # this is an ID I got from reddit - here:
#                             https://www.reddit.com/r/Steam/comments/68yr8k/building_a_big_list_of_steam_ids_hit_me_up_if_you/


# In[6]:


file = open('steam_ids', mode = 'r')# read in file
user_ids = file.read()
user_ids = user_ids.replace(" ","") # cleaning
user_ids = user_ids[1:-1].split(",")
user_ids = pd.DataFrame({'user_id':user_ids})

# user_ids.head()


# In[7]:


def get_player_info(steam_id):
    
    response = requests.get(
        f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={password}&steamids={steam_id}')
    return response


# In[8]:


def get_friends(steam_id):
    # returns basic profile information
    response = requests.get(
        f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={password}&steamid={steam_id}&relationship=friend')
    return response


# In[9]:


def get_games(steam_id):
    # returns basic profile information
    response = requests.get(
        f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={password}&steamid={steam_id}&format=json')
    return response


# In[10]:


# me = get_player_info(steam_id)
# friends = get_friends(steam_id)
# games = get_games(steam_id)


# In[11]:


# me.content # my profile info


# In[12]:


# friends.content # i have no friends


# In[13]:


# games.content # i only have one game. need to get a lookup from appid to name of game (it's middle earth: shadow of mordor)


# In[14]:


# next steps:
    # get list of active steam_ids (scraping forum?)
    # find a lookup from appid to game name
    # create function that takes friend's steam_id as an input and returns their top (5? 10?) played games
    # pull some sort of info on players


# In[15]:


# takes a steam_id and returns all the id's friends
def find_all_friends(steam_id):
    
    friends = get_friends(steam_id) # query steam api

    splitfriends = str(friends.content).split('"')
    all_friends = [i for i in splitfriends if i.isnumeric() == True] # items which are all numeric are steam_ids
    
    return all_friends


# In[ ]:


# need to get a list of active steam ids. 
# I'm pulling friends own a known popular ID, then pulling friends of each friend, and so on until I get 1M IDs

counter_start = 0
all_ids = list()
all_ids.append(new_id)

while len(all_ids) < number_ids_you_want and counter_start != len(all_ids):
    
    counter_end = counter_start+100 # the steam api can accept up to 100 steam ids at once, so we'll give it 100...
    
    if counter_end > len(all_ids): # ... or as many as we can if we don't have 100
        counter_end = len(all_ids)
        
    id_string = [i+"," for i in all_ids[counter_start:counter_end]] # pull out the ids from our list
    ids = "".join(id_string) # and concatenate them all into one string
    
    steam_ids = find_all_friends(ids)
    
    all_ids.extend(steam_ids) # adds the friends pulled to the list of ids to iterate through, so we can keep pulling friends
    all_ids = set(all_ids)
    all_ids = list(all_ids)
    
    clear_output()
    print("all_ids is "+str(len(all_ids))+" items long")
    
    counter_start = counter_end


# In[17]:


file = open('all_steam_ids', mode = 'w+') # in the future, the lookup will just be a function i'll import and call
file.write(str(all_ids))

