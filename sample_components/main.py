from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from helpers import character_name_helper


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Green"
        screen = Screen()
        # character_name = MDTextField(helper_text='Character Name', helper_text_mode='persistent',
        #                              pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #                              size_hint_x=None, width=300)
        label = MDLabel(adaptive_size=True, 
                        text="Example", pos_hint={"center_x": 0.5, "center_y": 0.8})
        button_search = MDRectangleFlatButton(text="Buscar", pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                              on_release=self.show_data)
        self.character_name = Builder.load_string(character_name_helper)

        label_about = MDLabel(adaptive_size=True, 
                        text="Desenvolvido por Own4rd - Sobre", pos_hint={"center_x": 0.5, "center_y": 0.1})


        screen.add_widget(label)
        screen.add_widget(self.character_name)
        screen.add_widget(button_search)
        screen.add_widget(label_about)
        return screen

    def show_data(self, obj):
        close_button = MDFlatButton(text="Voltar", on_release=self.close_dialog)
        self.dialog = MDDialog(title="Personagem Detalhes",
                           text=self.character_name.text,
                           size_hint=(0.9, 1), 
                           buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

DemoApp().run()
