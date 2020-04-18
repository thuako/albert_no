import telepot
from telepot.loop import MessageLoop
import pandas as pd


my_bot = telepot.Bot('712595804:AAHJZhoIQuMlxwDlW1HpPTY7gstFmc44y20')  # give bot a token

filename = "tmdb_5000_movies.csv"
# read the file
df = pd.read_csv(filename, encoding='utf-8')


def action(msg):
    chat_id = 898518917
    msg_txt = msg['text']  # get text of message
    msg_list = msg_txt.split()

    if len(msg_list) == 2:
        vote_count_lim = int(msg_list[1])
    else:
        vote_count_lim = 1000

    # Find the best vote_average movie
    vote_count_idx = (df['vote_count'] > vote_count_lim)
    df_short = df[vote_count_idx]
    df_short_sort = df_short.sort_values(by='vote_average', ascending=False)

    movie_rank = int(msg_list[0])
    row = df_short_sort.iloc[movie_rank-1, :]
    movie_title = row['title']
    msg_back = f'{movie_rank}-th movie: {movie_title}'
    my_bot.sendMessage(chat_id, msg_back)
    print(msg_back)


MessageLoop(my_bot, action).run_as_thread()  # checking message in the background
print('Up and Running....')

while True:
    pass  # keep running the code