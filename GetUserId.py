from linebot import LineBotApi

def GETUserId(event):
    UserId = str(event.source.user_id)
    # profile = line_bot_api.get_profile(UserId)
    return UserId