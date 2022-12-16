import tkinter as tk
from PIL import Image, ImageTk

class HangmanWindow:
    _buttons    = []
    _labels     = []
    _window     = None
    _icon       = None
    _gallows    = None
    _word       = ''
    _word_label = None
    _hangman_handler = None
    
    _title          = 'hangman'
    _icon_name      = 'icon.png'
    _num_of_liters  = 3
    _alphabet       = []
    
    _label_names = ['Твій рекорд', 'Набрані бали', '0', '0']
    
    def __init__(self, hangman):
        self._window     = tk.Tk()
        self._icon       = tk.PhotoImage(file=str(self._icon_name))
        self._window.title(self._title)
        self._window.iconphoto(False, self._icon)
        self._window.config(bg='#DFDFDF')
        self._window.geometry("445x325+0+0")
        self._window.resizable(False, False)
        self._alphabet = list(str('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя').upper())

        self._hangman_handler = hangman

        self.createButtonsGrid()
        self.createScoreGrid()
        self.createGallowsGrid()

        
    def createButtonsGrid(self):
        for item in range(0,len(self._alphabet)):
            self._buttons.append(tk.Button(self._window, text=self._alphabet[item],
                                        bg='#FFFFFF',
                                        fg='#000000',
                                        font=('Arial', 10, 'bold'),
                                        width=2,
                                        height=2,
                                        bd=0,
                                        command=lambda arg1=item: self._hangman_handler.play(arg1, self)
                                        ))

        item = 0
        for x in range(0, 9):
            for y in range(0, 5):
                if(item <= 32):
                    if(item >= 30):
                        y+=1
                        self._buttons[item].grid(row=x, column=y)
                    else:
                        self._buttons[item].grid(row=x, column=y)
                    item+=1
                else: break

    def createScoreGrid(self):
        for item in range(0,len(self._label_names)):
            self._labels.append(tk.Label(self._window, text=self._label_names[item],
                                           bg='#FFFFFF',
                                           fg='#000000',
                                           font=('Arial', 10, 'bold'),
                                           width=20,
                                           height=1
                                           ))
        item = 0
        for x in range(9, 11):
            for y in range(5, 7):
                if(item <= 32):
                    self._labels[item].grid(row=x, column=y)
                    item+=1
                else: break

    def createGallowsGrid(self):

        image1 = Image.open("1.png")
        test = ImageTk.PhotoImage(image1)

        self._gallows       = tk.Label(image=test, width=225, height=225, bg='#FFFFFF')
        self._gallows.image = test

        self._word_label    = tk.Label(self._window, text=self._hangman_handler.setNewWordMaskByWindow(),
                                           bg='#DFDFDF',
                                           fg='#000000',
                                           font=('Arial', 10, 'bold'),
                                           width=35,
                                           height=1
                                           )
        self._old_word_label = tk.Label(self._window, text='',
                                           bg='#DFDFDF',
                                           fg='#000000',
                                           font=('Arial', 10, 'bold'),
                                           width=35,
                                           height=1
                                           )
        self._help_button = tk.Button(self._window, text='Підказка',
                                        bg='#FFFF66',
                                        fg='#000000',
                                        font=('Arial', 8, 'bold'),
                                        width=9,
                                        height=1,
                                        bd=0,
                                        command=lambda arg1='help': self._hangman_handler.play(arg1, self))
        
        self._gallows.place(x=170, y=23)
        self._word_label.place(x=140, y=0)
        self._help_button.place(x=375, y=0)
        self._old_word_label.place(x=140, y=250)

    def updateButton(self, item, color, state):
        _index = self._alphabet.index(item)
        self._buttons[_index]['bg'] = color
        self._buttons[_index]['state'] = state
    def updatePoints(self, points):
        self._labels[3]['text'] = str(points)
    def updateStrike(self, strike):
        self._labels[2]['text'] = str(strike)
    def updateWord(self, word_mask, bg='#FFFFFF'):
        self._word_label['text'] = str(word_mask)
    def updateOldWord(self, word_mask, fg='#FFFFFF'):
        self._old_word_label['text'] = str(word_mask)
        self._old_word_label['fg'] = fg
    def updateImage(self, tries, bg='#FFFFFF'):
        name = str(tries)+str('.png')
        img_obj = Image.open(name)
        img_tk = ImageTk.PhotoImage(img_obj)

        self._gallows.configure(image=img_tk)
        self._gallows.image = img_tk
        
    def updateAllButtons(self):
        for item in self._buttons:
            item['bg'] = '#FFFFFF'
            item['fg'] = '#000000'
            item['state'] = 'normal'


    def getWindowHandler(self):
        self._hangman_handler._window_handler = self
        self._hangman_handler.init()
        return self._window
