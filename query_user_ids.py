
from queryer import QueryApi
import time
import keyring

password = keyring.get_password(service_name = 'steam', username = 'IcyJoseph')
api = QueryApi(password) # connect and authenticate

# pulling friends from a known id, then pulling friends of each friend, and so on

number_ids_you_want = 2000000

with(open('datafiles/idlist.txt', mode = 'r')) as file:
    input_ids = file.read()

input_ids = input_ids.replace("'","")
input_ids = input_ids.replace("[","")
input_ids = input_ids.replace("]","")
input_ids = input_ids.split(", ")

counter_start = 0
num_runs = 1
all_ids = list()

while len(all_ids) < number_ids_you_want and counter_start != len(input_ids):
    
    counter_end = counter_start+100 # the steam api can accept up to 100 steam ids at once, so we'll give it 100...
    
    if counter_end > len(input_ids): # ... or as many as we can if we don't have 100
        counter_end = len(input_ids)
        
    id_string = [i+"," for i in input_ids[counter_start:counter_end]] # pull out the ids from our list
    ids = "".join(id_string) # and concatenate them all into one string
        
    time.sleep(3)
        
    steam_ids = api.find_friends(ids) # query API
        
    all_ids.extend(steam_ids) # adds public ids to output list
    all_ids = list(set(all_ids)) # unique values
    
    input_ids.extend(steam_ids) # adds the friends just pulled to the list of ids to iterate through, so we can keep pulling
    input_ids = list(set(input_ids))
    
    print(f"running from {counter_start} to {counter_end}, input_ids is "+str(len(input_ids))+" items long")
    
    counter_start = counter_end
    num_runs += 1

id_df = pd.DataFrame(data = {'id':all_ids,'games_played':''}) # games_played will be populated in the next code
id_df.to_csv('datafiles/all_ids.csv', index = False) # export steam ids to csv