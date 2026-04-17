
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class CultivoEfectivoApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='CULTIVO EFECTIVO', font_size='30sp'))
        layout.add_widget(Label(text='Autor: Antonio Robles\nSoberania Alimentaria', halign='center'))
        return layout

if __name__ == "__main__":
    CultivoEfectivoApp().run()
