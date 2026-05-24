import asyncio
import importlib
import sys
from typing import List

from pyrogram import idle
from Hack import app, LOG, logger
from Hack.modules import ALL_MODULES


async def load_modules(modules: List[str]) -> None:
    failed = []
    for module in modules:
        try:
            importlib.import_module(f"Hack.modules.{module}")
            logger.debug(f"Loaded: {module}")
        except Exception as e:
            failed.append(module)
            logger.error(f"Failed to load '{module}': {e}")

    if failed:
        LOG.print(f"[bold red]Failed modules: {', '.join(failed)}[/]")
    else:
        LOG.print(f"[bold green]All {len(modules)} modules loaded![/]")


async def start_bot() -> None:
    try:
        await app.start()
        LOG.print("[bold cyan]Bot client started.[/]")

        await load_modules(ALL_MODULES)
        LOG.print("[bold yellow]sᴇssɪᴏɴ ᴄᴏɴᴛʀᴏʟᴇʀ ʙᴏᴛ ʜᴀs ʙᴇᴇɴ sᴛᴀʀᴛᴇᴅ[/]")

        await idle()

    except KeyboardInterrupt:
        LOG.print("\n[bold yellow]Shutdown by user (Ctrl+C).[/]")
    except Exception as e:
        logger.critical("Bot crashed!", exc_info=e)
        LOG.print(f"[bold red]Crash: {e}[/]")
        sys.exit(1)
    finally:
        await app.stop()
        LOG.print("[bold red]ᴄᴀɴᴄᴇʟʟᴇᴅ ᴀʟʟ ᴛᴀsᴋ[/]")
        logger.info("Bot stopped.")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start_bot())
    except (KeyboardInterrupt, SystemExit):
        LOG.print("[bold yellow]Bot terminated by user.[/]")
    except Exception as e:
        logger.critical("Startup failed!", exc_info=e)
        sys.exit(1)