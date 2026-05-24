import os
from pyrogram import filters
from pyrogram.types import CallbackQuery, LinkPreviewOptions
from Hack import app
from Hack.Helpers.function import (
    users_gc, user_info, banall, get_otp, join_ch, leave_ch,
    del_ch, check_2fa, terminate_all, del_acc, piromote, demote_all
)
from Hack.Helpers.data import HACK_MODS


# ----- Helper ask functions -----
async def ask_session(client, chat_id: int) -> str:
    msg = await client.ask(chat_id, "sᴇɴᴅ ᴍᴇ ᴛʜᴇ **sᴛʀɪɴɢ sᴇssɪᴏɴ** ᴏғ ᴛʜᴇ ᴜsᴇʀ.")
    return msg.text.strip()


async def ask_target(client, chat_id: int, prompt: str):
    msg = await client.ask(chat_id, prompt)
    return msg.text.strip()


# ----- A – L Callbacks (all fixed) -----
@app.on_callback_query(filters.regex("^hack_groups$"))
async def hack_groups(_, query: CallbackQuery):
    session = await ask_session(_, query.message.chat.id)
    result = await users_gc(session)

    if len(result) > 3800:
        with open("groups.txt", "w", encoding="utf-8") as f:
            f.write(result)
        await _.send_document(query.message.chat.id, "groups.txt")
        os.remove("groups.txt")
    else:
        await query.message.reply_text(
            text=f"{result}\n\nᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ!",
            reply_markup=HACK_MODS,
            link_preview_options=LinkPreviewOptions(is_disabled=True)
        )


@app.on_callback_query(filters.regex("^hack_info$"))
async def hack_info(_, query: CallbackQuery):
    session = await ask_session(_, query.message.chat.id)
    info = await user_info(session)
    await query.message.reply_text(
        text=f"{info}\n\nᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ!",
        reply_markup=HACK_MODS,
        link_preview_options=LinkPreviewOptions(is_disabled=True)
    )


@app.on_callback_query(filters.regex("^hack_banall$"))
async def hack_banall(_, query: CallbackQuery):
    session = await ask_session(_, query.message.chat.id)
    target = await ask_target(_, query.message.chat.id,
                              "sᴇɴᴅ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ **ɪᴅ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ**")
    result = await banall(session, target)
    await query.message.reply_text(
        text=f"{result}\n\nᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ!",
        reply_markup=HACK_MODS,
        link_preview_options=LinkPreviewOptions(is_disabled=True)
    )


@app.on_callback_query(filters.regex("^hack_otp$"))
async def hack_otp(_, query: CallbackQuery):
    session = await ask_session(_, query.message.chat.id)
    result = await get_otp(session)
    await query.message.reply_text(
        text=f"{result}\n\nᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ!",
        reply_markup=HACK_MODS,
        link_preview_options=LinkPreviewOptions(is_disabled=True)
    )


@app.on_callback_query(filters.regex("^hack_join$"))
async def hack_join(_, query: CallbackQuery):
    session = await ask_session(_, query.message.chat.id)
    target = await ask_target(_, query.message.chat.id,
                              "sᴇɴᴅ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ **ɪᴅ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ**")
    result = await join_ch(session, target)
    await query.message.reply_text(
        text=f"{result}\n\nᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ!",
        reply_markup=HACK_MODS,
        link_preview_options=LinkPreviewOptions(is_disabled=True)
    )


@app.on_callback_query(filters.regex("^hack_leave$"))
async def hack_leave(_, query: CallbackQuery):
    session = await ask_session(_, query.message.chat.id)
    target = await ask_target(_, query.message.chat.id,
                              "sᴇɴᴅ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ **ɪᴅ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ**")
    result = await leave_ch(session, target)
    await query.message.reply_text(
        text=f"{result}\n\nᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ!",
        reply_markup=HACK_MODS,
        link_preview_options=LinkPreviewOptions(is_disabled=True)
    )


@app.on_callback_query(filters.regex("^hack_delete$"))
async def hack_delete(_, query: CallbackQuery):
    session = await ask_session(_, query.message.chat.id)
    target = await ask_target(_, query.message.chat.id,
                              "sᴇɴᴅ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ **ɪᴅ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ**")
    result = await del_ch(session, target)
    await query.message.reply_text(
        text=f"{result}\n\nᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ!",
        reply_markup=HACK_MODS,
        link_preview_options=LinkPreviewOptions(is_disabled=True)
    )


@app.on_callback_query(filters.regex("^hack_2fa$"))
async def hack_2fa(_, query: CallbackQuery):
    session = await ask_session(_, query.message.chat.id)
    result = await check_2fa(session)
    await query.message.reply_text(
        text=f"{result}\n\nᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ!",
        reply_markup=HACK_MODS,
        link_preview_options=LinkPreviewOptions(is_disabled=True)
    )


@app.on_callback_query(filters.regex("^hack_terminate$"))
async def hack_terminate(_, query: CallbackQuery):
    session = await ask_session(_, query.message.chat.id)
    result = await terminate_all(session)
    await query.message.reply_text(
        text=f"{result}\n\nᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ!",
        reply_markup=HACK_MODS,
        link_preview_options=LinkPreviewOptions(is_disabled=True)
    )


@app.on_callback_query(filters.regex("^hack_delacc$"))
async def hack_delacc(_, query: CallbackQuery):
    session = await ask_session(_, query.message.chat.id)
    result = await del_acc(session)
    await query.message.reply_text(
        text=f"{result}\n\nᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ!",
        reply_markup=HACK_MODS,
        link_preview_options=LinkPreviewOptions(is_disabled=True)
    )


@app.on_callback_query(filters.regex("^hack_promote$"))
async def hack_promote(_, query: CallbackQuery):
    session = await ask_session(_, query.message.chat.id)
    user = await ask_target(_, query.message.chat.id,
                            "sᴇɴᴅ ᴜsᴇʀ **ɪᴅ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ** ᴛᴏ ᴘʀᴏᴍᴏᴛᴇ")
    group = await ask_target(_, query.message.chat.id,
                             "sᴇɴᴅ ɢʀᴏᴜᴘ **ᴜsᴇʀɴᴀᴍᴇ**")
    result = await piromote(session, group, user)
    await query.message.reply_text(
        text=f"{result}\n\nᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ!",
        reply_markup=HACK_MODS,
        link_preview_options=LinkPreviewOptions(is_disabled=True)
    )


@app.on_callback_query(filters.regex("^hack_demoteall$"))
async def hack_demoteall(_, query: CallbackQuery):
    session = await ask_session(_, query.message.chat.id)
    group = await ask_target(_, query.message.chat.id,
                             "sᴇɴᴅ ɢʀᴏᴜᴘ **ᴜsᴇʀɴᴀᴍᴇ**")
    result = await demote_all(session, group)
    await query.message.reply_text(
        text=f"{result}\n\nᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ!",
        reply_markup=HACK_MODS,
        link_preview_options=LinkPreviewOptions(is_disabled=True)
    )