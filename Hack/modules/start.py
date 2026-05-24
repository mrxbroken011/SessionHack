from pyrogram import filters
from pyrogram.types import CallbackQuery, LinkPreviewOptions
from Hack import app, START_PIC
from Hack.Helpers.data import PM_TEXT, PM_BUTTON, HACK_TEXT, HACK_MODS


@app.on_message(filters.command("start") & filters.private)
async def start_command(_, message):
    user = message.from_user.mention(style="html")
    bot = (await _.get_me()).mention(style="html")
    await message.reply_photo(
        photo=START_PIC,
        caption=PM_TEXT.format(user=user, bot=bot),
        reply_markup=PM_BUTTON
    )


@app.on_message(filters.command("hack") & filters.private)
async def hack_command(_, message):
    await message.reply_text(
        text=HACK_TEXT,
        reply_markup=HACK_MODS,
        link_preview_options=LinkPreviewOptions(is_disabled=True)
    )


@app.on_callback_query(filters.regex("^show_hack_menu$"))
async def show_hack_menu(_, query: CallbackQuery):
    await query.message.delete()
    await query.message.reply_text(
        text=HACK_TEXT,
        reply_markup=HACK_MODS,
        link_preview_options=LinkPreviewOptions(is_disabled=True)
    )


@app.on_callback_query(filters.regex("^back_to_start$"))
async def back_to_start(_, query: CallbackQuery):
    user = query.from_user.mention(style="html")
    bot = (await _.get_me()).mention(style="html")
    await query.message.edit_caption(
        caption=PM_TEXT.format(user=user, bot=bot),
        reply_markup=PM_BUTTON
    )
    await query.answer("Back to home")