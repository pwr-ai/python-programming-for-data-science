import praw
import streamlit as st
import statsd

stats = statsd.StatsClient('graphite', 8125)

stats.incr('random_reddit_memes.spawned')

reddit = praw.Reddit(client_id='WdgsSyHEDgL8_g',
                     client_secret='Mqs5rCsVze9iNM3QrmqjXDNulCBYxg', 
                     password="aaa111bbb222",
                     user_agent='meme_displayer',
                     username='SecretCauliflower665')

subreddit_name = st.radio('What kind of memes do you like?', ['meme', 'aww', 'funny', 'polandball', 'MemesIRL'])

memes_count = st.slider("How many memes you want to see?", 1, 10)

subreddit = reddit.subreddit(subreddit_name)

for i in range(memes_count):
   stats.incr('random_reddit_memes.requests')
   meme = subreddit.random()
   
   if meme is not None:
      st.image(meme.url)



