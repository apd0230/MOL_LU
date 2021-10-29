import discord

mollu = discord.Client()

@mollu.event
async def on_ready():
    print('I am ready')

@mollu.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content == '!사용법':
        await message.channel.send('```모르는 것이 있으면 몰?루를 출력합니다.\n몰?루 혹은 ㅁ?ㄹ를 입력하면 몰?루콘을 올립니다.```')

    if message.content == '!개발언어':
        await message.channel.send('```HTML```')

    Q_Mark = ''
    for i in range(message.content.count('?')):
        Q_Mark += '몰?루 '

    if '몰?루' in message.content:
        await message.channel.send(file=discord.File('mollu.png'))
    elif 'ㅁ?ㄹ' in message.content:
        await message.channel.send(file=discord.File('mollu.png'))
    elif '?' in message.content:
        await message.channel.send(Q_Mark)
    elif 'ㅁㄹ' in message.content:
        await message.channel.send('몰?루')
    elif '몰라' in message.content:
        await message.channel.send('몰?루')
    elif '모르는' in message.content:
        await message.channel.send('몰?루')
    elif '모르겠' in message.content:
        await message.channel.send('몰?루')
    elif '모르네' in message.content:
        await message.channel.send('몰?루')
    elif '모르나' in message.content:
        await message.channel.send('몰?루')
    elif '모르냐' in message.content:
        await message.channel.send('몰?루')
    elif '모르지' in message.content:
        await message.channel.send('몰?루')
    elif '모를' in message.content:
        await message.channel.send('몰?루')
    elif '모르죠' in message.content:
        await message.channel.send('몰?루')

token = ('OTAzMzI3NjY5NjcwODA1NTI2.YXrXcw.tV7JOHrjyfQgJ8npyd3-C5RWD4M')

mollu.run(token)