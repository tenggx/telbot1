import asyncio
import json

import telegram


async def send_message_async(bot_token, chat_id, text):
    bot = telegram.Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=text, parse_mode='html')


if __name__ == '__main__':
    chat_id = "-1001870599224"

    token = '6221601248:AAEoCC-VGrNi4EiIWpqawBiL0aaSlu92bUQ'
    text = "test111"
    datas = {"msgtype": "text", "text": {"content": "test111sss"}, "at": {"isAtAll": True}}
    textMsg = json.dumps(datas, ensure_ascii=False)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_message_async(token, chat_id, textMsg))
