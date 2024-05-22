from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, OneLineListItem

class DemoApp(MDApp):
    def build(self):
        screen = Screen()

        scroll_view = ScrollView()
        list_view = MDList()
        scroll_view.add_widget(list_view)

        for i in range(20):
            item = OneLineListItem(text=f"Item {i+1}")
            list_view.add_widget(item)

        screen.add_widget(scroll_view)
        return screen
DemoApp().run()
