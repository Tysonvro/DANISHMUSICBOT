from config import ASSISTANT_PREFIX
from Yukki import BOT_NAME, BOT_USERNAME
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = f"""
ð·ðð¢ MENTION !
ð  I Aá´ Dá´É´ÉªsÊ Má´sÉªá´ Bá´á´, A Aá´¡á´sá´á´á´ Má´sÉªá´ Bá´á´ WÉªá´Ê Lá´á´s OÒ  Fá´á´á´á´Êá´s
ââââââââââââââââââââ

âª Bá´á´ Fá´Ê PÊá´ÊÉªÉ´É¢ Má´sÉªá´ IÉ´ Yá´á´Ê GÊá´á´á´ Vá´ IÉ´ Bá´á´Ê Aá´á´Éªá´ AÉ´á´ VÉªá´á´á´ Fá´Êá´á´á´..ðâ¤ï¸

â¼ Sá´ WÊá´á´ Yá´á´ AÊá´ Wá´Éªá´ÉªÉ´É¢ Tá´ Aá´á´ Má´ IÉ´ Yá´á´Ê GÊá´á´á´ Bá´ÊÊ..ð

á´É´á´ á´á´É´'á´ ê°á´ÊÉ¢á´á´ á´á´ á´Êá´á´á´á´á´ á´á´ á´¡Éªá´Ê á´ÊÊ ÊÉªÉ¢Êá´ê±..â¡ï¸
âââââââââââââââââââ 
"""

COMMANDS_TEXT = f"""
â¨ **Hello MENTION !**

**Click on the buttons below to know my commands.**
"""

START_BUTTON_GROUP = InlineKeyboardMarkup(
    [   
        [
            InlineKeyboardButton(
                text="ð Commands", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="ð§ Settings", callback_data="settingm"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="â¡ï¸ð¼ð¢ ð¾ð ðððâ¡ï¸", url="https://t.me/DANISH_BABA"
            ),
            InlineKeyboardButton(
                text="â¨ ððððððð ð¶ðððð â¨", url="https://t.me/WEFRIENDSCIRCLE"
            ),                       
        ],        
    ]
)

START_BUTTON_PRIVATE = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="â Add me to Group â", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            ),            
        ],
        [   
            InlineKeyboardButton(
                text="ð Commands", callback_data="command_menu"
            ),                       
        ],
        [
            InlineKeyboardButton(
                text="â¡ï¸ð¼ð¢ ð¾ð ðððâ¡ï¸", url="https://t.me/DANISH_BABA"
            ),
            InlineKeyboardButton(
                text="â¨ ððððððð ð¶ðððð â¨", url="https://t.me/WEFRIENDSCIRCLE"
            ),                       
        ],        
    ]
)

COMMANDS_BUTTON_USER = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="Admin Commands", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="Bot Commands", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="Play Commands", callback_data="play_cmd"
            ),            
            InlineKeyboardButton(
                text="Extra Commands", callback_data="extra_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="âªï¸ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="ð Close", callback_data="close_btn"
            ),            
        ],                
    ]
)

COMMANDS_BUTTON_SUDO = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="Admin Commands", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="Bot Commands", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="Play Commands", callback_data="play_cmd"
            ),
            InlineKeyboardButton(
                text="Sudo Commands", callback_data="sudo_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="Extra Commands", callback_data="extra_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="âªï¸ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="ð Close", callback_data="close_btn"
            ),            
        ],                
    ]
)

BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="âªï¸ Back", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="ð Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

SUDO_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="More Sudo Commands", url="http://telegra.ph/ðððððð-ððððð-ððð-02-18"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="âªï¸ Back", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="ð Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)


ADMIN_TEXT = f"""
Here is the help for **Admin Commands:**


--**ADMIN ONLY COMMANDS WITH MANAGE VC RIGHT:**--

/pause 
- Pause the playing music on voice chat.

/resume
- Resume the paused music on voice chat.

/skip
- Skip the current playing music on voice chat

/end or /stop
- Stop the playout.


--**Authorised Users List:**--

**{BOT_NAME} has a additional feature for non-admin users who want to use admin commands**
- Auth users can skip, pause, stop, resume Voice Chats even without Admin Rights.


/auth [Username or Reply to a Message] 
- Add a user to AUTH LIST of the group.

/unauth [Username or Reply to a Message] 
- Remove a user from AUTH LIST of the group.

/authusers 
- Check AUTH LIST of the group.
"""

BOT_TEXT = """
Here is the help for **Bot Commands:**


/start 
- Start the Music Bot.

/help 
- Get Commands Helper Menu with detailed explanations of commands.

/settings 
- Get Settings dashboard of a group. You can manage Auth Users Mode. Commands Mode from here.

/ping
- Ping the Bot and check Ram, Cpu etc stats of Music Bot."""

PLAY_TEXT = """
Here is the help for **Play Commands:**


--**Youtube and Telegram Files:**--

/play __[Music Name]__(Bot will search on Youtube)
/play __[Youtube Track link or Playlist]__
/play __[Video, Live, M3U8 Links]__
/play __[Reply to a Audio or Video File]__
- Stream Video or Music on Voice Chat by selecting inline Buttons you get


--**Playlists:**--

/playplaylist 
- Start playing Your Saved Playlist.

/playlist 
- Check Your Saved Playlist On Servers.

/delmyplaylist
- Delete any saved music in your playlist

/delgroupplaylist
- Delete any saved music in your group's playlist [Requires Admin Rights.]
"""

SUDO_TEXT = f"""
Here is the help for **Sudo Commands:**

**<u>ADD & REMOVE SUDO USERS :</u>**
/addsudo [Username or Reply to a user]
/delsudo [Username or Reply to a user]

**<u>BOT COMMANDS:</u>**
/restart - Restart Bot. 
/update - Update Bot.
/stats - Check Bots Stats

**<u>BLACKLIST CHAT FUNCTION:</u>**
/blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
/whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot

**<u>BROADCAST FUNCTION:</u>**
/broadcast [Message or Reply to a Message] - Broadcast message.
/broadcast_pin [Message or Reply to a Message] - Broadcast message with pin [Disabled Notifications].
/broadcast_pin_loud [Message or Reply to a Message] - Broadcast message with pin [Enabled Notifications].

**<u>GBAN FUNCTION:</u>**
/gban [Username or Reply to a user] - Ban a user globally in Bot's Served Chats and prevents user from using bot commands.
/ungban [Username or Reply to a user] - Remove a user from Bot's GBan List.
"""

EXTRA_TEXT = """
Here is the help for **Extra Commands:**


/lyrics [Music Name]
- Searches Lyrics for the particular Music on web.

/sudolist 
- Check Sudo Users of Music Bot

/song [Track Name] or [YT Link]
- Download any track from youtube in mp3 or mp4 formats via Bot.

/queue
- Check Queue List of Music.
"""

BASIC_TEXT = """
ð  **Basic Commands:**

/start - start the bot
/help - get help message
/play - play songs or videos in vc
/mplay - play songs directly in vc
/vplay - play videos directly in vc
/spotify - play songs from spotify
/resso - play songs from resso
/lyrics - get lyrics of song
/ping - ping the bot
/playlist - play your playlist
/song - download a song as music or video
/settings - settings of the group
/theme - set theme for your group
/queue - get queued song
"""

BASIC_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="âªï¸ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="ð Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

COMMAND_MENU_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="ð Basic Commands", callback_data="basic_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="ð Advanced Commands", callback_data="advanced_cmd"
            ),
        ],
        [
            InlineKeyboardButton(
                text="âªï¸ Back", callback_data="open_start_menu"
            ),
            InlineKeyboardButton(
                text="ð Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)
