import os
import random
import asyncio
import datetime
import requests
import discord
import re
from keep_alive import keep_alive
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(
	command_prefix="$",  # Change to desired prefix
	case_insensitive=True,  # Commands aren't case-sensitive
    intents=intents
)

bot.author_id = 1062859498483617873  # Change to your discord id!!!

roasts = [
    "Your face looks like it was set on fire and put out with a fork.",
    "I'd call you a tool, but that would imply you were useful in at least one way.",
    "I'd roast you, but my mom said I'm not allowed to burn trash.",
    "I'm not saying I hate you, but I would unplug your life support to charge my phone.",
    "If you were any dumber, someone would have to water you twice a week.",
    "You're so annoying that you make happy meals cry",
    "Hey, you have something on your chin. No, the third one down",
    "You are the reason shampoo has instructions",
    "Don't think TOO hard, you might sprain your brain",
    "You are so full of crap, your toilet is jealous",
    "I'd smack you, but that'd be animal abuse",
    "Your mom is so fat, Dora can't even explore her",
    "So, a thought crossed your mind, eh? Must have been a long and lonely journey",
    "If I had a dollar for every time you said something smart, I'd be in the negatives",
    "Hold still. I’m trying to imagine you with a non-toxic personality.",
    "You look like a sentient bubonic plague",
    "If your brain was dynamite, there wouldn’t be enough to blow a hair off your head",
    "You look like a before picture",
    "You are what happens when women drink during pregnancy",
    "The last time I saw something like you, it was behind metal bars",
    "You were so happy for the negativity of your Covid test, we didn’t want to spoil the happiness by telling you it was IQ test",
    "You are like a software update. every time I see you, I immediately think “not now”",
    "I look at you and think, \"What a waste of two billion years of evolution\"",
    "All mistakes are fixable. Except for you, you're past the point of no return",
    "Are you at a loss for words, or did you exhaust your entire vocabulary"
    "You can be anything you want, except good looking or smart",
    "You sound reasonable… Time to up my medication",
    "My phone battery lasts longer than your relationships"
]

pickupLines = [
    "You're a 9 because I'm the 1 you need",
    "Are you anxiety because you got me shakin' (Anxiety rizz)",
    "Are you a Lamborghini because I want to get inside of you (Rich kid rizz)",
    "Are you a hockey puck because I cant stop chasing you (Hockey rizz)",
    "Well, here I am. What are your other two wishes?",
    "Are you French? Because Eiffel for you",
    "If I could rearrange the alphabet, I’d put ‘U’ and ‘I’ together",
    "If you were a Transformer… you’d be Optimus Fine",
    "Are you a parking ticket? Because you’ve got FINE written all over you",
    "Do you believe in love at first sight—or should I walk by again?",
    "Did you just come out of the oven? Because you’re hot",
    "It’s a good thing I have my library card because I am totally checking you out",
    "Is your name Google? Because you have everything I’ve been searching for",
    "Are you a bank loan? Because you got my interest",
    "Are you a time traveler? Cause I see you in my future!",
    "Can I follow you where you’re going right now? Because my parents always told me to follow my dreams",
    "Is this the Hogwarts Express? Because it feels like you and I are headed somewhere magical",
    "Something’s wrong with my eyes because I can’t take them off you",
    "My love for you is like diarrhea, I just can't hold it in",
    "Somebody better call God, because he’s missing an angel",
    "We’re not socks, but I think we’d make a great pair",
    "Do you like Star Wars? Because Yoda only one for me!",
    "Did you invent the airplane? Because you seem Wright for me",
    "Do you have a BandAid? I just scraped my knee falling for you",
    "Do you have a map? I keep getting lost in your eyes",
    "You must be tired because you've been running through my mind all night"
]


@bot.command()
async def weather(ctx, *, location: str):
    """Get the current weather for a specified location."""
    api_key = "245666739800010fae4c4e44d4a9f4ad"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={location}&units=imperial"
    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        city = data['name']
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        await ctx.send(f"The temperature in **{city}** is **{temp}°F** with **{desc}**")
    else:
        await ctx.send("Sorry, I couldn't get the weather for that location.")

@bot.command()
async def roast(ctx, member: discord.Member):
    """Roast the specified user."""
    randomRoast = random.choice(roasts)
    await ctx.send(f"{member.mention}, {randomRoast}")

@bot.command()
async def pickup(ctx, member: discord.Member):
    """Use a pickup line on the specified user."""
    randomPickupLine = random.choice(pickupLines)
    await ctx.send(f"{member.mention}, {randomPickupLine}")

# command to nuke a user
@bot.command()
async def nuke(ctx, member):
    """Launch a nuke at the specified user."""
    # generate a random time between 5 to 15 seconds
    nuke_time = random.randint(5, 15)
    # send the response message
    await ctx.send(f"Nuking {member}! Nuke will land in {nuke_time} seconds.")
    # wait for the nuke time
    await asyncio.sleep(nuke_time)
    # nuke the user
    await ctx.send(f"{member} has been blown off the face of the earth by your nuke! :smiling_imp:")

@bot.command()
async def rolldice(ctx, number: int):
    """Roll either one or two d6 dice."""
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum = dice1 + dice2
    if number == 1:
        await ctx.send("Rolling 1 die...")
        await asyncio.sleep(3)
        await ctx.send(f"You rolled {dice1}!")
    elif number == 2:
        await ctx.send("Rolling 2 dice...")
        await asyncio.sleep(3)
        await ctx.send(f"You rolled {dice1} and {dice2} (Sum: {sum})")
    else:
        await ctx.send("Please input the amount of dice you want to roll (1 or 2).")

@bot.command()
async def rolld12(ctx, number: int):
    """Roll either one or two d12 dice."""
    dice1 = random.randint(1, 12)
    dice2 = random.randint(1, 12)
    sum = dice1 + dice2
    if number == 1:
        await ctx.send("Rolling 1 d12 die...")
        await asyncio.sleep(3)
        await ctx.send(f"You rolled {dice1}!")
    elif number == 2:
        await ctx.send("Rolling 2 d12 dice...")
        await asyncio.sleep(3)
        await ctx.send(f"You rolled {dice1} and {dice2} (Sum: {sum})")
    else:
        await ctx.send("Please input the amount of d12 dice you want to roll (1 or 2).")

@bot.command()
async def rolld20(ctx, number: int):
    """Roll either one or two d20 dice."""
    dice1 = random.randint(1, 20)
    dice2 = random.randint(1, 20)
    sum = dice1 + dice2
    if number == 1:
        await ctx.send("Rolling 1 d20 die...")
        await asyncio.sleep(3)
        await ctx.send(f"You rolled {dice1}!")
    elif number == 2:
        await ctx.send("Rolling 2 d20 dice...")
        await asyncio.sleep(3)
        await ctx.send(f"You rolled {dice1} and {dice2} (Sum: {sum})")
    else:
        await ctx.send("Please input the amount of d20 dice you want to roll (1 or 2).")


@bot.command()
async def flip(ctx):
    """Flip a coin."""
    coin = random.choice(['Heads', 'Tails'])
    await ctx.send("Flipping coin...")
    await asyncio.sleep(3)
    await ctx.send(f"The coin landed on **{coin}**!")


@bot.command()
async def prostate(ctx, member):
    """Perform a prostate exam on the specified user."""
    cancer_prob = random.randint(1, 100)
    if cancer_prob <= 25:
        cancer = True
    elif cancer_prob > 25: cancer = False
    if cancer == True:
        await ctx.send(f"Prostate exam performed on {member}.\nOh no! It appears that {member} has prostate cancer :(")
    else:
        await ctx.send(f"Prostate exam performed on {member}.\nLuckily {member} doesn't have prostate cancer! :)")

@bot.command()
async def ballfondle(ctx, member):
    """Fondle the specified user's balls (give ur homies a lil tickle)."""
    await ctx.send(f"{member}\'s balls have been fondled :smirk:")

# Define the pins command and exclude pinned images
@bot.command()
async def pins(ctx):
    """Send all of the pinned messages in the current channel."""
    pinned_messages = await ctx.channel.pins()
    output = []

    for i, message in enumerate(pinned_messages):
        if message.content and not message.attachments:
            output.append(f"Pin - {message.author.name}: {message.content}")
    
    await ctx.send("\n".join(output))

# Define the mute command
@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, duration: str, *, reason="No reason provided."):
    """Mute the specified user for a specified length of time. Admin only."""
    # Parse the duration argument to extract the number of minutes
    match = re.match(r'^(\d+)(m)?$', duration)
    if not match:
        await ctx.send("Invalid duration format. Please enter a valid number of minutes.")
        return

    minutes = int(match.group(1))
    duration_seconds = minutes * 60

    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")

    if not muted_role:
        # If the Muted role doesn't exist, create it
        muted_role = await ctx.guild.create_role(name="Muted")

        # Set the permissions for the muted role
        for channel in ctx.guild.channels:
            await channel.set_permissions(muted_role, speak=False, send_messages=False)

    await member.add_roles(muted_role, reason=reason)

    # Schedule the member's unmute after the specified duration
    await ctx.send(f"{member.mention} has been muted for {minutes} minute(s).")
    await asyncio.sleep(duration_seconds)
    await member.remove_roles(muted_role, reason="Mute duration expired.")
    await ctx.send(f"{member.mention} has been unmuted.")

# Define the unmute command
@bot.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member):
    """Unmute the specified user. Admin only."""
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")

    if muted_role in member.roles:
        await member.remove_roles(muted_role, reason="Unmute command used.")
        await ctx.send(f"{member.mention} has been unmuted.")
    else:
        await ctx.send(f"{member.mention} is not currently muted.")

# Define the kick command
@bot.command()
@commands.has_role(916033010367873084)
async def kick(ctx, member: discord.Member, *, reason="No reason provided."):
    """Kick the specified user. Admin only."""
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} has been kicked.")

# Define the ban command
@bot.command()
@commands.has_role(916033010367873084)
async def ban(ctx, member: discord.Member, *, reason="No reason provided."):
    """Ban the specified user. Admin only."""
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} has been banned.")

@bot.command()
async def goofytime(ctx):
    """Activate goofy time and send a link to the Lounge VC."""
    await ctx.send("It's goofy time :smirk::smirk::smirk:\nhttps://discord.gg/nJfhkTKUhz")

# Timezone for scheduled Goofy Time
timezone = 'US/Central'

async def send_message():
    channel = client.get_channel(channel_id)
    await channel.send("It's goofy time :smirk::smirk::smirk:\nhttps://discord.gg/nJfhkTKUhz")

async def schedule_message():
    while True:
        now = datetime.datetime.now(datetime.timezone.utc).astimezone(pytz.timezone(timezone))
        # Set the desired hour and minute for the message to be sent
        send_time = now.replace(hour=20, minute=30, second=0, microsecond=0)
        if now > send_time:
            # If it's already past the scheduled send time for the day, schedule for the next day
            send_time += datetime.timedelta(days=1)
        delta = send_time - now
        # Sleep until the scheduled send time
        await asyncio.sleep(delta.seconds + 1)
        # Send the message
        await send_message()

# command to delete messages
@bot.command()
@commands.has_role('Admin')
async def delete(ctx, number: int):
    """Delete a specified amount of messages. Admin only."""
    # delete the specified number of messages
    await ctx.channel.purge(limit=number+1)

# Command to get the server invite
@bot.command()
async def invite(ctx):
    """Get the server invite."""
    await ctx.send("The server invite is: https://discord.gg/3v4MrCgRps")

@bot.command()
async def remind(ctx, time, *, message):
    """Set a reminder for a specific time with a specified message."""
    time_seconds = 0
    time_re = r'(?:(?P<days>\d+)d)?\s*(?:(?P<minutes>\d+)m)?\s*(?:(?P<seconds>\d+)s)?'
    match = re.fullmatch(time_re, time)

    if not match:
        await ctx.send("Invalid time format. Please provide the time in days, minutes, and/or seconds.")
        return

    days = int(match.group('days') or 0)
    minutes = int(match.group('minutes') or 0)
    seconds = int(match.group('seconds') or 0)

    time_seconds = days * 24 * 60 * 60 + minutes * 60 + seconds

    if time_seconds == 0:
        await ctx.send("Invalid time format. Please provide the time in days, minutes, and/or seconds.")
        return

    time_str = ""
    if days > 0:
        time_str += f"{days}d "
    if minutes > 0:
        time_str += f"{minutes}m "
    if seconds > 0:
        time_str += f"{seconds}s "

    await ctx.send(f"{ctx.author.mention}, I will remind you in {time_str.strip()} about '{message}'.")
    await asyncio.sleep(time_seconds)
    await ctx.send(f"{ctx.author.mention}, your reminder: '{message}'")

@bot.event
async def on_message_delete(message):
    channel = bot.get_channel(916449762977398804)
    if message.channel == 916449762977398804:
        pass
    else:
        await channel.send(f"***__Message deleted__***\nAuthor: {message.author.mention}\nMessage: {message.content}")

@bot.event
async def on_message_edit(before, after):
    channel = bot.get_channel(916449762977398804)
    if message.channel == 916449762977398804:
        pass
    else:
        await channel.send(f"***__Message edited__***\nAuthor: {before.author}\nBefore: {before.content}\nAfter: {after.content}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)



extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loads every extension.

# Define an event for when the bot is ready to connect to Discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

keep_alive()  # Starts a webserver to be pinged.
token = os.getenv("token") 
bot.run(token)  # Starts the bot