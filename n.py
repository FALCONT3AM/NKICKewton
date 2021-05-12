from telethon import TelegramClient, events, sync
api_id = 4133514
api_hash = '021b4d17355c929415ec36b1e51bb5b4'
client = TelegramClient('Newton', api_id, api_hash)
client.start()
@client.on(events.NewMessage(pattern=''))
async def handler(event):
    users = await client.get_participants(event.peer_id.channel_id)
    print(users[0].first_name)
    for user in users:
        if user.id:
            permissions = await client.get_permissions(event.peer_id.channel_id, user.id)
            if permissions.is_admin:
                print(str(user.id)+' ==> IS ADMIN')
            else:
                print(str(user.id)+' ==> KICK')
                await client.kick_participant(event.peer_id.channel_id, user.id)
client.run_until_disconnected()
