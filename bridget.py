#Created by Alden Lau for the Discord server of the hackathon BridgeHacks.
#Last updated 7/11/20

import discord
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import commands


token = 'INSERT TOKEN HERE'
client = discord.Client()

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
google_client = gspread.authorize(credentials)

sheet = google_client.open("Summer BridgeHacks Participant Registration (Responses)").get_worksheet(2)

found = False

@client.event
async def on_ready():
    game = discord.Game("Type !help for commands!")
    await client.change_presence(activity=game)
    print("Bot ready!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith("!checkin") and str(message.channel)=="check-in":
        found=False
        name1 = message.content[9:]
        cell_list1 = sheet.range("C2:C500")
        cell_list2 = sheet.range("D2:D500")
        for x in range(len(cell_list1)):
            if (cell_list1[x].value.lower()+" "+ cell_list2[x].value.lower()) == name1.lower():
                role = discord.utils.get(message.author.guild.roles, name="Hackers")
                await message.author.add_roles(role)
                channel = await message.author.create_dm()
                await channel.send("Welcome to BridgeHacks 2020! Remember to read #rules and #welcome. Have a good time!")
                found=True
                break
        if found==False:
            channel = await message.author.create_dm()
            await channel.send("You don't seem to be registered for BridgeHacks 2020. Sign up at bridgehacks.com! If you believe this is an error, message the BridgeHacks staff.")
        
            
    if message.content.lower() == "!schedule":
        channel = await message.author.create_dm()
        await channel.send(
                            "__**July 17**__"
                            "\n**5:00 PM**   Opening ceremony"
                            "\n**5:15 PM**   Words by sponsors"
                            "\n**5:30 PM**   Hacking begins"
                            "\n**6:30 PM**   Minecraft activity begins"
                            "\n**6:30 PM - 7:00 PM**   skribbl.io activity"
                            "\n**6:30 PM - 9:30 PM**   Mentoring available"
                            "\n**6:30 PM - 7:30 PM**   Python workshop"
                            "\n**7:30 PM - 8:30 PM**   HTML workshop"
                            "\n**8:30 PM - 9:30 PM**   Intro to iOS Development workshop\n"
                            "\n__**July 18**__"
                            "\n**9:00 AM - 12:00 PM**   Mentoring available"
                            "\n**9:30 AM - 10:30 AM**   Intro to UX/UI Design workshop"
                            "\n**10:30 AM - 11:30 AM**   JavaScript workshop"
                            "\n**12:00 PM - 1:00 PM**   Build a Cloud-Connected AR/VR App in 15 Min"
                            "\n**1:30 PM - 2:30 PM**  skribbl.io activity"
                            "\n**2:00 PM - 5:00 PM**   Mentoring available"
                            "\n**2:30 PM - 3:30 PM**   Getting Internships workshop"
                            "\n**4:00 PM - 5:00 PM**   AI Ethics workshop"
                            "\n**6:00 PM - 9:00 PM**   Mentoring available"
                            "\n**6:00 PM - 7:00 PM**   3D Modeling & CAD workshop"
                            "\n**7:00 PM - 8:00 PM**   How to Network from Home workshop\n"
                            "\n__**July 19**__"
                            "\n**9:00 AM - 12:00 PM**   Mentoring available"
                            "\n**10:30 AM - 11:30 AM**   Journey Through Tech talk"
                            "\n**11:30 AM - 12:30 PM**   Financial Literacy workshop"
                            "\n**2:00 PM - 4:30 PM**   Mentoring available"
                            "\n**5:00 PM**   Submit projects\n"
                            "\n__**July 20**__"
                            "\n**By 7:00 PM**   Winners announced")
        await message.delete()


    if message.content.lower() == "!prizes":
        channel = await message.author.create_dm()
        await channel.send("**First place:** Skullcandy Wireless Earbuds + SNAPTAIN Drone"
                                    "\n**Second place:** $50 Amazon gift card + Raspberry Pi 4"
                                    "\n**Third place:** Sony SRS-XB12 Mini Bluetooth Speaker + Logitech G502 gaming mouse\n"
                                    "\n**Cisco's Choice:** $30 Amazon gift card"
                                    "\n**Top Middle School Hack:** $20 Steam gift card"
                                    "\n**Best Design:** Omni Design Group Student Licence + Drawing Pad and Pen for PC"
                                    "\n**Best Hack for Education:** Rocketbook Smart Reusable Notebook + Art of Problem Solving coupons"
                                    "\n**Best Enviromental Hack:** Boba Tumbler set with 2 straws"
                                    "\n**Best Hack for Social Justice:** AOMAIS Pro Camera Lens Kit"
                                    "\n**Best Mobile App:** Anker PowerCore 10000 Portable Charger"
                                    "\n**Best Beginner Hack:** Raspberry Pi 3 B+"
                                    "\n**Best Solo Hack:** Redragon S101 Wired Gaming Keyboard and Mouse"
                                    "\n**Best VR/AR Hack:** $50 Amazon gift card")
        await message.delete()


    if message.content.lower() == "!help":
        channel = await message.author.create_dm()
        await channel.send("**!schedule:** Shows the schedule."
                            "\n**!prizes:** Shows the list of prizes."
                            "\n**!faq:** Shows frequently asked questions."
                            "\n**!submit:** Shows the link where you can submit your project."
                            "\n**!social:** Shows links to BridgeHacks social media.")
        await message.delete()


    if message.content.lower() == "!faq":
        channel = await message.author.create_dm()
        await channel.send(
            "__**FAQ **__"
            "\n**Who is this hackathon for?**"
            "\nBridgeHacks is a hackathon for middle and high school students. No programming experience is needed, and all skill levels are welcome."
            "\n**Do I have to submit a project?**"
            "\nYou are not required to submit a project, but we highly recommend it."
            "\n**Where are the workshops hosted?**"
            "\nThe workshops will take place on Zoom calls. Check <#730279543516168203> or <#628464975043624960> for the links to the Zoom calls when they become available."
            "\n**Is there a cost?**"
            "\nNo. This hackathon is completely free of charge."
            "\n**Do I need a team?**"
            "\nNo. You can work solo or in a team of up to 4 people. You can also find a team during the hackathon."
            "\n**Where do I submit my project?**"
            "\nSubmit your project at https://bridgehacks.devpost.com/"
            "\n**Can I attend as a complete beginner?**"
            "\nYes. There will be plenty of workshops to learn how to code and make projects."
            "\n**My question isn't listed here.**"
            "\nYou can send us an email at bridgehacks@gmail.com or DM one of the BridgeHacks staff."
        )
        await message.delete()

    if message.content.lower() == "!submit":
        channel = await message.author.create_dm()
        await channel.send("Submit your project at https://bridgehacks.devpost.com/")
        await message.delete()

    if message.content.lower() == "!social":
        channel = await message.author.create_dm()
        await channel.send("**Website:** https://www.bridgehacks.com/"
                            "\n**Instagram:** https://www.instagram.com/bridgehacks/"
                            "\n**Facebook:** https://www.facebook.com/groups/bridgehacks/"
                            "\n**Email:** bridgehacks@gmail.com"
        )
        await message.delete()

    if str(message.channel)=="check-in":
        await message.delete()

# token goes here
client.run(token)
