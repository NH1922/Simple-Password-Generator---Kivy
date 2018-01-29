#imports 

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from random import choice
from random import shuffle
from pyperclip import copy
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition

#Dictionary to store the usernames and passwords
IDS ={}

class MainScreen(Screen):
    pass
class GenerateScreen(Screen):
    pass
class screenmanage(ScreenManager):
    pass


#Class to generate the passwords
class Dis(GridLayout):
    global IDS
    length = NumericProperty()
    password = StringProperty('')
    keyword = StringProperty('')
    def generatepwd(self):
        self.password = ''
        keywd = self.ids.keywd.text

        alphas = 'ABCDEFGHIJKLMNOPQRSTUBWXYZabcdefghijklmnopqrstuvwxyz0123456789./_-'
        if (self.ids.pwdlen.text==''):
            popup = Popup(title="Incorrect Input",size=(200, 200),size_hint=(None, None),content=Label(text='Length cannot be empty ! '))
            popup.open()
        else:
            length = int(self.ids.pwdlen.text) - len(keywd)


            while(length):
               self.password=self.password + choice(alphas)
               length = length - 1
            result = list(self.password)
            result.append(keywd)
            shuffle(result)
            result = ''.join(result)
            self.password = result

#class to save the password and copy it to the clipboard using pyperclip
    def savepwd(self):
        IDS[self.ids.usrname.text] = self.password
        copy(IDS[self.ids.usrname.text])
        popup = Popup(title='Saved !', content=Label(text='Copied to clipboard'),size_hint=(None,None),size=(400,200))
        popup.open()

    def clear(self):
        self.length=0
        #self.password = ''

class someapp(App):
    pass


if __name__ == '__main__':
    someapp = someapp()
    someapp.run()