# SPDX-License-Identifier: Apache-2.0

import logging

from telegram import Bot


class Module:
    name: str = "ModBase"
    disabled: bool = False

    def __init__(self) -> None:
        self.log = logging.getLogger(self.__class__.name.replace(" ", "_"))

    def register_help(self, cmd_name: str, cmd_desc: str) -> None:
        ...

    def on_load(self) -> None:
        raise NotImplementedError

    def on_stop(self) -> None:
        raise NotImplementedError
