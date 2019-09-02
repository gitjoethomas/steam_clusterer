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

class QueryApi():
    '''
    Contains several functions for querying steam's api. Requires an API key to instantiate
    
    get_player_info(steam_id) - basic info on a player. Returns a response object
    get_friends(steam_id) - gets all public friends for a steam id. the id you supply can actually be a list of ids, separated by commas
    find_all_friends(steam_id) - uses the above function and separates the steam ids into a list, and returns that
    get_games(steam_id) - returns all games played by the steam_id, returns a response object
    users_games(steam_id) - pulls out the names of the games played by a single steam_id. Pretty slow
    '''
    
    def __init__(self, api_key):
        
        self.api_key = api_key
        
        response = requests.get(f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={self.api_key}&steamids=blank')
        
        if response:
            print("Successfully connected to the Steam API")
        else:
            print("Connection unsuccessful - API key rejected")
    

    def get_player_info(self, steam_id):
        'Returns basic info on a player, in a response object'
        
        response = requests.get(
            f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={self.api_key}&steamids={steam_id}')
        
        return response
    
    
#     def get_game_info(self, app_id)
        
#         'Returns info on a game/app - requires an app id'
        
#         response = requests.get(
#             f'http://api.steampowered.com/ISteamUserStats/GetGlobalStatsForGame/v0001/?format=xml&appid={appid}&count=1&name[0]=global.map.emp_isle'
            
#         return response

    def get_friends(self, steam_id):
        
        'gets all friend-related data for a steam id. the id you supply can actually be a list of ids, separated by commas'
        
        response = requests.get(
            f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={self.api_key}&steamid={steam_id}&relationship=friend')
        
        return response
    
    
    def find_all_friends(self, steam_id):

        'returns a list of all friends for a steam_id. Uses the get_friends() function.'
        
        friends = get_friends(steam_id) # query steam api

        splitfriends = str(friends.content).split('"')
        all_friends = [i for i in splitfriends if i.isnumeric() == True] # items which are all numeric are steam_ids

        return all_friends
    
    
    def get_users_games(self, steam_id):
        
        'returns a list of all games played by a user. This is very slow - needs work'
        
        response = requests.get(
            f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.api_key}&steamid={steam_id}&format=json')

        gametext = get_games(steam_id)

        # re.finditer returns an iterator object, so we have to use list comprehension to get the index at which the game 
        # names begin
        gamestart = [i.end() for i in re.finditer('name":"',str(response.content))]

        gamelist = []

        for start_index in gamestart: # we're pulling out the names of games for each user_id. This is very slow - needs work

            end_index =  re.search('",',str(newgames.content)[start_index:])
            end_index = end_index.start()

            game = str(newgames.content)[start_index:start_index+end_index]

            gamelist.append(game)

        return gamelist