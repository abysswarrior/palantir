from telethon import TelegramClient, events, sync
import environments as env

api_id = env.API_Id
api_hash = env.API_HASH

user_input_channel = 'me'

client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats=user_input_channel)) 
async def newMessageListener(event):

    newMessage = event.message.message
    print(newMessage)

    await client.forward_messages(entity='https://t.me/ravand_palantir', messages=event.message)


with client: 
    client.run_until_disconnected() 