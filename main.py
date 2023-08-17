import discord
import things
import requests

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

pos1 = "CHWY"
api_12 = things.DUODEC
USER1 = things.USER1

def get_stock_price(stock_symbol, api):
    url = f"https://api.twelvedata.com/price?symbol={stock_symbol}&apikey={api}"
    response = requests.get(url).json()
    price = response['price'][:-3]
    print(response)
    print(f"{stock_symbol} is {price}")
    return price

@client.event
async def on_ready():
    print('{0.user} is ready and surfing the market'.format(client))

@client.event
async def on_message(message):
    global api_12
    global pos1
    global USER1
    if message.author == client.user:
        return
    
    if message.content.startswith('$moon'):
        await message.channel.send('to the moon!')
        price = get_stock_price(pos1, api_12)
        await message.channel.send(f"{pos1} is {price}")

        if float(price) <= 29:
            await message.channel.send(f"<@{USER1}> SELL {pos1} it has hit strike price")

client.run(things.CLAVIS)
