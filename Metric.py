import time
import os
import discord
import nltk
from discord.ext import commands

class Metric:
    def __init__(self):
        self.chatLog = []
    
    def responseTime(self):
        return time.time()
        
    async def writeLogs(self, ctx):
        chatLog = []
        async for message in ctx.channel.history(limit=1000):
        	author = str(message.author)
        	content = str(message.content)
        	created_at = str(message.created_at)
        	entry = [author, content, created_at]
        	chatLog.append(entry)
        return chatLog

        
    def saveLogs(self, userLog, filename):
        with open(filename, 'w') as f:
        	for entry in reversed(userLog):
        		f.write(str(entry) + '\n')