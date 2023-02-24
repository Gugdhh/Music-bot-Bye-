#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from YukkiMusic import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
        second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="HELP_1",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="HELP_2",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="HELP_3",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="HELP_4",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="HELP_12",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="HELP_5",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="HELP_7",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="HELP_8",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="HELP_9",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="HELP_10",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="HELP_11",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="HELP_9",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❄ ʜᴇʟᴩ ❄",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
