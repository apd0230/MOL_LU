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
    if message.content == '!사용언어':
        await message.channel.send('```HTML```')
    if message.content == '!언어':
        await message.channel.send('```HTML```')
    
    if message.content == '우컴':
        await message.channel.send('골1')

    Q_Mark = ''
    E_Q_Mark = ''
    for i in range(message.content.count('?')):
        Q_Mark += '몰?루 '
        E_Q_Mark += 'Don\'t?know '

    if '몰?루' in message.content:
        await message.channel.send(file=discord.File('mollu.png'))
    elif 'ㅁ?ㄹ' in message.content:
        await message.channel.send(file=discord.File('mollu.png'))
    elif message.content.startswith('What'):
        if '?' in message.content:
            await message.channel.send(E_Q_Mark)
        else: await message.channel.send('Don\'t?know')
    elif message.content.startswith('what'):
        if '?' in message.content:
            await message.channel.send(E_Q_Mark)
        else: await message.channel.send('Don\'t?know')
    elif message.content.startswith('WHAT'):
        if '?' in message.content:
            await message.channel.send(E_Q_Mark)
        else: await message.channel.send('Don\'t?know')
    elif message.content.startswith('Why'):
        if '?' in message.content:
            await message.channel.send(E_Q_Mark)
        else: await message.channel.send('Don\'t?know')
    elif message.content.startswith('why'):
        if '?' in message.content:
            await message.channel.send(E_Q_Mark)
        else: await message.channel.send('Don\'t?know')
    elif message.content.startswith('WHY'):
        if '?' in message.content:
            await message.channel.send(E_Q_Mark)
        else: await message.channel.send('Don\'t?know')
    elif '?' in message.content:
        await message.channel.send(Q_Mark)
    elif '누구' in message.content:
        await message.channel.send('몰?루')
    elif '어디' in message.content:
        await message.channel.send('몰?루')
    elif 'ㅁㄹ' in message.content:
        await message.channel.send('몰?루')
    elif '몰라' in message.content:
        await message.channel.send('몰?루')
    elif '모를' in message.content:
        await message.channel.send('몰?루')
    elif '모르' in message.content:
        if '아모르' in message.content:
            return None
        if '모르핀' in message.content:
            return None
        if '모르가나' in message.content:
            return None
        if '모르간' in message.content:
            return None
        else: await message.channel.send('몰?루')
    elif '그럴' in message.content:
        await message.channel.send('몰?루')
    elif '아닐' in message.content:
        await message.channel.send('몰?루')
    elif '뭐' in message.content:
        await message.channel.send('몰?루')
    elif '뭔' in message.content:
        await message.channel.send('몰?루')
    elif '왜' in message.content:
        if '왜놈' in message.content:
            return None
        elif '왜건' in message.content:
            return None
        elif '왜나라' in message.content:
            return None
        else: await message.channel.send('몰?루')
    elif '왤까' in message.content:
        await message.channel.send('몰?루')
    elif '왤케' in message.content:
        await message.channel.send('몰?루')
    elif '어쩌' in message.content:
        await message.channel.send('몰?루')
    elif '어째' in message.content:
        await message.channel.send('몰?루')
    elif '어찌' in message.content:
        await message.channel.send('몰?루')
    elif '저쩌' in message.content:
        await message.channel.send('몰?루')
    elif '저째' in message.content:
        await message.channel.send('몰?루')
    elif '저찌' in message.content:
        await message.channel.send('몰?루')
    elif '추천' in message.content:
        if '아침' in message.content:
            await message.channel.send('삼양라면')
        elif '점심' in message.content:
            await message.channel.send('민트초코')
        elif '저녁' in message.content:
            await message.channel.send('파인애플 피자')
        else: await message.channel.send('몰?루')
    elif message.content.endswith('냐'):
        if message.content.startswith('냐'):
            return None
        else: await message.channel.send('몰?루')
    elif message.content.endswith('그런가'):
        await message.channel.send('몰?루')
    elif message.content.endswith('아닌가'):
        await message.channel.send('몰?루')

token = ('OTAzMzI3NjY5NjcwODA1NTI2.YXrXcw.tV7JOHrjyfQgJ8npyd3-C5RWD4M')

mollu.run(token)