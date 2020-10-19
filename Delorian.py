import discord
import string
import random as r
from discord.ext import commands
from discord.utils import get
import asyncio
import pymongo
from pymongo import MongoClient
from bs4 import BeautifulSoup
from asyncio import sleep
import asyncio
import requests
import re
from discord import Activity, ActivityType
import os
import csv
import sys

prefix = "!"
bot_name = "DeLorian [МЗ]"
version = "2.1"
author = "Картавый"


client = commands.Bot(command_prefix = prefix, intents = discord.Intents.all())
@client.remove_command('help')

@client.event
async def on_ready():
	print(f'Logged in as {bot_name} Версия: {version} Автор: {author}')
	channel = client.get_channel(746443271999455323)# получаем айди канала
	await channel.send(embed = discord.Embed(description = '**Бот успешно перезагружен**'))
	while True:
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Палому"))
		await asyncio.sleep(10)
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="за палатами"))
		await asyncio.sleep(10)
		await client.change_presence(activity = discord.Game('Следящего за Министреством Здравоохранения'))
		await asyncio.sleep(10)

#Чистка чата
@client.command()
@commands.has_permissions( administrator = True )
async def clear( ctx, amout = 70 ):
    await ctx.channel.purge(limit=1)
    await ctx.channel.purge( limit=amout )

cluster = MongoClient("mongodb+srv://warn:jmAwgw1DQOQdPc9c@cluster0.tmzus.mongodb.net/warn?retryWrites=true&w=majority")
db = cluster["warn"]
collusers = db["users"]


#Больницы ЛС Выдача старшего состава
@client.command()
@commands.has_any_role(746117981930782852,746117984686178414,746117985873297469,746117987915792385)  #Следак/Министр/Лидер БЛС/Зам БЛС
async def sbls(ctx, member: discord.Member):
    sbls_role = discord.utils.get(ctx.message.guild.roles, id = 746846011556757575) #БЛС Старший
    sbsf_role = discord.utils.get(ctx.message.guild.roles, id = 746846015901925407) #БСФ Старший
    sblv_role = discord.utils.get(ctx.message.guild.roles, id = 746761946375651348) #БЛВ Старший
    bls_role = discord.utils.get(ctx.message.guild.roles, id = 746120147588087931) #БЛС Младщий
    bsf_role = discord.utils.get(ctx.message.guild.roles, id = 746120252529573958) #БСФ Младщий
    blv_role = discord.utils.get(ctx.message.guild.roles, id = 746120251313356922) #БЛВ Младщий       
    stsf_channel = ctx.message.channel
    fasfasfas = client.get_channel(761350595873341471)
    if fasfasfas == stsf_channel:
        if not sbls_role in member.roles:
          await member.add_roles(sbls_role)
          await member.remove_roles(sbsf_role)
          await member.remove_roles(sblv_role)
          await member.remove_roles(bls_role)
          await member.remove_roles(bsf_role)
          await member.remove_roles(blv_role)          
          await ctx.channel.purge(limit=1)
          emb = discord.Embed(title= "", colour= 0xDEB887)
          emb.add_field(name= '⚔️ Роль старшего состава Больницы Лос-Сантос выдана игроку:', value=f'{member.mention} Роль выдал:{ctx.author.mention}, остальные сняты' , inline=True)
          await ctx.send(embed=emb)
        elif sbls_role in member.roles:
          await ctx.channel.purge(limit=1)
          emb = discord.Embed(title= "", colour= 0xD2B48C)
          emb.add_field(name= '⚙️ У игрока:', value=f'{member.mention}  Уже есть роль:{ctx.author.mention}' , inline=True)
          await ctx.send(embed=emb)
    else:
          pass
#Больницы СФ Выдача старшего состава
@client.command()
@commands.has_any_role(746117981930782852,746117984686178414,746117987299360870,746117989216026704)  #Следак/Министр/Лидер БСФ/Зам БСФ
async def sbsf(ctx, member: discord.Member):
    sbls_role = discord.utils.get(ctx.message.guild.roles, id = 746846011556757575) #БЛС Старший
    sbsf_role = discord.utils.get(ctx.message.guild.roles, id = 746846015901925407) #БСФ Старший
    sblv_role = discord.utils.get(ctx.message.guild.roles, id = 746761946375651348) #БЛВ Старший
    bls_role = discord.utils.get(ctx.message.guild.roles, id = 746120147588087931) #БЛС Младщий
    bsf_role = discord.utils.get(ctx.message.guild.roles, id = 746120252529573958) #БСФ Младщий
    blv_role = discord.utils.get(ctx.message.guild.roles, id = 746120251313356922) #БЛВ Младщий       
    stsf_channel = ctx.message.channel
    fasfasfas = client.get_channel(761350595873341471)
    if fasfasfas == stsf_channel:
        if not sbsf_role in member.roles:
          await member.remove_roles(sbls_role)
          await member.add_roles(sbsf_role)
          await member.remove_roles(sblv_role)
          await member.remove_roles(bls_role)
          await member.remove_roles(bsf_role)
          await member.remove_roles(blv_role)          
          await ctx.channel.purge(limit=1)
          emb = discord.Embed(title= "", colour= 0xDEB887)
          emb.add_field(name= '⚔️ Роль старшего состава Больницы Сан-Фиерро выдана игроку:', value=f'{member.mention} Роль выдал:{ctx.author.mention}, остальные сняты' , inline=True)
          await ctx.send(embed=emb)
        elif sbsf_role in member.roles:
          await ctx.channel.purge(limit=1)
          emb = discord.Embed(title= "", colour= 0xD2B48C)
          emb.add_field(name= '⚙️ У игрока:', value=f'{member.mention}  Уже есть роль:{ctx.author.mention}' , inline=True)
          await ctx.send(embed=emb)
    else:
          pass
#Больницы ЛВ Выдача старшего состава
@client.command()
@commands.has_any_role(746117981930782852,746117984686178414,746117986053521429,746117988775886898)  #Следак/Министр/Лидер БЛВ/Зам БЛВ
async def sblv(ctx, member: discord.Member):
    sbls_role = discord.utils.get(ctx.message.guild.roles, id = 746846011556757575) #БЛС Старший
    sbsf_role = discord.utils.get(ctx.message.guild.roles, id = 746846015901925407) #БСФ Старший
    sblv_role = discord.utils.get(ctx.message.guild.roles, id = 746761946375651348) #БЛВ Старший
    bls_role = discord.utils.get(ctx.message.guild.roles, id = 746120147588087931) #БЛС Младщий
    bsf_role = discord.utils.get(ctx.message.guild.roles, id = 746120252529573958) #БСФ Младщий
    blv_role = discord.utils.get(ctx.message.guild.roles, id = 746120251313356922) #БЛВ Младщий       
    stsf_channel = ctx.message.channel
    fasfasfas = client.get_channel(761350595873341471)
    if fasfasfas == stsf_channel:
        if not sblv_role in member.roles:
          await member.remove_roles(sbls_role)
          await member.remove_roles(sbsf_role)
          await member.add_roles(sblv_role)
          await member.remove_roles(bls_role)
          await member.remove_roles(bsf_role)
          await member.remove_roles(blv_role)          
          await ctx.channel.purge(limit=1)
          emb = discord.Embed(title= "", colour= 0xDEB887)
          emb.add_field(name= '⚔️ Роль старшего состава Больницы Лас Вентурас выдана игроку:', value=f'{member.mention} Роль выдал:{ctx.author.mention}, остальные сняты' , inline=True)
          await ctx.send(embed=emb)
        elif sblv_role in member.roles:
          await ctx.channel.purge(limit=1)
          emb = discord.Embed(title= "", colour= 0xD2B48C)
          emb.add_field(name= '⚙️ У игрока:', value=f'{member.mention}  Уже есть роль:{ctx.author.mention}' , inline=True)
          await ctx.send(embed=emb)
    else:
          pass
#Снятие всех ролей
@client.command()
@commands.has_permissions( administrator = True )
async def un_role(ctx, member: discord.Member):
    sbls_role = discord.utils.get(ctx.message.guild.roles, id = 746846011556757575) #БЛС Старший
    sbsf_role = discord.utils.get(ctx.message.guild.roles, id = 746846015901925407) #БСФ Старший
    sblv_role = discord.utils.get(ctx.message.guild.roles, id = 746761946375651348) #БЛВ Старший
    bls_role = discord.utils.get(ctx.message.guild.roles, id = 746120147588087931) #БЛС Младщий
    bsf_role = discord.utils.get(ctx.message.guild.roles, id = 746120252529573958) #БСФ Младщий
    blv_role = discord.utils.get(ctx.message.guild.roles, id = 746120251313356922) #БЛВ Младщий       
    stsf_channel = ctx.message.channel
    fasfasfas = client.get_channel(761350595873341471)
    if fasfasfas == stsf_channel:
        if not un_role in member.roles:
          await member.remove_roles(sbls_role)
          await member.remove_roles(sbsf_role)
          await member.remove_roles(sblv_role)
          await member.remove_roles(bls_role)
          await member.remove_roles(bsf_role)
          await member.remove_roles(blv_role)          
          await ctx.channel.purge(limit=1)
          emb = discord.Embed(title= "", colour= 0x39d0d6)
          emb.add_field(name= '⚙️ Снял все роли:', value=f'{member.mention}' , inline=True)
          await ctx.send(embed=emb)


#Снятие ролей по отдельности

#LSMC
@client.command()
@commands.has_any_role(746117981930782852,746117984686178414,746117985873297469,746117987915792385)  #Следак/Министр/Лидер БЛС/Зам БЛС
async def un_stls(ctx, member: discord.Member):
    stls_role = discord.utils.get(ctx.message.guild.roles, id = 746846011556757575)
    stls_channel = ctx.message.channel
    fasfasfas = client.get_channel(761350595873341471)
    if fasfasfas == stls_channel:
        if not stls_role in ctx.author.roles:
            emb = discord.Embed(title= "", colour= 0xD2B48C)
            emb.add_field(name= '⚙️ Роль старшего состава Больницы Лос-Сантос у игрока:', value=f'{member.mention}. Не найдена' , inline=True)
            await ctx.send(embed=emb)
        else:
            await member.remove_roles(stls_role)
            await ctx.channel.purge(limit=1)
            emb = discord.Embed(title= "", colour= 0xD2B48C)
            emb.add_field(name= '⚙️ У игрока:', value=f'{member.mention} Снята роль Старшего состава Больницы Лос-Сантос:' , inline=True)
            await ctx.send(embed=emb)
#SFMC
@client.command()
@commands.has_any_role(746117981930782852,746117984686178414,746117987299360870,746117989216026704)  #Следак/Министр/Лидер БСФ/Зам БСФ
async def un_stsf(ctx, member: discord.Member):
    stsf_role = discord.utils.get(ctx.message.guild.roles, id = 746846015901925407)
    un_stsf_channel = ctx.message.channel
    fasfasfas = client.get_channel(761350595873341471)
    if fasfasfas == un_stsf_channel:
        if not stsf_role in ctx.author.roles:
            emb = discord.Embed(title= "", colour= 0xD2B48C)
            emb.add_field(name= '⚙️ Роль старшего состава Больницы Лос-Сантос у игрока:', value=f'{member.mention}. Не найдена' , inline=True)
            await ctx.send(embed=emb)
        else:
            await member.remove_roles(stsf_role)
            await ctx.channel.purge(limit=1)
            emb = discord.Embed(title= "", colour= 0xD2B48C)
            emb.add_field(name= '⚙️ У игрока:', value=f'{member.mention} снята роль Старшего состава Больницы Сан-Фиерро' , inline=True)
            await ctx.send(embed=emb)
#LVMC
@client.command()
@commands.has_any_role(746117981930782852,746117984686178414,746117986053521429,746117988775886898)  #Следак/Министр/Лидер БЛВ/Зам БЛВ
async def un_stlv(ctx, member: discord.Member):
    stlv_role = discord.utils.get(ctx.message.guild.roles, id = 746761946375651348)
    un_stlv_channel = ctx.message.channel
    fasfasfas = client.get_channel(761350595873341471)
    if fasfasfas == un_stlv_channel:
        if not stlv_role in ctx.author.roles:
            emb = discord.Embed(title= "", colour= 0xD2B48C)
            emb.add_field(name= '⚙️ Роль старшего состава Больницы Лос-Сантос у игрока:', value=f'{member.mention}. Не найдена:' , inline=True)
            await ctx.send(embed=emb)
        else:
            await member.remove_roles(stlv_role)
            emb = discord.Embed(title= "", colour= 0xD2B48C)
            emb.add_field(name= '⚙️ У игрока:', value=f'{member.mention} снята роль Старшего состава Больницы Лас-Вентурас' , inline=True)
            await ctx.send(embed=emb)
#ВЫДАЧА РОЛЕЙ ЗАМОВ
#depls
@client.command()
@commands.has_any_role(746117981930782852,746117984686178414,746117985873297469)  #Следак/Министр/Лидер БЛС/Зам БЛС
async def depls(ctx, member: discord.Member):
    dep_role = discord.utils.get( ctx.guild.roles, id = 746117987303424020)
    yzbek_dep_role = discord.utils.get( ctx.guild.roles, id = 746117987915792385)
    dep_channel = ctx.message.channel
    fasfasfas = client.get_channel(761396716578013184)
    if fasfasfas == dep_channel:
        if not dep_role in member.roles:
          await member.add_roles(dep_role)
          await member.add_roles(yzbek_dep_role)
          emb = discord.Embed(title= "", colour= 0xD2B48C)
          emb.add_field(name= '⚙️ Роль заместителя Больницы Лос-Сантос выдана:', value=f'{member.mention}' , inline=True)
          await ctx.send(embed=emb)
        elif yzbek_dep_role in member.roles:  
          emb = discord.Embed(title= "", colour= 0xD2B48C)
          emb.add_field(name= '⚙️ У игрока:', value=f'{member.mention} уже есть роль заместителя' , inline=True)
          await ctx.send(embed=emb)
    else:
          pass
#depsf
@client.command()
@commands.has_any_role(746117981930782852,746117984686178414,746117987299360870)  #Следак/Министр/Лидер БСФ/Зам БСФ
async def depsf(ctx, member: discord.Member):
    yz_dep_role = discord.utils.get( ctx.guild.roles, id = 746117987303424020)
    yz_ddep_role = discord.utils.get( ctx.guild.roles, id = 746117989216026704)
    dep_channel = ctx.message.channel
    fasfasfas = client.get_channel(761396716578013184)
    if fasfasfas == dep_channel:
        if not yz_dep_role in member.roles:
          await member.add_roles(yz_dep_role)
          await member.add_roles(yz_ddep_role)
          emb = discord.Embed(title= "", colour= 0xD2B48C)
          emb.add_field(name= '⚙️ Роль заместителя Больницы Сан-Фиерро выдана:', value=f'{member.mention}' , inline=True)
          await ctx.send(embed=emb)
        elif yz_dep_role in member.roles:
          await ctx.send(f'{ctx.author.mention}, у данного человека уже есть роль заместителя')
    else:
          pass
#deplv
@client.command()
@commands.has_any_role(746117981930782852,746117984686178414,746117986053521429)  #Следак/Министр/Лидер БЛВ/Зам БЛВ
async def deplv(ctx, member: discord.Member):
    rm_dep_role = discord.utils.get( ctx.guild.roles, id = 746117987303424020)
    rm_ddep_role = discord.utils.get( ctx.guild.roles, id = 746117988775886898)
    dep_channel = ctx.message.channel
    fasfasfas = client.get_channel(761396716578013184)
    if fasfasfas == dep_channel:
        if not rm_dep_role in member.roles:
          await member.add_roles(rm_dep_role)
          await member.add_roles(rm_ddep_role)
          emb = discord.Embed(title= "", colour= 0xD2B48C)
          emb.add_field(name= '⚙️ Роль заместителя Больницы Лас-Вентурас выдана:', value=f'{member.mention}' , inline=True)
          await ctx.send(embed=emb)
        elif rm_dep_role in member.roles:
          emb = discord.Embed(title= "", colour= 0xD2B48C)
          emb.add_field(name= '⚙️ У игрока:', value=f'{member.mention} уже есть роль заместителя' , inline=True)
          await ctx.send(embed=emb)
    else:
          pass
#un_depls
@client.command()
@commands.has_any_role(746117981930782852,746117984686178414,746117985873297469)  #Следак/Министр/Лидер БЛС/Зам БЛС
async def un_depls(ctx, member: discord.Member):
    dep_role = discord.utils.get(ctx.message.guild.roles, id = 746117987303424020)
    yzbek_dep_role = discord.utils.get(ctx.message.guild.roles, id = 746117987915792385)
    un_dep_channel = ctx.message.channel
    fasfasfas = client.get_channel(761396716578013184)
    if fasfasfas == un_dep_channel:
        if not dep_role in ctx.author.roles:
            await ctx.channel.purge(limit=1)
            await ctx.channel.send(f'У человека нет роли заместителя {member.mention}.')
        else:
            await member.remove_roles(dep_role)
            await member.remove_roles(yzbek_dep_role)
            await ctx.channel.purge(limit=1)
            await ctx.channel.send(f'Роль заместителя снята у пользователю {member.mention}. Снята : {ctx.author.mention}')
#un_depsf
@client.command()
@commands.has_any_role(746117981930782852,746117984686178414,746117986053521429)  #Следак/Министр/Лидер БЛВ/Зам БЛВ
async def un_depsf(ctx, member: discord.Member):
    yz_dep_role = discord.utils.get(ctx.message.guild.roles, id = 746117987303424020)
    yz_ddep_role = discord.utils.get(ctx.message.guild.roles, id = 746117989216026704)
    un_yz_dep_channel = ctx.message.channel
    fasfasfas = client.get_channel(761396716578013184)
    if fasfasfas == un_yz_dep_channel:
        if not yz_dep_role in ctx.author.roles:
            await ctx.channel.purge(limit=1)
            emb = discord.Embed(title= "", colour= 0xD2B48C)
            emb.add_field(name= '⚙️ У игрока:', value=f'{member.mention}. Роль заместителя не найдена' , inline=True)
            await ctx.send(embed=emb)
        else:
            await member.remove_roles(yz_dep_role)
            await member.remove_roles(yz_ddep_role)
            await ctx.channel.purge(limit=1)
            emb = discord.Embed(title= "", colour= 0xD2B48C)
            emb.add_field(name= '⚙️ У игрока:', value=f'{member.mention}. Роль заместителя Больницы Сан-Фиерро снята' , inline=True)
            await ctx.send(embed=emb)
#un_deplv
@client.command()
@commands.has_any_role(746117981930782852,746117984686178414,746117986053521429)  #Следак/Министр/Лидер БЛВ/Зам БЛВ
async def un_deplv(ctx, member: discord.Member):
    rm_dep_role = discord.utils.get(ctx.message.guild.roles, id = 746117987303424020)
    rm_ddep_role = discord.utils.get(ctx.message.guild.roles, id = 746117988775886898)
    un_rm_dep_channel = ctx.message.channel
    fasfasfas = client.get_channel(761396716578013184)
    if fasfasfas == un_rm_dep_channel:
        if not rm_dep_role in ctx.author.roles:
            await ctx.channel.purge(limit=1)
            emb = discord.Embed(title= "", colour= 0xD2B48C)
            emb.add_field(name= '⚙️ У игрока:', value=f'{member.mention}. Роль заместителя не найдена' , inline=True)
            await ctx.send(embed=emb)
        else:
            await member.remove_roles(rm_dep_role)
            await member.remove_roles(rm_ddep_role)
            await ctx.channel.purge(limit=1)
            emb = discord.Embed(title= "", colour= 0xD2B48C)
            emb.add_field(name= '⚙️ У игрока:', value=f'{member.mention}. Роль заместителя Больницы Лас-Вентурас снята' , inline=True)
            await ctx.send(embed=emb)
#invite
@commands.cooldown(1, 60*30, commands.BucketType.user)
@client.command()
@commands.has_any_role(746111063975526494)
async def invite( ctx ):
    await ctx.channel.purge(limit=1)
    await ctx.send('https://discord.gg/NHH7EMY')

#парсер
#Онлаин фракций
#Армия ЛС
@commands.cooldown(1, 60*1, commands.BucketType.user)
@client.command()
@commands.has_any_role(746111063975526494) 
async def mc(ctx):
    botchannel = client.get_channel(758007147526094988)
    r = requests.get('https://arizona-rp.com/mon/fraction/13/5')
    soup = BeautifulSoup (r.text, 'html.parser')
    players_bs4 = soup.findAll("tr")

    leader1 = None

    for player in players_bs4[1:]:
        _, name, rank, status = [
            i.text for i in player.findAll("td")
        ]
        data1 = {
            "**Действующий лидер:**": name,
            "**Статус**": status,
        }
        if rank == "Лидер":
            leader1 = data1

    r1 = requests.get('https://arizona-rp.com/mon/fraction/13/5')
    result1 = re.findall('Сейчас играет', r.text)
    onlineMembers1 = len(result1) # Игроки онлайн)
#Армия СФ
    r = requests.get('https://arizona-rp.com/mon/fraction/13/8')
    soup = BeautifulSoup (r.text, 'html.parser')
    players_bs4 = soup.findAll("tr")

    leader2 = None

    for player in players_bs4[1:]:
        _, name, rank, status = [
            i.text for i in player.findAll("td")
        ]
        data2 = {
            "**Действующий лидер:**": name,
            "**Статус**": status,
        }
        if rank == "Лидер":
            leader2 = data2

    r = requests.get('https://arizona-rp.com/mon/fraction/13/8')
    result2 = re.findall('Сейчас играет', r.text)
    onlineMembers2 = len(result2) # Игроки онлайн)
#ТСР
    r = requests.get('https://arizona-rp.com/mon/fraction/13/22')
    soup = BeautifulSoup (r.text, 'html.parser')
    players_bs4 = soup.findAll("tr")

    leader3 = None

    for player in players_bs4[1:]:
        _, name, rank, status = [
            i.text for i in player.findAll("td")
        ]
        data3 = {
            "**Действующий лидер:**": name,
            "**Статус**": status,
        }
        if rank == "Лидер":
            leader3 = data3

    r = requests.get('https://arizona-rp.com/mon/fraction/13/22')
    result3 = re.findall('Сейчас играет', r.text)
    onlineMembers3 = len(result3) # Игроки онлайн)
#text
    leader1 = 'Действующий лидер: {0}, статус: {1}'.format(leader1['**Действующий лидер:**'], leader1['**Статус**'])
    leader2 = 'Действующий лидер: {0}, статус: {1}'.format(leader2['**Действующий лидер:**'], leader2['**Статус**'])
    leader3 = 'Действующий лидер: {0}, статус: {1}'.format(leader3['**Действующий лидер:**'], leader3['**Статус**'])
    e = discord.Embed(description="**Онлаин Министерства Здравоохранения**")
    e.add_field(name="`Больница Лос-Сантос`", value=f' Сотрудников в сети: **{onlineMembers1}**\n{leader1}', inline=False)
    e.add_field(name="`Больница Сан-Фиерро`", value=f' Сотрудников в сети: **{onlineMembers2}**\n{leader2}', inline=False)
    e.add_field(name="`Больница Лас-Вентурас`", value=f' Сотрудников в сети: **{onlineMembers3}**\n{leader3}', inline=False)
    await ctx.send(embed=e)


#@client.command()
async def dephelp(ctx):
    emb = discord.Embed(title= "**Команды бота** `Команды работают только в этом канале`", colour= 0xE0FFFF)
    emb.add_field(name= "{}str".format(prefix), value = "⭕ Выдать строгий выговор")
    emb.add_field(name= "{}yst".format(prefix), value = "❌ Выдать устный выговор")
    emb.add_field(name= "{}unstr".format(prefix), value = "✅ Снять строгий выговор")
    emb.add_field(name= "{}unyst".format(prefix), value = "❎ Снять устный выговор")
    emb.add_field(name= "{}warnlist".format(prefix), value = "⬜ Просмотреть выговоры лидеров")
    emb.add_field(name= "**INFO**".format(prefix), value = "🔥 Выдача предов: !кмд @упом.лидера Причина")
    emb.add_field(name= "**INFO**".format(prefix), value = "🔥 Снятие предов: !unкмд @упом.лидера")
    await ctx.send(embed=emb)

#@client.command()
async def hyi(ctx, arg):
	podkl = client.get_channel(746443271999455323)
	if podkl == ctx.message.channel:
		await ctx.send(arg) #отправляем обратно аргумент
	else:
		await ctx.send('Работаю только в определенном канале')

@client.command()
@commands.has_any_role(746117981930782852)
async def yst(stx, member: discord.Member = None, reason = None):
	author = stx.message.author
	podkl = client.get_channel(765948198412877904)
	if podkl == stx.message.channel:
		if member is None:
			await stx.send(embed = discord.Embed(description = f'**Укажите пользователя!**'))
			return
		if reason is None:
			await stx.send(embed = discord.Embed(description = f'**Причина не указана!**'))
			return
		if collusers.count_documents({"_id": member.id}) == 0:
			collusers.insert_one({"_id": member.id, "Устный": 0, "Строгий": 0})
		nowpred = collusers.find_one({"_id": member.id})["Устный"]
		collusers.update_one({"_id": member.id}, {"$set": {"Устный": nowpred + 1}})
		channel = client.get_channel(747216687941550202)
		await channel.send(embed = discord.Embed(description = f'**Следящий {author.mention} выдал устное предупреждение лидеру {member.mention} по причине: `{reason}`.**', color = 0x00cc00))
		nextcheck = collusers.find_one({"_id": member.id})["Устный"]
		if nextcheck == 3:
			nowpred = collusers.find_one({"_id": member.id})["Строгий"]
			collusers.update_one({"_id": member.id}, {"$set": {"Устный": 0, "Строгий": nowpred + 1}})
			await stx.send(embed = discord.Embed(description = f'**Так как лидер {member.mention} получил 3й устный выговор, он получает 1 строгий!**', color = 0x00cc00))
		else:
			await stx.send('Выдал.')

@client.command()
@commands.has_any_role(746117981930782852)
async def str(stx, member: discord.Member = None, reason = None):
	author = stx.message.author
	podkl = client.get_channel(765948198412877904)
	if podkl == stx.message.channel:
		if member is None:
			await stx.send(embed = discord.Embed(description = f'**Укажите пользователя!**'))
			return
		if reason is None:
			await stx.send(embed = discord.Embed(description = f'**Причина не указана!**'))
			return
		if collusers.count_documents({"_id": member.id}) == 0:
			collusers.insert_one({"_id": member.id, "Устный": 0, "Строгий": 0})
		nowpred = collusers.find_one({"_id": member.id})["Строгий"]
		collusers.update_one({"_id": member.id}, {"$set": {"Строгий": nowpred + 1}})
		channel = client.get_channel(747216687941550202)
		await channel.send(embed = discord.Embed(description = f'**Следящий {author.mention} выдал строгое предупреждение лидеру {member.mention} по причине: `{reason}`.**', color = 0x00cc00))
		nextcheck = collusers.find_one({"_id": member.id})["Строгий"]
		if nextcheck == 3:
			nowpred = collusers.find_one({"_id": member.id})["Строгий"]
			await member.send(embed = discord.Embed(description = f'**Дружище {member.mention} у тебя 3 строгих, иди снимай**', color = 0x00cc00))
		else:
			await stx.send('Выдал.')


@client.command()
@commands.has_any_role(746117981930782852)
async def unyst(stx, member: discord.Member = None):
	author = stx.message.author
	podkl = client.get_channel(765948198412877904)
	if podkl == stx.message.channel:
		if member is None:
			await stx.send(embed = discord.Embed(description = f'**Укажите пользователя!**'))
			return
		if collusers.count_documents({"_id": member.id}) == 0:
			await stx.send(embed = discord.Embed(description = '**У этого лидера отсутствуют предупреждения!**'))
		nowpred = collusers.find_one({"_id": member.id})["Устный"]
		strogpred = collusers.find_one({"_id": member.id})["Строгий"]
		if nowpred == 0 and strogpred >= 1:
			collusers.update_one({"_id": member.id}, {"$set": {"Устный": 2, "Строгий": strogpred - 1}})
			await channel.send(embed = discord.Embed(description = f'**Следящий {author.mention} снял устное предупреждение лидеру {member.mention}. Так как у него не было устных а был строгий, он заменил ему 1 строгий на 2 устных.**', color = 0x00cc00))
			channel = client.get_channel(747216687941550202)
		elif nowpred >= 1:
			collusers.update_one({"_id": member.id}, {"$set": {"Устный": nowpred - 1}})
			channel = client.get_channel(747216687941550202)
			await channel.send(embed = discord.Embed(description = f'**Следящий {author.mention} снял устное предупреждение лидеру {member.mention}.**', color = 0x00cc00))
			nowpred = collusers.find_one({"_id": member.id})["Устный"]
			strogpred = collusers.find_one({"_id": member.id})["Строгий"]
			if nowpred == 0 and strogpred == 0:
				collusers.delete_one({"_id": member.id})
				print(f'Пользователь с ID {member.id} удалён из БД т.к. у него нет выговоров')
			else:
				pass
		else:
			await stx.send(embed = discord.Embed(description = f'**Неизвестная ошибка, обратитесь к разработчику...**'))

@client.command()
@commands.has_any_role(746117981930782852)
async def unstr(stx, member: discord.Member = None):
	author = stx.message.author
	podkl = client.get_channel(765948198412877904)
	if podkl == stx.message.channel:
		if member is None:
			await stx.send(embed = discord.Embed(description = f'**Укажите пользователя!**'))
			return
		if collusers.count_documents({"_id": member.id}) == 0:
			await stx.send(embed = discord.Embed(description = '**У этого лидера отсутствуют строгие предупреждения! Используйте `!unyst`**'))
		nowpred = collusers.find_one({"_id": member.id})["Строгий"]
		if nowpred == 0 and strogpred >= 1:
			channel = client.get_channel(747216687941550202)
			await channel.send(embed = discord.Embed(description = f'**Следящий {author.mention} снял строгое предупреждение лидеру {member.mention}.**', color = 0x00cc00))
		elif nowpred >= 1:
			collusers.update_one({"_id": member.id}, {"$set": {"Строгий": nowpred - 1}})
			channel = client.get_channel(747216687941550202)
			await channel.send(embed = discord.Embed(description = f'**Следящий {author.mention} снял строгое предупреждение лидеру {member.mention}.**', color = 0x00cc00))
			nowpred = collusers.find_one({"_id": member.id})["Устный"]
			strogpred = collusers.find_one({"_id": member.id})["Строгий"]
			if nowpred == 0 and strogpred == 0:
				collusers.delete_one({"_id": member.id})
				print(f'Пользователь с ID {member.id} удалён из БД т.к. у него нет выговоров')
			else:
				pass
		else:
			await stx.send(embed = discord.Embed(description = f'**Неизвестная ошибка, обратитесь к разработчику...**'))

@client.command()
@commands.has_any_role(746117981930782852, 746117985445478551, 746117987303424020)
async def warnlist(stx):
    userlist = list()
    strog = list()
    ystn = list()
    text = ''
    text2 = ''
    text3 = ''
    for doc in collusers.find().sort([("Строгий", -1), ("Устный", -1)]):
        userlist.append(doc.get('_id'))
        strog.append(doc.get('Строгий'))
        ystn.append(doc.get('Устный'))

    for z in strog:
        text2 += f'{z} \n'
    
    for o in ystn:
        text3 += f'{o} \n'

    for i in userlist:
        member = stx.guild.get_member(i)
        text += f'{member.mention} \n'

    e = discord.Embed(title = 'Выговоры лидеров', colour = discord.Color.red())
    e.add_field(name = 'Ник лидера', value = text)
    e.add_field(name = 'Строгий', value = text2)
    e.add_field(name = 'Устный', value = text3)
    await stx.send(embed = e)





#Token + Start
token = open('token.txt', 'r').readline()
client.run(token)
