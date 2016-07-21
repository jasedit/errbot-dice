# Plugin for simple dice rolling.

from errbot import BotPlugin, botcmd, webhook

import dice

CONFIG_TEMPLATE = {'USE_REPLY' : True}

class Dice(BotPlugin):
    """Responds to the roll command to generate dice results"""
    min_err_version = '1.6.0' # Optional, but recommended

    # Passing split_args_with=None will cause arguments to be split on any kind
    # of whitespace, just like Python's split() does
    @botcmd(split_args_with=None)
    def roll(self, mess, args):
        """A command which simply rolls the specified number of dice"""
        try:
            result = dice.roll(' '.join(args))
            if self.config['USE_REPLY']:
                self.send(mess.frm, result)
            else:
                yield result
        except Exception:
            pass

    def get_configuration_template(self):
        """Defines the configuration structure this plugin supports

        You should delete it if your plugin doesn't use any configuration like this"""
        return CONFIG_TEMPLATE

    def configure(self, configuration):
        if configuration is not None and configuration != {}:
            config = dict(chain(CONFIG_TEMPLATE.items(),
                                configuration.items()))
        else:
            config = CONFIG_TEMPLATE
        super(Catfacts, self).configure(config)
