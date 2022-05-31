from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction


class GnomeSessionExtension(Extension):
    def __init__(self):
        super(GnomeSessionExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        options = ['airDots', 'nuove']
        my_list = event.query.split(" ")

        # uncume pro lite && move up

        items.append(Pro3Lite())
        items.append(XPro3Lite())
        items.append(airDot())
        items.append(XairDot())

        return RenderResultListAction(items)


def airDot():
    return ExtensionResultItem(icon='images/on.png',
                               name='Connetti airDot',
                               description='disconnect from phone frist',
                               on_enter=RunScriptAction("bt on air", None))


def XairDot():
    return ExtensionResultItem(icon='images/off.png',
                               name='Disconnetti airDot',
                               description='and connect to the phone',
                               on_enter=RunScriptAction("bt off air", None))


def Pro3Lite():
    return ExtensionResultItem(icon='images/on.png',
                               name='Connetti Pro 3',
                               description='disconnect from phone frist',
                               on_enter=RunScriptAction("bt on red", None))


def XPro3Lite():
    return ExtensionResultItem(icon='images/off.png',
                               name='Disconnetti Pro 3',
                               description='and connect to the phone',
                               on_enter=RunScriptAction("bt off red", None))


if __name__ == '__main__':
    GnomeSessionExtension().run()
