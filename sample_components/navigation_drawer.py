from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500)


navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "Navigation Drawer"
                        elevation: 5
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'

                Image:
                    source: 'me.png'
                MDLabel:
                    text: 'App'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: 'eee@ee.com'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Item1'
                        OneLineListItem:
                            text: 'Item2'
"""


class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen


DemoApp().run()
