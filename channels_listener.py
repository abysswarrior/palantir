from telethon import TelegramClient, events, sync
import environments as env
from message_validators import quality_channel_validator

api_id = env.API_Id
api_hash = env.API_HASH
client = TelegramClient('anon', api_id, api_hash)
palantir_channel = 'https://t.me/ravand_palantir'

@client.on(events.NewMessage(chats='https://t.me/QualitySignalsChannel'))
# @client.on(events.NewMessage(chats='me'))
async def quality_signal_channel_listener(event):

    new_message = event.message.message
    print("-------- new signal")

    final_message = quality_channel_validator(new_message)

    if final_message:

        # await client.forward_messages(entity=palantir_channel, messages=event.message)
        await client.send_message(entity=palantir_channel, message=final_message)


with client: 
    client.run_until_disconnected()
