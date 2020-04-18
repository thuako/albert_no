import telepot
from telepot.loop import MessageLoop
import pandas as pd


my_bot = telepot.Bot('712595804:AAHJZhoIQuMlxwDlW1HpPTY7gstFmc44y20')  # give bot a token

filename = "tmdb_5000_movies.csv"
# read the file
df = pd.read_csv(filename, encoding='utf-8')

# Find the best vote_average movie
vote_count_idx = (df['vote_count'] > 1000)
df_short = df[vote_count_idx]
df_short_sort = df_short.sort_values(by='vote_average', ascending=False)


def action(msg):
    chat_id = 898518917
    msg_txt = msg['text']  # get text of message
    for i in range(int(msg_txt)):
        row = df_short_sort.iloc[i, :]
        movie_title = row['title']
        msg_back = f'{i+1}th movie: {movie_title}'
        my_bot.sendMessage(chat_id, msg_back)
        print(msg_back)


MessageLoop(my_bot, action).run_as_thread()  # checking message in the background
print('Up and Running....')

while True:
    pass  # keep running the code