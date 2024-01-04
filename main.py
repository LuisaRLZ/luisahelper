from discord.ext import commands
import os
import discord
from discord import app_commands
from requests_html import AsyncHTMLSession
import re
from keep_alive import keep_alive

TOKEN = os.environ['TOKEN']

#intents = discord.Intents.default()
intents = discord.Intents.all()
client = commands.Bot(command_prefix='+',intents=intents)
bot = client

@client.event
async def on_ready():
    print(f'Connected to bot {client.user.name}')
    print(f'Bot ID: {client.user.id}')
    await client.change_presence(activity=discord.Game('Use +helper'))

@client.command()
async def helper(ctx):
    embed = discord.Embed(title="Guild Helper & Tweaks Bot", description="Use one of the following commands and what you wanna search, for example:", color=0x0DF6EB)

    embed.add_field(name="+item", value="Example: `+item refining gem`", inline=False)
    embed.add_field(name="+monster", value="Example: `+monster black dragon`", inline=False)
    embed.add_field(name="+npc", value="Example: `+npc newbie guide`", inline=False)
    embed.add_field(name="+quest", value="Example: `+quest welcome`", inline=False)

    embed.add_field(name="Other Commands", value="`+tweaks` - Shows you a list of downloadable tweaks\n"
                                                  "`+list` - Creates a list of the current voice channel people\n"
                                                  "`+list2` - Creates a list of the current voice channel people (old version)\n"
                                                  "`+potions` - Gives you information about all Pots & Manu Items\n"
                                                  "`+guides` - Links you to a guides database.\n"
                                                  "`+updatelog` - Shows you a list of things I've updated in this bot\n"
                                                  "`+invite` - Invite this bot to your discord server!\n", inline=False)

    embed.add_field(name="Extras", value="`+bots` - Shows you a list useful bots for your guild\n"
                                                  "`+extras` - Shows you some extra goodies you can use for your guild!\n", inline=False)

    embed.add_field(name="Note", value="This is my Guild Helper & Tweaks bot. It slowly growing to be a great bot! please have some patience for ol Luisa ❤️ More functions will be added soon!", inline=False)

    await ctx.send(embed=embed)


@client.command()
async def updatelog(ctx):
    # Create an embed for the update log
    embed = discord.Embed(title="Update Log", description="Here are the latest updates to the bot:", color=0x0DF6EB)

    # Add fields for each version update
    embed.add_field(name="v0.1", value="Added search functions: `+item`, `+monster`, `+quest`, and `+npc`", inline=False)
    embed.add_field(name="v0.2", value="Added `+tweaks` function and some tweaks", inline=False)
    embed.add_field(name="v0.3", value="Upgraded `+item`, `+monster`, `+quest`, and `+npc` functions further and added some tweaks", inline=False)
    embed.add_field(name="v0.4", value="Fixed bug that caused constant disconnections", inline=False)
    embed.add_field(name="v0.5", value="Added the reaction function to `+list` command", inline=False)
    embed.add_field(name="v0.6", value="Big updates to the `+tweaks` commands!", inline=False)
    embed.add_field(name="Read More:", value="[Click Here](https://docs.google.com/document/d/1-Dd8uMMCnObb7tcYqGkKZTY9L8HcwGy79p6sjIt9E2c/edit?usp=sharing)", inline=False)

    # Send the embed
    await ctx.send(embed=embed)

@client.command(name='potions', aliases=['pots'])
async def potions(ctx):
    embed = discord.Embed(title="Potions & Manufacturing Items Information", color=0x0DF6EB)

    # Add content to the embed
    embed.add_field(name="Check the following Excel Spreadsheet", value="[Pots & Manu Info (Click Here)](https://docs.google.com/spreadsheets/d/1EOgLCjuyRAl06H1sYSfKDdvoJxl3dM4zQgKLXmqil_4/edit?usp=sharing)", inline=False)
    embed.add_field(name="Or Select one of the following:", value="`+recoveryhp`\n`+recoverysp`\n`+potshp`\n`+potssp`\n`+potsattack`\n`+otherpots`\n`+shipmanu`\n`+landmanu`", inline=False)

    await ctx.send(embed=embed)

@client.command(name='recoveryhp', aliases=['hprecovery','hpreco'])
async def recoveryhp(ctx):
    embed = discord.Embed(title="HP Recovery Potions", color=0x0DF6EB)

    # Add image to the embed
    embed.set_image(url='https://i.imgur.com/fvkN1cE.png')

    # Add content to the embed
    embed.add_field(name="Or you can check the following Excel Spreadsheet", value="[Pots & Manu Info (Click Here)](https://docs.google.com/spreadsheets/d/1EOgLCjuyRAl06H1sYSfKDdvoJxl3dM4zQgKLXmqil_4/edit?usp=sharing)", inline=False)

    await ctx.send(embed=embed)

@client.command(name='recoverysp', aliases=['sprecovery','spreco'])
async def recoverysp(ctx):
    embed = discord.Embed(title="SP Recovery Potions", color=0x0DF6EB)

    # Add image to the embed
    embed.set_image(url='https://i.imgur.com/p1G4vjL.png')

    # Add content to the embed
    embed.add_field(name="Or you can check the following Excel Spreadsheet", value="[Pots & Manu Info (Click Here)](https://docs.google.com/spreadsheets/d/1EOgLCjuyRAl06H1sYSfKDdvoJxl3dM4zQgKLXmqil_4/edit?usp=sharing)", inline=False)

    await ctx.send(embed=embed)

@client.command(name='otherpots', aliases=['otherpotions'])
async def otherpots(ctx):
    embed = discord.Embed(title="Other Potions", color=0x0DF6EB)

    # Add image to the embed
    embed.set_image(url='https://i.imgur.com/k8YHhum.png')

    # Add content to the embed
    embed.add_field(name="Or you can check the following Excel Spreadsheet", value="[Pots & Manu Info (Click Here)](https://docs.google.com/spreadsheets/d/1EOgLCjuyRAl06H1sYSfKDdvoJxl3dM4zQgKLXmqil_4/edit?usp=sharing)", inline=False)

    await ctx.send(embed=embed)

@client.command(name='potssp', aliases=['sppots', 'sprpotions', 'potionsspr', 'potsspr','sprpots'])
async def potssp(ctx):
    embed = discord.Embed(title="SPR Potions", color=0x0DF6EB)

    # Add image to the embed
    embed.set_image(url='https://i.imgur.com/z7Pfdwq.png')

    # Add content to the embed
    embed.add_field(name="Or you can check the following Excel Spreadsheet", value="[Pots & Manu Info (Click Here)](https://docs.google.com/spreadsheets/d/1EOgLCjuyRAl06H1sYSfKDdvoJxl3dM4zQgKLXmqil_4/edit?usp=sharing)", inline=False)

    await ctx.send(embed=embed)

@client.command(name='potsattack', aliases=['attackpots', 'potsatt', 'attpots', 'potionsattack', 'attackpotions'])
async def potsatt(ctx):
    embed = discord.Embed(title="Attack/HP Potions", color=0x0DF6EB)

    # Add image to the embed
    embed.set_image(url='https://i.imgur.com/JSicgQQ.png')

    # Add content to the embed
    embed.add_field(name="Or you can check the following Excel Spreadsheet", value="[Pots & Manu Info (Click Here)](https://docs.google.com/spreadsheets/d/1EOgLCjuyRAl06H1sYSfKDdvoJxl3dM4zQgKLXmqil_4/edit?usp=sharing)", inline=False)

    await ctx.send(embed=embed)

@client.command(name='shipmanu', aliases=['seamanu','shipmanufacturing','seamanufacturing'])
async def shipmanu(ctx):
    embed = discord.Embed(title="Ship Manufacturing", color=0x0DF6EB)

    # Add image to the embed
    embed.set_image(url='https://i.imgur.com/xGitlrH.png')

    # Add content to the embed
    embed.add_field(name="Or you can check the following Excel Spreadsheet", value="[Pots & Manu Info (Click Here)](https://docs.google.com/spreadsheets/d/1EOgLCjuyRAl06H1sYSfKDdvoJxl3dM4zQgKLXmqil_4/edit?usp=sharing)", inline=False)

    await ctx.send(embed=embed)

@client.command(name='landmanu', aliases=['manu','landmanufacturing','manufacturing'])
async def landmanu(ctx):
    embed = discord.Embed(title="Land Manufacturing", color=0x0DF6EB)

    # Add image to the embed
    embed.set_image(url='https://i.imgur.com/zhYy6tm.png')

    # Add content to the embed
    embed.add_field(name="Or you can check the following Excel Spreadsheet", value="[Pots & Manu Info (Click Here)](https://docs.google.com/spreadsheets/d/1EOgLCjuyRAl06H1sYSfKDdvoJxl3dM4zQgKLXmqil_4/edit?usp=sharing)", inline=False)

    await ctx.send(embed=embed)

@client.command(name='potshp', aliases=['hppots'])
async def potshp(ctx):
    embed = discord.Embed(title="HP Potions", color=0x0DF6EB)

    # Add image to the embed
    embed.set_image(url='https://i.imgur.com/el6sj9b.png')

    # Add content to the embed
    embed.add_field(name="Or you can check the following Excel Spreadsheet", value="[Pots & Manu Info (Click Here)](https://docs.google.com/spreadsheets/d/1EOgLCjuyRAl06H1sYSfKDdvoJxl3dM4zQgKLXmqil_4/edit?usp=sharing)", inline=False)

    await ctx.send(embed=embed)

@client.command()
async def list(ctx):
    if not ctx.author.voice:
        return await ctx.send('👈 Please join a voice channel first then try again')

    channel = ctx.author.voice.channel
    members = channel.members
    original_names = {member.id: member.display_name for member in members}

    embed = discord.Embed(title="Maze List by Luisa RLZ", color=0x0DF6EB)
    information_line = (
        "**React 🖐️ to get added if you assisted but missed in the list. ❌ To remove yourself. You got 1 hour. Use `+list2` for a list without emoji. Use `+invite` to add this bot to your server.**"
    )
    embed.description = (
        f"{information_line}\n\n**Members:**\n" + '\n'.join(original_names.values()) + "\n\n**----DROPS----**"
    )

    # Send the initial message with the list
    msg = await ctx.send(embed=embed)

    # Add the emoji to the message (changed to 🖐️ and ❌)
    await msg.add_reaction("🖐️")
    await msg.add_reaction("❌")

    # Allow continuous updates until a certain condition is met
    while True:
        try:
            # Wait for a reaction or a message with a 1-hour timer
            reaction, user = await client.wait_for('reaction_add', timeout=3600.0)
        except asyncio.TimeoutError:
            break  # Exit the loop if the timeout occurs
        else:
            if str(reaction.emoji) == '🖐️':
                # Add the new name to the original list with the 🖐️ emoji
                original_names[user.id] = f"{ctx.guild.get_member(user.id).display_name} 🖐️"
            elif str(reaction.emoji) == '❌':
                # Handle self-removal reaction
                original_names.pop(user.id, None)

            # Check if the reaction corresponds to the original message
            if reaction.message.id == msg.id:
                # Concatenate the information line, original names, and drops line
                updated_description = (
                    f"{information_line}\n\n**Members:**\n" + '\n'.join(original_names.values()) + "\n\n**----DROPS----**"
                )

                # Edit the original message with the updated list
                embed.description = updated_description
                await msg.edit(embed=embed)

                # await ctx.send(f"List updated with reactions within 1 hour.")


@client.command()
async def list2(ctx):
    if not ctx.author.voice:
        return await ctx.send('👈 Please join a voice channel first then try again')

    channel = ctx.author.voice.channel
    members = channel.members
    memids = [member.display_name for member in members]

    embed = discord.Embed(title="Maze List by Luisa RLZ", color=0x0DF6EB)
    embed.add_field(name="Members:", value='\n'.join(memids), inline=False)
    embed.add_field(name=" ", value="**----DROPS----**", inline=False)

    await ctx.send(embed=embed)

async def search_and_send(ctx, search_type, text):
  formatted_text = text.replace(" ", "+")
  base_url = f"https://pirateking.online/database/{search_type}/?name="
  full_url = base_url + formatted_text

  asession = AsyncHTMLSession()
  async def search():
      response = await asession.get(full_url)
      return response

  result = await search()
  result_data = [element.text for element in result.html.find('.database-id')]
  result_id = (' \n'.join(result_data)).split()[1]

  url = f"https://pirateking.online/database/{search_type}/{formatted_text}.{result_id}"

  await ctx.send(f"{url}\n"
                 f"You may click the link above, remember to type the name of your search as accurately as possible for better results 👍\n"
                 f"You may also check close results by opening this link: <{full_url}>")


@client.command()
async def item(ctx, *, text):
  await search_and_send(ctx, "item", text)

@client.command()
async def monster(ctx, *, text):
  await search_and_send(ctx, "monster", text)

@client.command()
async def quest(ctx, *, text):
  await search_and_send(ctx, "quest", text)

@client.command()
async def npc(ctx, *, text):
    message = ctx.message
    formatted_text = text.replace(" ", "-")
    url_base = "https://pirateking.online/database/npc/?name="
    url_full = url_base + formatted_text
    asession = AsyncHTMLSession()

    async def NpcSearch():
        response = await asession.get(url_full)
        return response

    npc_search = await NpcSearch()
    npc_search_data = [element.text for element in npc_search.html.find('.database-id')]
    npc_search_garner = (' \n'.join(npc_search_data)).split()[1]
    npc_search_id = (' \n'.join(npc_search_data)).split()[3]
    print(npc_search_id)

    result_url = f"https://pirateking.online/database/npc/{npc_search_garner}/{formatted_text}.{npc_search_id}"

    await ctx.send(f"{result_url}\n"
                   f"You may click the link above, remember to type the name of your search as accurately as possible for better results 👍\n"
                   f"You may also check close results by opening this link: <{url_full}>")

@client.command()
async def tweaks(ctx):
    embed = discord.Embed(title="TWEAKS INDEX 2024", description="Which server do you need Tweaks for? Use one of the following codes to obtain the desired tweaks:", color=0x0DF6EB)

    # Compilations
    compilations_value = (
        "(Download Tweaks Packages)\n\n"
        "`+poaio` A single package containing all Pirates Online Tweaks\n"
        "`+pkoaio` A single package containing all Pirate King Online Tweaks"
    )
    embed.add_field(name="Compilations", value=compilations_value, inline=False)

    # Individual Tweaks
    individual_tweaks_value = (
        "(In case you prefer picking individual files)\n\n"
        "`+tweaksall` Tweaks for any server\n"
        "`+tweakspko` Tweaks for Pirate King Online\n"
        "`+tweakspo` Tweaks for Pirates Online\n"
        "`+tweaksroso` Tweaks for Rage of Sage Online\n"
        "`+tweaksindex` Links you to the classic Tweaks Index\n"
    )
    embed.add_field(name="Individual Tweaks", value=individual_tweaks_value, inline=False)

    # Extras
    extras_value = (
        "(Other Resources)\n\n"
        "`+bots` Useful Discord Bots\n"
        "`+invite` Invite this Bot to your server\n"
        "`+extras` More Resources for your game\n"
        "`+pots` List of Potions & Manu in-game\n"
    )
    embed.add_field(name="Extras", value=extras_value, inline=False)

    # Website
    embed.add_field(name="Website", value="Or you may also pick them from my website! [Click Here](https://luisarlzproductions.com/tweaks/tweaks-main.html)", inline=False)

    await ctx.send(embed=embed)

@client.command(name='tweaksall', aliases=['alltweaks'])
async def tweaksall(ctx):
    embed = discord.Embed(title="TWEAKS FOR ANY SERVER", description="Use one of the following codes to obtain the desired tweak:\n*Please note, however, that some tweaks might not work in some servers as these are base tweaks, but they still have high odds of working in any server.*", color=0x0DF6EB)

    basic_tweaks_value = (
    "`+camera` Allows you to see the game from a higher point of view\n"
    "`+animation` Eliminates annoying casting animations, attacks faster\n"
    "`+nightargent` Makes all floor textures darker\n"
  )
    embed.add_field(name="Basic Tweaks", value=basic_tweaks_value, inline=False)

    embed.add_field(
      name="Visual Tweaks",
      value=(
          "`+ts` Allows you to see skill True Sight easily, with a big yellow square\n"
          "`+seal` Adds a 'Rec Me' emoji above sealed target\n"
          "`+aoeskull` Changes AoE Skull into a dotted square\n"
          "`+slash` Changes the color of Illusion Slash\n"
          "`+noglows` Gets rid of all weapon glows\n"
          "`+topperf` File .exe to eliminate effects in game\n"
          "`+buffs` Makes buffs smaller and easier to see\n"
          "`+emojis` Changes emojis to Pepes, Anime, Heal me and more!\n"
          "`+lucky` Changes the colors of different Lucky Packets\n"
          "`+bps` Changes the colors of different Blue Prints\n"
          "`+indicators` Changes the shapes of enemy/friend indicators\n"
          "`+flashbomb` Changes the visibility of flash bombs\n"
          "`+hiteffect` Removes melee visual hit effect\n"
      ),
      inline=False
  )

    embed.add_field(
      name="Guilds",
      value=(
          "`+bots` Gives you a list of useful Discord Bots for Guilds\n"
          "`+invite` Invite this Bot to your server\n"
          "`+extras` Gives you a list of Excel Systems and more!\n"
          "`+pots` List of Potions & Manu in-game\n"
      ),
      inline=False
  )

    await ctx.send(embed=embed)

@client.command(name='pkotweaks', aliases=['tweakspko'])
async def tweakspko(ctx):
    embed = discord.Embed(title="TWEAKS FOR PIRATE KING ONLINE", description="Use one of the following codes to obtain the desired tweak:", color=0x0DF6EB)

    basic_tweaks_value = (
      "`+pkoaio` Contains all Tweaks in an All-In-One package\n"
      "`+camera` Allows you to see the game from a higher point of view\n"
      "`+animation` Eliminates annoying casting animations, attacks faster\n"
      "`+nightargent` Makes all floor textures darker\n"
      "`+blackskin` Gives you a cool User Interface!\n"
  )
    embed.add_field(name="Basic Tweaks", value=basic_tweaks_value, inline=False)

    embed.add_field(name="PK Tweaks", value="`+nomelee` Tweak to not melee on targets on magic classes", inline=False)

    embed.add_field(
        name="Visual Tweaks",
        value=(
            "`+bigbarspko` Adds bigger HP and SP bars\n"
            "`+ts` Allows you to see skill True Sight easily, with a big yellow square\n"
            "`+seal` Adds a 'Rec Me' emoji above sealed target\n"
            "`+aoeskull` Changes AoE Skull into a dotted square\n"
            "`+slash` Changes the color of Illusion Slash\n"
            "`+noglows` Gets rid of all weapon glows\n"
            "`+topperf` File .exe to eliminate effects in game\n"
            "`+buffs` Makes buffs smaller and easier to see\n"
            "`+emojis` Changes emojis to Pepes, Anime, Heal me and more!\n"
            "`+lucky` Changes the colors of different Lucky Packets\n"
            "`+bps` Changes the colors of different Blue Prints\n"
            "`+indicators` Changes the shapes of enemy/friend indicators\n"
            "`+flashbomb` Changes the visibility of flash bombs\n"
            "`+hiteffect` Removes melee visual hit effect\n"
            "`+effectspko` Adds several effect tweaks for a better visualization of potions and certain skills\n"
            "`+restore` Restores textures files to be editable\n"
            "`+mapeditor` Downloads Amu's Map Editor\n"
            "`+decompiler` Downloads deguix decompiler with instructions\n"
        ),
        inline=False
    )

    embed.add_field(
        name="Guilds",
        value=(
            "`+bots` Gives you a list of useful Discord Bots for Guilds\n"
            "`+invite` Invite this Bot to your server\n"
            "`+extras` Gives you a list of Excel Systems and more!\n"
            "`+pots` List of Potions & Manu in-game\n"
        ),
        inline=False
    )

    embed.set_thumbnail(url="https://i.imgur.com/QvSh7yh.png")

    await ctx.send(embed=embed)

@client.command(name='potweaks', aliases=['tweakspo'])
async def tweakspo(ctx):
    embed = discord.Embed(title="TWEAKS FOR PIRATES ONLINE", description="Use one of the following codes to obtain the desired tweak:", color=0x0DF6EB)

    basic_tweaks_value = (
    "`+poaio` Contains all Tweaks in an All-In-One package\n"
    "`+nightargent` Makes all floor textures darker\n"
  )
    embed.add_field(name="Basic Tweaks", value=basic_tweaks_value, inline=False)

    embed.add_field(name="Built-in Tweaks", value="`+builtinpo` Info about Built-in client tweaks (no download required)", inline=False)

    embed.add_field(
      name="Visual Tweaks",
      value=(
          "`+bigbarspo` Adds bigger HP and SP bars\n"
          "`+ts` Allows you to see skill True Sight easily, with a big yellow square\n"
          "`+seal` Adds a 'Rec Me' emoji above sealed target\n"
          "`+aoeskull` Changes AoE Skull into a dotted square\n"
          "`+slash` Changes the color of Illusion Slash\n"
          "`+noglows` Gets rid of all weapon glows\n"
          "`+topperf` File .exe to eliminate effects in game\n"
          "`+buffs` Makes buffs smaller and easier to see\n"
          "`+emojis` Changes emojis to Pepes, Anime, Heal me and more!\n"
          "`+lucky` Changes the colors of different Lucky Packets\n"
          "`+bps` Changes the colors of different Blue Prints\n"
          "`+indicators` Changes the shapes of enemy/friend indicators\n"
          "`+flashbomb` Changes the visibility of flash bombs\n"
          "`+cleandreampo` Removes buildings and plants in Dream Island map\n"
          "`+hiteffect` Removes melee visual hit effect\n"
          "`+effectspo` Adds several effect tweaks for a better visualization of potions and certain skills\n"
      ),
      inline=False
  )

    embed.add_field(
      name="Guilds",
      value=(
          "`+bots` Gives you a list of useful Discord Bots for Guilds\n"
          "`+invite` Invite this Bot to your server\n"
          "`+extras` Gives you a list of Excel Systems and more!\n"
          "`+pots` List of Potions & Manu in-game\n"
      ),
      inline=False
  )

    embed.set_thumbnail(url="https://i.imgur.com/sJeQmW9.png")

    await ctx.send(embed=embed)



# Define create_generic_command function
def create_generic_command(name, title, description, param1, value1, param2, value2, submit, submitdesc, download_urls, thumbnail_url, thumbnail_image_url, default_author_icon_url, authorname, pkoonly, pkoonlydesc, poonly, poonlydesc, footer_text):
    # Set default values for pkoonly and poonly if not provided
    if pkoonly is not None:
        pkoonly = "NOTE:"
    if pkoonlydesc is not None:
        pkoonlydesc = "This tweak is meant exclusively for PKO. Please do not install in other servers. Use command `+tweaks` to see the full list of tweaks for your server"
    if poonly is not None:
        poonly = "NOTE:"
    if poonlydesc is not None:
        poonlydesc = "This tweak is meant exclusively for PO. Please do not install in other servers. Use command `+tweaks` to see the full list of tweaks for your server"
    default_author_icon_url = "https://i.imgur.com/nDenrwc.png"
    if submit is not None:
      submit = "Customize it:"
    if submitdesc is not None:
      submitdesc = "[Create your own Tweak](https://docs.google.com/document/d/1VKqRaujjA89kEjGxWQ9r7cigJm1auBO_SqkShUS-M7c/edit) | [Community Tweaks Folder](https://drive.google.com/drive/folders/13uEfZkHBD199DfumYr8v1ecOlsR3CCG7)"
    default_author_icon_url = "https://i.imgur.com/nDenrwc.png"

    @client.command(name=name, help=description)
    async def command(ctx, *args):
        # Use the provided title or capitalize the first letter of each word in the command name
        embed_title = title or ' '.join(word.capitalize() for word in name.split('_'))

        # Command logic using 'args'
        embed = discord.Embed(title=embed_title, description=description, color=0x0DF6EB)  # You can customize the color

        # Set author with icon and name
        embed.set_author(name=authorname, icon_url=default_author_icon_url)

        # Add "param1" and "value1" in the "details" section
        embed.add_field(name=param1, value=value1, inline=False)

        # Add the optional pkoonly value below the "How to Install" section
        if submit and submitdesc:
          embed.add_field(name=submit, value=submitdesc, inline=False)

        # Add "How to Install" section with common URLs
        embed.add_field(name="How to Install", value=f"[Manual (All Servers)](https://youtu.be/bnu_W712-Zg?si=lzchb7LyuUlNfR8J&t=65)\n[PKO EZ (PKO Only)](https://www.youtube.com/watch?v=Nvw2J2vBuIY&t)", inline=False)

        # Add another "param1" and "value1" line below the "How to Install" section
        embed.add_field(name=param2, value=value2, inline=False)

        # Add the optional pkoonly value below the "How to Install" section
        if pkoonly and pkoonlydesc:
            embed.add_field(name=pkoonly, value=pkoonlydesc, inline=False)

        # Add the optional poonly value below the "How to Install" section
        if poonly and poonlydesc:
            embed.add_field(name=poonly, value=poonlydesc, inline=False)

        # Set thumbnail with caption
        embed.set_thumbnail(url=thumbnail_url)

        # Set additional thumbnail image at the end of the embed
        embed.set_image(url=thumbnail_image_url)

        # Set the footer if provided, otherwise use a default footer
        if footer_text:
            embed.set_footer(text=footer_text)
        else:
            embed.set_footer(text="This is a preview. Tweak downloaded from luisarlzproductions.com. Use +invite to invite this bot to your Discord Server.")

        await ctx.send(embed=embed)

# Create commands using create_generic_command
##################################################################################
############### EXAMPLE EXAMPLE EXAMPLE ##########################################
##################################################################################
commands_info = {
    "example": {
        "title": "Example title",  # edit value
        "description": "Example description",
        "param1": "Author(s):",
        "value1": "Example",  # edit author
        "submit": "submit",
        "submitdesc": "submitdesc",
        "param2": "Download",
        "value2": "[Click Here (Manual Install)](examplelink.com)",  # edit link
        "thumbnail_image_url": "https://www.examplebigimagelink.com",  # edit image big
        #"pkoonly": "pkoonly",  # add for pko, use None if not needed
        #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
        #"poonly": None,  # add for po, use None if not needed
        #"poonlydesc": None,  # add for po, use None if not needed
        "authorname": "Example Author",
        "footer_text": " ",  # Add your custom footer here
    },

    ##################################################################################
    ############### NO MELEE TWEAK ###################################################
    ##################################################################################
    "nomelee": {
        "title": "No Melee Tweak",
        "description": "With this, you will not be able to click on targets accidentally and get pulled to them and die.",
        "param1": "Author(s):",
        "value1": "DevilEX",
        "submit": "submit",
        "submitdesc": "submitdesc",
        "param2": "Download",
        "pkoonly": "pkoonly",
        "pkoonlydesc": "pkoonlydesc",
        "value2": "[Click Here (Manual Install)](https://luisarlzproductions.com/tweaks/files/No_Melee_Tweak.rar)",
        "thumbnail_image_url": "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjFvczQwbDEyb24yMXRwMHYyOTMwcXg3ZTg5d2gwNDBqNWU3NnYycyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/mohcoDYdcK05E7IaOs/giphy.gif",
        "authorname": "[PK Tweak] For Magics",
    },

    ##################################################################################
    ############### TS TWEAK ############## ##########################################
    ##################################################################################

    "ts": {
        "title": "TS Tweak",  # edit value
        "description": "You will be able to see enemy and friend True Sight on floor. Tweak used in preview = Red 2",
        "param1": "Author(s):",
        "value1": "Jaxxen, LuisaRLZ, ToNy",  # edit author
        "submit": "submit",
        "submitdesc": "submitdesc",
        "param2": "Downloads",
        "value2": "[Jaxxen Ver](https://luisarlzproductions.com/tweaks/files/yellow-ts-po.rar) | [Eye Ver](https://luisarlzproductions.com/tweaks/files/ts-square-po.rar) | [Luisa Blue](https://luisarlzproductions.com/tweaks/files/luisa-ts-tweak-blue.rar) | [Luisa Yellow]( https://luisarlzproductions.com/tweaks/files/luisa-ts-tweak-yellow.rar) | [Luisa Pink]( https://luisarlzproductions.com/tweaks/files/luisa-ts-tweak-pink.rar) | [Luisa Rainbow]( https://luisarlzproductions.com/tweaks/files/luisa-ts-tweak-rainbow.rar) | [Luisa Red]( https://luisarlzproductions.com/tweaks/files/luisa-ts-tweak-red.rar) | [Blue 2]( https://luisarlzproductions.com/tweaks/files/luisa-ts-tweak-blue-2.rar) | [Yellow 2]( https://luisarlzproductions.com/tweaks/files/luisa-ts-tweak-yellow-2.rar) | [Pink 2]( https://luisarlzproductions.com/tweaks/files/luisa-ts-tweak-pink-2.rar) | [Rainbow 2]( https://luisarlzproductions.com/tweaks/files/luisa-ts-tweak-rainbow-2.rar) | [Red 2]( https://luisarlzproductions.com/tweaks/files/luisa-ts-tweak-red-2.rar) | ",  # edit link
        "thumbnail_image_url": "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGQ1MHlhaHhwcnZuM3BrM2d1aWs4MnlxaXJ2Nm92azFhMHJ1bDMxbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TCcWq4ckyRgN5vTbFe/giphy.gif",  # edit image big
        "authorname": "[PK Tweak] For Cler, SM, Crus",
    },

  ##################################################################################
  ############### PKO AIO ##########################################
  ##################################################################################
      "pkoaio": {
          "title": "PKO All-In-One",  # edit value
          "description": "A compilation of all useful PKO Tweaks. Read .txt inside to see which tweaks are currently included.",
          "param1": "Author(s):",
          "value1": "LuisaRLZ",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download",
          "value2": "[Click Here (PKO EZ)](https://luisarlzproductions.com/tweaks/files/PKO-EZ-All-In-One.rar)",  # edit link
          "thumbnail_image_url": "https://i.imgur.com/FUXaTpd.png",  # edit image big
          "pkoonly": "pkoonly",  # add for pko, use None if not needed
          "pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": None,  # add for po, use None if not needed
          #"poonlydesc": None,  # add for po, use None if not needed
          "authorname": "[All-In-One PKO]",
          "footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### PO AIO ##########################################
  ##################################################################################
      "poaio": {
          "title": "PKO All-In-One",  # edit value
          "description": "A compilation of all useful PO Tweaks. Read .txt inside to see which tweaks are currently included.",
          "param1": "Author(s):",
          "value1": "LuisaRLZ",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download",
          "value2": "[Click Here (Manual Install)](https://luisarlzproductions.com/tweaks/files/PO-EZ-All-In-One-2.rar)",  # edit link
          "thumbnail_image_url": "https://i.imgur.com/ovh16O7.png",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          "poonly": "poonly",  # add for po, use None if not needed
          "poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[All-In-One PO]",
          "footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### NIGHT ARGENT ##########################################
  ##################################################################################
      "nightargent": {
          "title": "Night Argent Tweak",  # edit value
          "description": "Makes all floors darker and cooler-looking. It helps with sensitive eyes. Tweak in preview = Luisa's HD",
          "param1": "Author(s):",
          "value1": "LuisaRLZ, Rami, Clerigo",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Downloads (Manual Installs):",
          "value2": "[Classic]( https://luisarlzproductions.com/tweaks/files/black-floor-po.rar) | [Fancy Tile](https://luisarlzproductions.com/tweaks/files/fancy-tile-po.rar) | [Clerigo’s]( https://luisarlzproductions.com/tweaks/files/clerigo-black-floor-po.rar) | [Luisa’s HD Day]( https://luisarlzproductions.com/tweaks/files/hd-floor-textures.rar) | [Luisa’s HD Night #1]( https://luisarlzproductions.com/tweaks/files/hd-night-argent.rar) | [Luisa’s HD Night #2]( https://luisarlzproductions.com/tweaks/files/hd-night-argent-2.rar)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/gi2hgOt.png",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For sensitive eyes",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### CAMERA ##########################################
  ##################################################################################
      "camera": {
          "title": "Camera Tweak",  # edit value
          "description": "Upgrades your field of view so you can actually see what is happening in PK! with this your gameplay experience will be a lot more fluid",
          "param1": "Author(s):",
          "value1": "LuisaRLZ, Lipstick, Gabo, iRuin",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Downloads (Manual Installs):",
          "value2": "[Classic](https://luisarlzproductions.com/tweaks/files/classic-camera-tweak.rar) | [Lipstick’s](https://luisarlzproductions.com/tweaks/files/lipstick-camera.rar) | [Gabo’s](https://luisarlzproductions.com/tweaks/files/fun-camera-2.rar) | [iRuin’s](https://luisarlzproductions.com/tweaks/files/fun-camera-3.rar) | [Wide Camera](https://luisarlzproductions.com/tweaks/files/wide-camera.rar)", # edit link
          "thumbnail_image_url": "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNndjd3ZkYzhkZmQ5dDRpdG9jY2hhMGlpYWJ4cXZ0bjNjNnFqMnZzNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oj2SGZyVOlFeI7YTbI/giphy.gif",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Basic Tweak] For everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### ANIMATION ##########################################
  ##################################################################################
      "animation": {
          "title": "Animation Tweak",  # edit value
          "description": "Makes all skill and melee animations a lot shorter for a more fluid gameplay experience. Please note, however, as instructed inside the .txt file, you may need to manually edit the file if the server you play uses custom monsters.",
          "param1": "Author(s):",
          "value1": "LuisaRLZ, DevilEX, Hollister, Liz, Apex",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Downloads (Manual Installs):",
          "value2": "[Classic All Mobs]( https://luisarlzproductions.com/tweaks/files/classic-animation-tweak-all-mobs.rar) | [Classic No DW Mobs]( https://luisarlzproductions.com/tweaks/files/classic-animation-tweak-no-dw-mobs.rar) | [Modern 2021 Vanilla All Mobs](https://luisarlzproductions.com/tweaks/files/modern-animation-all-mobs.rar) | [Modern 2021 No DW Mobs](https://luisarlzproductions.com/tweaks/files/modern-animation-no-dw.rar)  | [Modern 2021 PO](https://luisarlzproductions.com/tweaks/files/animation-tweak-2021-po.rar)", # edit link
          "thumbnail_image_url": "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGdwZzhld2dtazB2bXlxNmFiYXJjbGpqY2hiam15dDllYXV5ZjV5dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bhp4UX5kVsKypX9R9Z/giphy.gif",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Basic Tweak] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### SEAL ##########################################
  ##################################################################################
      "seal": {
          "title": "Seal Tweak",  # edit value
          "description": "Adds a crying squid emoji on sealed targets",
          "param1": "Author(s):",
          "value1": "Jaxxen",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download (Manual Install)",
          "value2": "[Click Here](https://luisarlzproductions.com/tweaks/files/seal-tweak-po.rar)", # edit link
          "thumbnail_image_url": "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXFvcjh2aWh1Mm50aGFjejFseW1mbGptYXZ0enQ5N2U1YjkybG9hdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/mcV5Xb5QxWeJjt54M4/giphy.gif",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### EFFECTS PKO ##########################################
  ##################################################################################
      "effectspko": {
          "title": "Effects Tweak for PKO",  # edit value
          "description": "Adds effects to most pots in-game as well as some skills. It can get pretty heavy on the eyes, however...",
          "param1": "Author(s):",
          "value1": "Punish3r",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download (Manual Install)",
          "value2": "[Click Here](https://luisarlzproductions.com/tweaks/files/effects-pko.rar)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/CUImJF7.png",  # edit image big
          "pkoonly": "pkoonly",  # add for pko, use None if not needed
          "pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### EFFECTS PO ##########################################
  ##################################################################################
      "effectspo": {
          "title": "Effects Tweak for PO",  # edit value
          "description": "Adds effects to most pots in-game as well as some skills. It can get pretty heavy on the eyes, however...",
          "param1": "Author(s):",
          "value1": "Unknown",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download (Manual Install)",
          "value2": "[Click Here](https://luisarlzproductions.com/tweaks/files/pots-glow-tweak-po.rar)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/ic3XrFM.png",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          "poonly": "poonly",  # add for po, use None if not needed
          "poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### BLACK SKIN PKO ##########################################
  ##################################################################################
      "blackskin": {
          "title": "Black Sk--- I mean, Dark UI",  # edit value
          "description": "Gives you a cool user interface!",
          "param1": "Author(s):",
          "value1": "LuisaRLZ, PKO Community, Noir",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download (Manual Install)",
          "value2": "[Click Here](https://luisarlzproductions.com/tweaks/files/pko-black-skin.rar)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/msoNc2I.png",  # edit image big
          "pkoonly": "pkoonly",  # add for pko, use None if not needed
          "pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### BIG BAR PKO ##########################################
  ##################################################################################
      "bigbarspko": {
          "title": "Big Bars PKO",  # edit value
          "description": "Makes your HP and SP bars bigger",
          "param1": "Author(s):",
          "value1": "LuisaRLZ",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download (Manual Install)",
          "value2": "[Click Here](https://luisarlzproductions.com/tweaks/files/better-bars-pko.rar)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/cilh1A4.png",  # edit image big
          "pkoonly": "pkoonly",  # add for pko, use None if not needed
          "pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### BIG BAR PO ##########################################
  ##################################################################################
      "bigbarspo": {
          "title": "Big Bars PO",  # edit value
          "description": "Makes your HP and SP bars bigger",
          "param1": "Author(s):",
          "value1": "LuisaRLZ",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download (Manual Install)",
          "value2": "[Click Here](https://luisarlzproductions.com/tweaks/files/better-bars-pko.rar)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/ysH6D9i.png",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          "poonly": "poonly",  # add for po, use None if not needed
          "poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### DECOMPILER ##########################################
  ##################################################################################
      "decompiler": {
          "title": "Deguix Decompiler",  # edit value
          "description": "Decompiles bin files of the game folder. It might not work with newer files.",
          "param1": "Author(s):",
          "value1": "Deguix",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download",
          "value2": "[Click Here](https://luisarlzproductions.com/tweaks/files/top-decompiler.zip)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/C0ouYhX.jpg",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          #"authorname": "[Visual Tweak] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### RESTORE ##########################################
  ##################################################################################
      "restore": {
          "title": "Restore.Exe",  # edit value
          "description": "Run .exe in main folder to restore some texture files. Will not work with newer files.",
          "param1": "Author(s):",
          "value1": "Unknown",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download",
          "value2": "[Click Here](https://luisarlzproductions.com/tweaks/files/restore.rar)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/qOvdecT.png",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          #"authorname": "[Visual Tweak] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### AMU EDITOR ##########################################
  ##################################################################################
      "mapeditor": {
          "title": "Amu Map Editor",  # edit value
          "description": "You may edit your map files with this. Copy-paste the maps you'll edit. Open Editor.bat. Save and Copy-paste the new maps back into game folder.",
          "param1": "Author(s):",
          "value1": "Amu",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download",
          "value2": "[Click Here](https://mega.nz/file/LBEXALra#MjXrfVH4DzcIWcy1KHU6L_RbobJCSB3MFSkS0NAhyqQ)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/krIdpIq.png",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          #"authorname": "[Visual Tweak] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### SLASH ##########################################
  ##################################################################################
      "slash": {
          "title": "Slash Color Tweak",  # edit value
          "description": "Changes the color of Illusion Slash",
          "param1": "Author(s):",
          "value1": "LuisaRLZ",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Downloads (Manual Installs)",
        "value2": "[Red]( https://luisarlzproductions.com/tweaks/files/dragon-slash-red.rar) | [Yellow](https://luisarlzproductions.com/tweaks/files/dragon-slash-yellow.rar) | [Green](https://luisarlzproductions.com/tweaks/files/dragon-slash-green.rar) | [Blue](https://luisarlzproductions.com/tweaks/files/dragon-slash-blue.rar) | [Black](https://luisarlzproductions.com/tweaks/files/dragon-slash-black.rar) | ", # edit link
          "thumbnail_image_url": "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWg5N201aGVhaHZwbWgyNjdzOTVzdXcwNnk4Y2tpY3p4eDhuNG1xaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xmhdAkrsmrEDJhkWA3/giphy.gif",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For Crusader",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### INDICATORS ##########################################
  ##################################################################################
      "indicators": {
          "title": "Indicator Shapes",  # edit value
          "description": "Changes the shapes of Indicators",
          "param1": "Author(s):",
          "value1": "LuisaRLZ",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Downloads (Manual Installs)",
        "value2": "[Star](https://luisarlzproductions.com/tweaks/files/indicator-star.rar) | [Circle](https://luisarlzproductions.com/tweaks/files/indicator-circle.rar) | [Heart](https://luisarlzproductions.com/tweaks/files/indicator-heart.rar) | [Square](https://luisarlzproductions.com/tweaks/files/indicator-square.rar) | [Original](https://luisarlzproductions.com/tweaks/files/indicator-og.rar) | ", # edit link
          "thumbnail_image_url": "https://i.imgur.com/Douxu6Y.png",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### AOESKULL ##########################################
  ##################################################################################
      "aoeskull": {
          "title": "Mofa Tweak",  # edit value
          "description": "Changes the shape of the AoE skull into a dotted square for improved visibility",
          "param1": "Author(s):",
          "value1": "LuisaRLZ",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download (Manual Install)",
        "value2": "[Click Here](https://luisarlzproductions.com/tweaks/files/mofa-tweak-1.rar)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/KAzt72f.png",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### NO GLOWS ##########################################
  ##################################################################################
      "noglows": {
          "title": "No Glows Tweak",  # edit value
          "description": "Eliminates all weapon glows. Improves visibility and decreases PC usage.",
          "param1": "Author(s):",
          "value1": "LuisaRLZ",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download (Manual Install)",
        "value2": "[Click Here](https://luisarlzproductions.com/tweaks/files/glows-tweak.rar)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/96TuE2Q.png",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### BUFFS ##########################################
  ##################################################################################
      "buffs": {
          "title": "Buffs Tweak",  # edit value
          "description": "Makes buffs smaller and easier to see.",
          "param1": "Author(s):",
          "value1": "LuisaRLZ, Jaxxen, Rami",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download (Manual Install)",
        "value2": "[Version 1](https://luisarlzproductions.com/tweaks/files/buffs-tweak-v1-po.rar) | [Version 2](https://luisarlzproductions.com/tweaks/files/buffs-tweak-v2-po.rar) | [Jaxxen’s](https://luisarlzproductions.com/tweaks/files/buffs-tweak.rar)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/3FdyvX2.png",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### EMOJIS ##########################################
  ##################################################################################
      "emojis": {
          "title": "Emojis Tweaks",  # edit value
          "description": "Changes the default emojis into different ones. Only the ones who have the same tweak installed will see them, otherwise the original emoji will be displayed.",
          "param1": "Author(s):",
          "value1": "LuisaRLZ, Unknown",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Downloads (Manual Installs)",
        "value2": "[Heal, Buff, Reco](https://luisarlzproductions.com/tweaks/files/emojis-po.rar) | [Pepes](https://luisarlzproductions.com/tweaks/files/emojis-po-pepe.rar) | [Anime Girls](https://luisarlzproductions.com/tweaks/files/emojis-po-2.rar)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/DAfVoDd.png",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### LUCKY ##########################################
  ##################################################################################
      "lucky": {
          "title": "Lucky Packets Tweak",  # edit value
          "description": "Changes the color of Lucky, Fortune and Prosperous packets",
          "param1": "Author(s):",
          "value1": "LuisaRLZ",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download (Manual Install)",
        "value2": "[Click Here](https://luisarlzproductions.com/tweaks/files/lucky-tweak.rar)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/zMQ1pnf.png",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For Choppers",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### BPS ##########################################
  ##################################################################################
      "bps": {
          "title": "Blueprints Tweak",  # edit value
          "description": "Changes the color of Cooking, Crafting and Manufacturing Blueprints",
          "param1": "Author(s):",
          "value1": "LuisaRLZ",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download (Manual Install)",
        "value2": "[Click Here](https://luisarlzproductions.com/tweaks/files/bps-tweak.rar)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/rVXmKYs.png",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For Life Skills Users",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### HIT EFFECT ##########################################
  ##################################################################################
      "hiteffect": {
          "title": "Hit Effect Removal",  # edit value
          "description": "Removes the visual effect of melee hit to improve visibility",
          "param1": "Author(s):",
          "value1": "LuisaRLZ",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download (Manual Install)",
        "value2": "[Click Here](https://luisarlzproductions.com/tweaks/files/remove-hit-effect.rar)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/nm7a8Ie.png",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For Melee users",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### FLASH BOMBS ##########################################
  ##################################################################################
      "flashbomb": {
          "title": "Flash Bomb Tweak",  # edit value
          "description": "Changes the visual effect of flash bomb to improve visibility. Tweak shown in preview = Version 1",
          "param1": "Author(s):",
          "value1": "LuisaRLZ, Darius",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download (Manual Install)",
        "value2": "[Version 1](https://luisarlzproductions.com/tweaks/files/fb-tweak-po.rar) | [Version 2](https://luisarlzproductions.com/tweaks/files/fb-tweak-2-po.rar) | [Version 3](https://luisarlzproductions.com/tweaks/files/fb-tweak-3-po.rar)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/7078jlt.png",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### TOPPERF ##########################################
  ##################################################################################
      "topperf": {
          "title": "Topperf.exe",  # edit value
          "description": "File .exe that allows you to remove a lot of effects from the game. Download, put .exe file inside main game folder and double click to run.",
          "param1": "Author(s):",
          "value1": "Unknown",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "Download (Manual Install)",
        "value2": "[Click Here](https://luisarlzproductions.com/tweaks/files/topperf.rar)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/EEtmI50.png",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          #"poonly": "poonly",  # add for po, use None if not needed
          #"poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### BUILTIN ##########################################
  ##################################################################################
      "builtinpo": {
          "title": "Built-in Tweaks for PO",  # edit value
          "description": "Press the Esc Key to get equivalents of camera, no melee and glows tweaks among others. Click more information to read about what every option does.",
          "param1": "Author(s):",
          "value1": "PO Staff",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "More Information",
        "value2": "[Click Here](https://docs.google.com/document/d/1SNPR_OBwDBSzGvrnI5VxH4Tq8LVsMzjFKb3LRhgMSpU/edit?usp=sharing)", # edit link
          "thumbnail_image_url": "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMG1xaWpvbTZpMXkxZTYxeGl4eXIzbnBheG5hczMyeDFoNDNtMnFpZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uDy10GO1sYTKTGcJrT/giphy.gif",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          "poonly": "poonly",  # add for po, use None if not needed
          "poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Built-in Tweaks] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

  ##################################################################################
  ############### CLEAN DREAM ##########################################
  ##################################################################################
      "cleandreampo": {
          "title": "Clean Dream Tweak",  # edit value
          "description": "Removes a lot of buildings and plants for a better visibility of the map.",
          "param1": "Author(s):",
          "value1": "Unknown",  # edit author
          "submit": "submit",
          "submitdesc": "submitdesc",
          "param2": "More Information",
        "value2": "[Click Here](https://luisarlzproductions.com/tweaks/files/dream-tweak-po.rar)", # edit link
          "thumbnail_image_url": "https://i.imgur.com/akMfpyC.png",  # edit image big
          #"pkoonly": "pkoonly",  # add for pko, use None if not needed
          #"pkoonlydesc": "pkoonlydesc",  # add for pko, use None if not needed
          "poonly": "poonly",  # add for po, use None if not needed
          "poonlydesc": "poonlydesc",  # add for po, use None if not needed
          "authorname": "[Visual Tweak] For Everyone",
          #"footer_text": " ",  # Add your custom footer here
      },

}

for command_name, command_info in commands_info.items():
    title = command_info.get("title", None)
    description = command_info.get("description", "No description available")
    param1 = command_info.get("param1", "Default Param1")
    value1 = command_info.get("value1", "Default Value1")
    param2 = command_info.get("param2", "Default Param2")
    value2 = command_info.get("value2", "Default Value2")
    submit = command_info.get("submit", None)
    submitdesc = command_info.get("submitdesc", None)
    download_urls = command_info.get("download_urls", [])
    thumbnail_url = command_info.get("thumbnail_url", "https://example.com/default-thumbnail.jpg")
    thumbnail_image_url = command_info.get("thumbnail_image_url", "https://example.com/default-thumbnail.jpg")
    author_icon_url = command_info.get("author_icon_url", "https://i.imgur.com/gIYPkEs.png")
    authorname = command_info.get("authorname", "Default Author")
    preview_caption = command_info.get("preview_caption", "Preview not available")
    pkoonly = command_info.get("pkoonly", None)
    pkoonlydesc = command_info.get("pkoonlydesc", None)
    poonly = command_info.get("poonly", None)
    poonlydesc = command_info.get("poonlydesc", None)
    footer_text = command_info.get("footer_text", None)

    create_generic_command(command_name, title, description, param1, value1, param2, value2, submit, submitdesc, download_urls, thumbnail_url, thumbnail_image_url, author_icon_url, authorname, pkoonly, pkoonlydesc, poonly, poonlydesc,footer_text)

@client.command()
async def guides(ctx):
    guides = discord.Embed(
        title="Guides Index",
        url=
        "https://luisarlzproductions.com/guides/guides-main.html",
        description=
        "Enjoy a Guides Index made with guides I've collected around the years!",
        color=0x35DEA8)
    guides.set_author(name="Guides by LuisaRLZ",
                         url="https://luisarlzproductions.com/guides/guides-main.html",
                         icon_url="https://i.imgur.com/gIYPkEs.png")
    guides.set_thumbnail(url="https://i.imgur.com/QzGwyD9.png")
    guides.add_field(
        name="Link:",
        value=
        "https://luisarlzproductions.com/guides/guides-main.html",
        inline=False)
    guides.set_footer(
        text=
        "If you've got any guide you'd like to add, please message me @luisarlz"
    )
    await ctx.send(embed=guides)

@client.command()
async def bots(ctx):
    bots = discord.Embed(
        title="Useful Bots for Guilds by LuisaRLZ",
        url=
"https://docs.google.com/document/d/1tP7GZiIsLEsTiMTSppM6CwLzo8x8iiHiSl9ikStR3w4/edit?usp=sharing",
        description=
        "Enjoy a Guide I made with all discord bots your guild may find useful! Make sure to also check out my `+extras` command for some extra goodies for your guild!",
        color=0x35DEA8)
    bots.set_author(name="Bots for Guilds",
                         url="https://docs.google.com/document/d/1tP7GZiIsLEsTiMTSppM6CwLzo8x8iiHiSl9ikStR3w4/edit?usp=sharing",
                         icon_url="https://i.imgur.com/gIYPkEs.png")
    bots.set_thumbnail(url="https://i.imgur.com/QzGwyD9.png")
    bots.add_field(
        name="Link:",
        value=
        "[Click Here](https://docs.google.com/document/d/1tP7GZiIsLEsTiMTSppM6CwLzo8x8iiHiSl9ikStR3w4/edit?usp=sharing)",
        inline=False)
    bots.set_footer(
        text=
        "If you've got any bot you'd like to add, please message me @luisarlz"
    )
    await ctx.send(embed=bots)

@client.command(name='tweaksindex', aliases=['index'])
async def tweaksindex(ctx):
  tweaksindex = discord.Embed(
        title="2018 Tweaks Index",
        url=
"https://docs.google.com/document/d/1HVUNe9QJYjK3Y7ZsFPkMOLa908uN-dhQXhOshI84-LQ/edit?usp=sharing",
        description=
        "Visit the classic Tweaks Index I made back in 2018",
        color=0x35DEA8)
  tweaksindex.set_author(name="Classic Tweaks Index",
                         url="https://docs.google.com/document/d/1HVUNe9QJYjK3Y7ZsFPkMOLa908uN-dhQXhOshI84-LQ/edit?usp=sharing",
                         icon_url="https://i.imgur.com/gIYPkEs.png")
  tweaksindex.set_thumbnail(url="https://i.imgur.com/QzGwyD9.png")
  tweaksindex.add_field(
        name="Links:",
        value=
        "[ToP2](https://docs.google.com/document/d/1QG1dZvDBBu9snrU5i5wPua11vycqBAuk5UGQfwgdVDc/edit?usp=sharing) | [Private Servers](https://docs.google.com/document/d/1HVUNe9QJYjK3Y7ZsFPkMOLa908uN-dhQXhOshI84-LQ/edit?usp=sharing) | [PKO](https://docs.google.com/document/d/1BUdTKe4OpK1SJtbmVXkcgrc2q38zRsWp-kAXru2KMkY/edit?usp=sharing) | [PO](https://docs.google.com/document/d/1TvZC4bhYh9fcytD2KCVXqsRzWIVvoo3NQ2cnp5kZF8w/edit?usp=sharing) | [ROSO](https://docs.google.com/document/d/1YsR40yepHaB3orBsdnRlvjCy1PeVMsfKr5FJUYN2XK0/edit?usp=sharing) | ",
        inline=False)
  tweaksindex.set_footer(
        text=
        "If you've got any tweaks you'd like to add, please message me @luisarlz"
    )
  await ctx.send(embed=tweaksindex)

@client.command(name='rosotweaks', aliases=['tweaksroso'])
async def rosotweaks(ctx):
    rosotweaks = discord.Embed(
        title="ROSO Tweaks Index",
        url=
"https://docs.google.com/document/d/1YsR40yepHaB3orBsdnRlvjCy1PeVMsfKr5FJUYN2XK0/edit?usp=sharing",
        description=
        "2018 Guide to tweaking your ROSO Client + some manual tweaks",
        color=0x35DEA8)
    rosotweaks.set_author(name="ROSO Tweaks",
                         url="https://docs.google.com/document/d/1YsR40yepHaB3orBsdnRlvjCy1PeVMsfKr5FJUYN2XK0/edit?usp=sharing",
                         icon_url="https://i.imgur.com/gIYPkEs.png")
    rosotweaks.set_thumbnail(url="https://i.imgur.com/QzGwyD9.png")
    rosotweaks.add_field(
        name="Link:",
        value=
        "[Click Here](https://docs.google.com/document/d/1YsR40yepHaB3orBsdnRlvjCy1PeVMsfKr5FJUYN2XK0/edit?usp=sharing)",
        inline=False)
    rosotweaks.set_footer(
        text=
        "If you've got any tweak you'd like to add, please message me @luisarlz"
    )
    await ctx.send(embed=rosotweaks)

@client.command()
async def extras(ctx):
    extras = discord.Embed(
        title="Extra Material for Guilds by LuisaRLZ",
        url=
"https://docs.google.com/document/d/1DnGRLUJOHvqu95egD2u3PO6vSY50V9HsaitV8Ah1Veo/edit?usp=sharing",
        description=
        "Enjoy a couple systems and goodies I've made for all guilds to use! Also check out my `+bots` command for some cool bots for your guild!",
        color=0x35DEA8)
    extras.set_author(name="Extras for Guilds",
                         url="https://docs.google.com/document/d/1DnGRLUJOHvqu95egD2u3PO6vSY50V9HsaitV8Ah1Veo/edit?usp=sharing",
                         icon_url="https://i.imgur.com/gIYPkEs.png")
    extras.set_thumbnail(url="https://i.imgur.com/QzGwyD9.png")
    extras.add_field(
        name="Materials",
        value=
        "[AP/GP System (Click Here)](https://docs.google.com/document/d/1DnGRLUJOHvqu95egD2u3PO6vSY50V9HsaitV8Ah1Veo/edit?usp=sharing)",
        inline=False)
    extras.set_footer(
        text=
        "If you've got any material you'd like to add, please message me @luisarlz"
    )
    await ctx.send(embed=extras)

@client.command(name='invite', aliases=['inviteme','invitebot'])
async def invite(ctx):
    invite = discord.Embed(
        title="Invite Me!",
        url=
"https://discord.com/api/oauth2/authorize?client_id=957567616589901824&permissions=8&scope=applications.commands%20bot",
        description=
        "Invite this bot to your Discord Server! You must have inviting permissions. Use `+helper` to check out my commands. Also, Invite more useful Bots by [Clicking Here](https://docs.google.com/document/d/1tP7GZiIsLEsTiMTSppM6CwLzo8x8iiHiSl9ikStR3w4/edit?usp=sharing).",
        color=0x0DF6EB)
    invite.set_author(name="Invite this Bot",
                         url="https://discord.com/api/oauth2/authorize?client_id=957567616589901824&permissions=8&scope=applications.commands%20bot",
                         icon_url="https://i.imgur.com/xJv1N42.png")
    invite.set_thumbnail(url="https://i.imgur.com/xJv1N42.png")
    invite.add_field(
        name="Invite Link:",
        value=
        "[Click Here](https://discord.com/api/oauth2/authorize?client_id=957567616589901824&permissions=8&scope=applications.commands%20bot)",
        inline=False)
    invite.set_footer(
        text=
        "If you've got any doubt or suggestion on this bot, please message me @luisarlz"
    )
    await ctx.send(embed=invite)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("**Command not Found. Please use** `+helper` **to check out my commands!** \n(*This message will be deleted in 5 seconds*)", delete_after=5.0)

try:
   keep_alive()
   client.run(os.environ['TOKEN'])
except Exception:
  os.system('kill 1')

#####client.run(TOKEN)