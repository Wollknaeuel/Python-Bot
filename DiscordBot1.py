import discord

class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
            print("Ja mein Herr und Gebieter, ich bin zurstelle.")

    #Reaktion auf Nachrichten
    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith("hallo"):
            await message.channel.send("Willkommen mein Gebieter")

        if message.content.startswith("moin"):
            await message.channel.send("Willkommen mein Gebieter")

        if message.content.startswith("Hallo"):
            await message.channel.send("Willkommen mein Gebieter")

        if message.content.startswith("Moin"):
            await message.channel.send("Willkommen mein Gebieter")

        if message.content.startswith("Malzeit"):
            await message.channel.send("Willkommen mein Gebieter")

        if message.content.startswith("malzeit"):
            await message.channel.send("Willkommen mein Gebieter")


client = MyClient()
client.run("hier das Token einfügen")
