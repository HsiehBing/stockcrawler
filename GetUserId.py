from linebot import LineBotApi

def GETUserId(event):
    UserId = event.source.user_id
    profile = line_bot_api.get_profile(UserId)
    return profile