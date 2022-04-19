"""
Script by CLOTI (Xsarz)
Github : https://github.com/xXxCLOTIxXx
"""


TOKEN = 'Токен бота'
import discord
class MainClass(discord.Client):
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))

	async def on_message(self, message):
		channel = message.channel 							#--------------Имя канала, в котором написали сообщение
		user_name = str('{0.author}'.format(message)) 			#--------------------имя человека, который написал сообщение
		user_Id = message.author.mention 					#---------------------айди человека, который написал сообщение
		ct = '{0.content}'.format(message) 				#------------------------Сообщение пользователя
		content = str(ct).split(" ") 							#----------------------------------Сообщение пользователя, разбитое по словам в список
		channel_id =  [message.channel.mention] 							#-------------------айди канала, в котором былонаписано сообщение
		print(f"\nКанал: {channel}\n{str(user_name)}: {ct}\n")
		if content[0][0].lower() == "/":
			if content[0][1:].lower() == "ping":
				await channel.send('Pong!')




bot = MainClass()
bot.run(TOKEN)