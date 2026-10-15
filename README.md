# Discord Notifying Bot
This is a discord bot made by me to remind people to study at the desired time in our discord server.

_(for privacy reasons, I changed the channel and role Ids)_

This is a simple discord bot made using python that pings roles in a selected channel at the selected time. 
This is useful for reminding about studying or any work.

## setup process:
  - **Pre-setup:**
      1) make a discord bot from [discord developer portal](https://discord.com/developers/applications).
      2) give it the following permissions and add it to your server -> **i.**  view channel **ii.** send message
      3) create/select a channel where the reminder message will be sent
      4) create roles to be pinged and give that roles to the members

  - **setting up the program:**
      1) download the zip and extract it to get the folder with the files
      2) create a file and name it ".env" then inside it write `DISCORD_TOKEN=[your bot token]`
      3) change the bot.py according to your preference. follow the comments for better understanding of the code
      4) open up terminal in that folder location and run - `pip install -r requirements.txt`  to install the required packages.
      5) then run the bot.py
   
[N.B:- the bot will only run when the program "bot.py" is running]


![GitHub language count](https://img.shields.io/github/languages/count/SaadHM741/Reminding-bot)
