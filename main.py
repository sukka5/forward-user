from pyrogram import Client, filters
from pyrogram.types import Message


RUN = {"isRunning": True}
User = Client(
    name='pyrogram',
    api_hash="a0539f94d7e13d3ba3296f56a4da1f2e",
    api_id=10499076,
    in_memory=True,
    session_string="BQAYwXoLveHSkfIMQEWWXPU9MfaLIfhKWffzwNrrdWLpovzc0o9e64FZUeHHvms95TZ3iXcIkaB--Z8lxGhnZy6eRpY892H7gyYK2oj618Vab2t5J3mjvP0EKfD8SH0YZwL16sIjTc60xznjqKtOQuI8tPlR-HKgfNDEYH8CfzQgQCaeqeSqpb76jtASduwFUqau6ZsGbrmZFgL9EVOYzX7Wdy3f52mR5dFk38GZJZ4GqEK1v88pND8BvXFKiRbxUMqUlwF-b_98gT-G1UeXZbM75MWGgO50FntKXRCW6V1y-it1E3q6uINJMlLn5pMR3eCZxx1FCBrPr82lCcC_LOC7AAAAAVDG_X8A"
)

chat_id_FROM = -1001602097039
chat_id_to =-1001550672968

forward_from = [-1001832059495, -1001743088836]
forward_to = -1001550672968

@User.on_message((filters.text | filters.media))
async def main(client: Client, message: Message):
    if (message.text == "!start") and message.from_user.is_self:
        if not RUN["isRunning"]:
            RUN["isRunning"] = True
        await message.edit(
            text=f"Hi, **{(await client.get_me()).first_name}**!\nThis is a Forwarder Userbot by @MalithD",
            disable_web_page_preview=True)
    elif message.chat.id == chat_id_FROM and RUN["isRunning"]:
        await client.copy_message(
            chat_id=chat_id_to,
            from_chat_id=message.chat.id,
            message_id=message.id
        )

    # Getting groups data
    elif (message.text == "!grps") and message.from_user.is_self and RUN["isRunning"]:
        async for dialog in User.get_dialogs(5):
            await message.reply_text(
              f"**🔖 Title :{dialog.chat.title}**\n**◾️ ID: <code>{dialog.chat.id}</code>**"
            )
    # Adding group to the forward from list
    elif message.text and (message.text.startswith("!addgroup")) and message.from_user.is_self and RUN["isRunning"]:
        try:
            group = message.text.split(" ")[-1]
            forward_from.append(group)
            print(forward_from)
            await message.edit(f'**Group**: {group} Added Succesfully!')
        except Exception as err:
            await client.send_message(chat_id="me", text=f"#ERROR: `{err}`")

    # Forwarding messages 
    elif message.chat.id in forward_from and RUN["isRunning"]:
        try:
            await client.copy_message(
                chat_id=forward_to,
                from_chat_id=message.chat.id,
                message_id=message.id
            )
            print('done')
        except Exception as err:
            await client.send_message(chat_id="me", text=f"#ERROR: `{err}`")

  




print("working")
User.run()


















