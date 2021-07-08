from asyncio.windows_events import NULL
import discord
from discord.ext import commands
import praw
import random as rand
reddit = praw.Reddit(
    client_id= 'my_client_ID',
    client_secret= 'my_Secret_code',
    user_agent='<yea, my thing again>'
    #username = 'floaredorbot',
    #password = 'ramrajkisalute',
)
search_limit = 50
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready(ctx):
    print("Bot is ready af")
    await ctx.send("type `help me` for commands :)")
@client.command()
async def meme(ctx):
    all_subs = []
    #await ctx.send("Here's your meme, take it and leave.")
    subreddit = reddit.subreddit("memes")
    for submission in subreddit.hot(limit=search_limit):
        all_subs.append(submission)
        #print(submission.title)
    random_sub = rand.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    emb = discord.Embed(title = name)
    emb.set_image(url = url)
    await ctx.send(embed = emb)
@client.command()
async def earthme(ctx):
    ball_subs = []
    #await ctx.send("Here's your meme, take it and leave.")
    subreddit = reddit.subreddit("EarthPorn")
    for submission in subreddit.hot(limit=search_limit):
        ball_subs.append(submission)
        #print(submission.title)
    random_sub = rand.choice(ball_subs)
    name = random_sub.title
    url = random_sub.url
    emb = discord.Embed(title = name[0:-16] + " : )")
    emb.set_image(url = url)
    await ctx.send(embed = emb)
@client.command()
async def amongusmeme(ctx):
    ball_subs = []
    #await ctx.send("Here's your meme, take it and leave.")
    subreddit = reddit.subreddit("AmongUsMemes")
    for submission in subreddit.hot(limit=search_limit):
        ball_subs.append(submission)
        #print(submission.title)
    random_sub = rand.choice(ball_subs)
    name = random_sub.title
    url = random_sub.url
    emb = discord.Embed(title = name)
    emb.set_image(url = url)
    await ctx.send(embed = emb)
@client.command()
async def valomeme(ctx):
    ball_subs = []
    #await ctx.send("Here's your meme, take it and leave.")
    subreddit = reddit.subreddit("ValorantMemes")
    for submission in subreddit.hot(limit=search_limit):
        ball_subs.append(submission)
        #print(submission.title)
    random_sub = rand.choice(ball_subs)
    name = random_sub.title
    url = random_sub.url
    emb = discord.Embed(title = name)
    emb.set_image(url = url)
    await ctx.send(embed = emb)
@client.command()
async def music(ctx):
    ball_subs = []
    #await ctx.send("Here's your meme, take it and leave.")
    subreddit = reddit.subreddit("Music")
    for submission in subreddit.hot(limit=20):
        ball_subs.append(submission)
        #print(submission.title)
    random_sub = rand.choice(ball_subs)
    name = random_sub.title
    url = random_sub.url
    emb = discord.Embed(title = name)
    emb.set_image(url = url)
    await ctx.send(embed = emb)
@client.command()
async def synthhelp(ctx, type):
    subreddit = reddit.subreddit("synthrecipes")
    for submission in subreddit.hot(limit = 10):
        if type in submission.title.lower():
            if submission.comments != NULL:
                await ctx.send(submission.title)
                for comment in submission.comments:
                    if hasattr(comment, "body"):
                        comment_lower = comment.body.lower()
                        #print("-----------")
                        ctx.send(comment.body)

@client.command()
async def helpme(ctx):
    await ctx.send('''earthme - to let fleury take your breath away
meme - for memes
amongusmeme - for among us memes :)
valomeme - for valorant memes :)
synthhelp - for virtual synthesizer help : )''')
client.run("I shouldnt be revealing the run code")
