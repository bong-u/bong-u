import discord
import time

from crawler import Crawler

client = discord.Client()

@client.event
async def on_ready():
    name = ['학사공지', '일반공지']
    channel = client.get_channel(770277612382847006)
    date = time.strftime('%c', time.localtime(time.time()))
    cnt = [0, 0]
    
    print (date, end=' ')
    crawler = Crawler()

    for i in range(2):
        for el in crawler.CrawlData(i):
            cnt[i] += 1
            embed = discord.Embed(**el)
            embed.set_author(name=name[i])
            embed.set_footer(text=date)
            await channel.send(embed=embed)

    print (cnt)
    crawler.UpdateFile()

    await client.close()

client.run('[BOT TOKEN]')
