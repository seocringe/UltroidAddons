import emoji

import addons.emojifontss as emojify


@ultroid_cmd(pattern="etxt(?: |$)(.*)")
async def itachi(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(
            event, "What am I Supposed to do with this stupid, Give me a text. "
        )
        return
    result = ""
    for a in args:
        a = a.lower()
        if a in emojify.oofman:
            char = emojify.offman[emojify.oofman.index(a)]
            result += char
        else:
            result += a
    await edit_or_reply(event, result)


@ultroid_cmd(pattern="ctxt(?: |$)(.*)")
async def naruhina(event):
    snku = event.pattern_match.group(1)
    get = await event.get_reply_message()
    args = get.text
    if not args:
        await edit_or_reply(
            event, "What am I Supposed to do with this stupid, Give me a text. "
        )
        return
    try:
        emoji, arg = args.split(" ", 1)
    except Exception:
        arg = args
        emoji = snku
    if not char_is_emoji(emoji):
        arg = args
        emoji = snku
    result = ""
    for a in arg:
        a = a.lower()
        if a in emojify.oofman:
            char = emojify.sedman[emojify.oofman.index(a)].format(cj=emoji)
            result += char
        else:
            result += a
    await edit_or_reply(event, result)


def char_is_emoji(character):
    return character in emoji.UNICODE_EMOJI["en"]
