import discord
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import commands


token = 'NzIyNjU0NTE2OTA1NzcxMDA5.XvEKtg.9N8PpTo65GbHdcPoi_7U0gm1i4I'
client = discord.Client()

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
google_client = gspread.authorize(credentials)

sheet = google_client.open("Summer BridgeHacks Participant Registration (Responses)").sheet1


@client.event
async def on_ready():
    #channel = client.get_channel(720730646892511344)
    #await channel.send('Welcome to BridgeHacks 2020! Type "!checkin YourFirstName YourLastName" in this channel to gain access to the rest of the server. \nExample: !checkin John Doe\nIf you haven\'t registered yet, go to bridgehacks.com!')
    print("Bot ready!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.lower().startswith("!checkin") and str(message.channel)=="check-in":
        name1 = message.content[9:]
        cell_list1 = sheet.range("C1:C100")
        cell_list2 = sheet.range("D1:D100")
        for x in range(len(cell_list1)):
            if (cell_list1[x].value.lower()+" "+ cell_list2[x].value.lower()) == name1.lower():
                role = discord.utils.get(message.author.guild.roles, name="Registered Hacker")
                await message.author.add_roles(role)
                channel = await message.author.create_dm()
                await channel.send("Welcome to BridgeHacks 2020! Remember to read #rules and #welcome. Have a good time!")
                break
        channel = await message.author.create_dm()
        await channel.send("You don't seem to be registered for BridgeHacks 2020. Sign up at bridgehacks.com!")
        
            
    if message.content.lower() == "!schedule":
        await message.channel.send("placeholder schedule")


    if message.content.lower() == "!prizes":
        await message.channel.send("First place: Hydro Flask + Drone"
                                    "\nSecond place: $50 Amazon gift card + Raspberry Pi 4"
                                    "\nThird place: Sony SRS-XB12 Mini Bluetooth Speaker + $20 Amazon gift card"
                                    "\nCisco's Choice: $30 Amazon gift card"
                                    "\nTop Middle School Hack: $25 Gamestop gift card"
                                    "\nBest Design: Omni Design Group Student Licence + Drawing Pad and Pen for PC"
                                    "\nBest Hack for Education: Rocketbook Smart Reusable Notebook + Art of Problem Solving coupons"
                                    "\nBest Enviromental Hack: Bumbler cup with 2 straws"
                                    "\nBest Hack for Social Justice: AOMAIS Pro Camera Lens Kit"
                                    "\nBest Mobile App: Anker PowerCore 10000 Portable Charger"
                                    "\nBest Beginner Hack: Elegoo Arduino Super Starter Kit"
                                    "\nBest Solo Hack: Redragon S101 Wired Gaming Keyboard and Mouse")


    if message.content.lower() == "!help":
        channel = await message.author.create_dm()
        await channel.send("!schedule: Shows the schedule.\n!prizes: Shows the list of prizes.")


    if str(message.channel)=="check-in":
        await message.delete()

# token goes here
client.run(token)