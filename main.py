from asyncio.tasks import wait
from asyncio.windows_events import NULL
import discord
from discord.ext import commands
import praw
import random as rand
import asyncio
import speech_recognition as sr
import pyttsx3
import webbrowser
import requests as req
from youtubesearchpython import VideosSearch
from bs4 import BeautifulSoup
from pynput.keyboard import Controller,Key
from googletrans import Translator
from gtts import gTTS
import os
html_text = req.get("https://developers.google.com/admin-sdk/directory/v1/languages").text
soup = BeautifulSoup(html_text, 'lxml')
langs = soup.findAll('td')
lang_Codes = []
for lang in langs:
    lang_Codes.append(lang.text.lower())
trans = Translator()
reddit = praw.Reddit(
    client_id= 'mQiQTwEKfmKtDSWq0jHzyg',
    client_secret= 'DrZG-CKbOkkGAzhSp59B5X3zAYu0tQ',
    user_agent='<console:FLOARE:1.0>'
    #username = 'floaredorbot',
    #password = 'ramrajkisalute',
)
search_limit = 50
client = commands.Bot(command_prefix = ">")

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
async def synthhelp(ctx,*, arg):
    subreddit = reddit.subreddit("synthrecipes")
    for submission in subreddit.hot(limit = search_limit):
        if str(arg).lower() in submission.title.lower():
            if submission.comments != NULL:
                await ctx.send(embed = discord.Embed(title = submission.title))
                for comment in submission.comments:
                    if hasattr(comment, "body"):
                        comment_lower = comment.body.lower()
                        #print("-----------")
                        await ctx.send(comment.body)
@client.command()
async def quoteme(ctx):
    ball_subs = []
    #await ctx.send("Here's your meme, take it and leave.")
    subreddit = reddit.subreddit("quotes")
    for submission in subreddit.hot(limit=search_limit):
        ball_subs.append(submission)
        #print(submission.title)
    random_sub = rand.choice(ball_subs)
    name = random_sub.title
    url = random_sub.url
    emb = discord.Embed(title = name)
    #emb.set_image(url = url)
    await ctx.send(embed = emb)

@client.command()
async def t(ctx,*,arg):
    temp = str(arg)
    lang_text = temp.split("to ")[1]
    index = lang_Codes.index('english (us)')
    if lang_text in lang_Codes:
        index = lang_Codes.index(lang_text)
    code = lang_Codes[index+1]
    final = temp.split("to ")[0]
    src_code = trans.detect(final).lang
    #final = final.replace("translate", "")
    #trans = Translator()
    t = "yes"
    try:
        t = trans.translate(final, src = src_code, dest = code)
    except AttributeError:
        await ctx.send("oops")
    if final == "fuck you":
        await ctx.send("no, fuck you!")
    else:
        await ctx.send(t.text)
    #output = ''
    #for word in args:
    #   output += word
    #    output += ' '
    #await client.send(output)

@client.command()
async def helpme(ctx):
    await ctx.send('''earthme - to let fleury take your breath away
meme - for memes
amongusmeme - for among us memes :)
valomeme - for valorant memes :)
synthhelp - for virtual synthesizer help''')
client.run("ODYyNzM0NzgyOTE5NzM3Mzg1.YOcqYQ.RbFeN9evFEeuH0O_45KSKPaBr_U")
