#!/usr/bin/env python3

import tweepy
import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv
import logging

# Set up logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='/tmp/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Grab stuff from the .env file
load_dotenv()

TOKEN = os.getenv("DIS_TOKEN")
GUILD_ID = os.getenv("DIS_GUILD")
BEARER = os.getenv("TWI_BEARER")
TEST_CHANNEL = os.getenv("TEST_CHANNEL")
IKDY_SEARCH_QUERY = "from:updates_henry"

# Set up the Discord API stuff
intents = disnake.Intents.default()
#intents.message_content = True
print("Intents set")

try:
    print("Getting Discord API")
    bot = commands.InteractionBot(intents=intents, test_guilds=[int(GUILD_ID)])
except:
    print("Discord API access went sideways")
else:
    print("Discord API get")

# Set up the Twitter API stuff
try:
    print("Getting Twitter API", BEARER)
    twi_client = tweepy.Client(bearer_token=BEARER)
except:
    print("Twitter API access went sideways")
else:
    print("Twitter API get")

def get_last_tweet():
    tweets = twi_client.search_recent_tweets(query=IKDY_SEARCH_QUERY, max_results=10)
    return tweets.data[0]

@bot.slash_command(
    name="ping",
    description="respond when called",
)
async def ping(inter):
    if inter.channel.id != TEST_CHANNEL:
        return
    await inter.response.send_message("pong")

@bot.slash_command(
    name="ishedead",
    description="Is the USA's favorite lich banished from this realm yet?",
)
async def ishedead(inter):
    try:
        tweet = get_last_tweet()
    except:
        await inter.response.send_message("something's fucked on the bot backend")
    #print(tweet.user.screen_name)
    #dead_url = "https://twitter.com/{}/status/{}".format(tweet.user.screen_name,tweet.id)
    #dead_embed = disnake.Embed(url=str(tweet))
    else:
        await inter.response.send_message(tweet)

#@bot.listen('on_message')
#async def on_message(message):
#    if message.channel.id != 951635682399494154:
#        return
#
#    if message.content == "hi ikdb-test":
#        await message.channel.send("hi friend")
#
#    print(message.content)

bot.run(TOKEN)
