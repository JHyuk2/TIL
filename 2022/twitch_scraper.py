from twitch_listener import listener

_user_name = 'whdgurdl77'
_oauth = 'oauth:kci7129gdr09f8mmd4izf74biudl24'
_client_id = '1cu75bp9ugj3q0fu7j8s5wzw7jcia8'

# Connect to Twitch
bot = listener.connect_twitch(_user_name, 
                             _oauth, 
                             _client_id)

# List of channels to connect to
channels_to_listen_to = ['Faker']

# Scrape live chat data into raw log files. (Duration is seconds)
bot.listen(channels_to_listen_to, duration = 60) 

# Convert log files into .CSV format
bot.parse_logs(timestamp = True)

# Generate adjacency matrix
bot.adj_matrix(weighted = False, matrix_name = "streamer_network.csv")