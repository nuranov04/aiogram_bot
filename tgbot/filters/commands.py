from aiogram.dispatcher.filters.builtin import Command


class CommandGetMyId(Command):
    """
    This filter based on :obj:`Command` filter but can handle only ``/get_my_id`` command.
    """

    def __init__(self):
        super().__init__(['get_my_id'])


class CommandMenu(Command):
    """
    This filter based on :obj:`Command` filter but can handle only ``/menu`` command.
    """

    def __init__(self):
        super().__init__(['menu'])
