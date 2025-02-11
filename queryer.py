
# import pandas as pd
# import numpy as np
import requests
from requests.exceptions import ConnectionError
# import keyring
import json

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
    
    
    def get_game_info(self, app_id):
        
        'Returns info on a game/app - requires an app id'
        
        response = requests.get(f'http://steamspy.com/api.php?request=appdetails&appid={app_id}')
            
        return json.loads(response.content)
    
    
    def find_friends(self, steam_id):

        'returns a list of all friends for a steam_id. Uses the get_friends() function. Returns dict'
        
        response = requests.get(
            f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={self.api_key}&steamid={steam_id}&relationship=friend')
        
        friend = json.loads(response.content) # query steam api
        try:
            all_friends = [i['steamid'] for i in friend['friendslist']['friends']] # pick out steam ids from returned dictionary
            return all_friends
        
        except KeyError:
            return []        
    
    
    def get_users_games(self,steam_id):
        
        'returns a list of all games played by a user. Returns dict'
        try:
            response = requests.get(
                f"""http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.api_key}&steamid={steam_id}
                        &format=json&include_appinfo=true""")

            gamedata = json.loads(response.content)

            all_games = [(i['appid'], i['name']) for i in gamedata['response']['games']]
            
        except ConnectionError:
            raise ConnectionError

        return all_games