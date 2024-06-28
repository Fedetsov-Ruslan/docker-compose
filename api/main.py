import os
import asyncio
from fastapi import FastAPI
from aiogram import types, Dispatcher, Bot
from pydantic import BaseModel
from bot.app import process_message_from_user


from dotenv import load_dotenv

load_dotenv()
TG_TOKEN = os.getenv('TOKEN')

class Message(BaseModel):
    message: str

bot = Bot(token=TG_TOKEN)

app = FastAPI()
    
@app.get("/test")
async def test():
    return {"message": "ok"}

@app.post("/test")
async def test_post(message: Message):
    print(message.message)
    asyncio.create_task(process_message_from_user( message_text=message.message, chat_id=bot.id))
    return message


