from aiogram.dispatcher.filters.builtin import Command


class CommandStop(Command):
    """
    This filter based on :obj:`Command` filter but can handle only ``/stop`` command.
    """

    def __init__(self):
        super().__init__(['stop'])

