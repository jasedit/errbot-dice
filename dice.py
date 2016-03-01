# Plugin for simple dice rolling.

from errbot import BotPlugin, botcmd, webhook

import dice


class Dice(BotPlugin):
    """Responds to the roll command to generate dice results"""
    min_err_version = '1.6.0' # Optional, but recommended

    # Passing split_args_with=None will cause arguments to be split on any kind
    # of whitespace, just like Python's split() does
    @botcmd(split_args_with=None)
    def roll(self, mess, args):
        """A command which simply rolls the specified number of dice"""
        try:
            yield dice.roll(' '.join(args))
        except Exception:
            pass