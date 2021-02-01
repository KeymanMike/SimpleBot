from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile, MediaGroup

from loader import dp, bot


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def get_file_id(message: types.Message):
    await message.reply(message.photo[-1].file_id)
    await message.photo[-1].download()

@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def get_file_id(message: types.Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command("get_cats"))
async def send_cat(message: types.Message):
    photo_file_id = '..'
    photo_url = 'https://static.probusiness.io/720x480c/n/03/d/38097027_439276526579800_2735888197547458560_n.jpg'
    photo_bytes = InputFile(path_or_bytesio="photos/cat.jpg")
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_url,
                         caption="Вот кот /more")

@dp.message_handler(Command("more"))
async def more_cats(message: types.Message):
    album = MediaGroup()
    photo_file_id = '..'
    photo_url = 'https://static.probusiness.io/720x480c/n/03/d/38097027_439276526579800_2735888197547458560_n.jpg'
    photo_bytes = InputFile(path_or_bytesio="photos/cat.jpg")
    album.attach_photo(photo_bytes)
    album.attach_photo(photo_url)

    #await bot.send_media_group(chat_id=message.from_user.id, media=album)
    await message.answer_media_group(album)
