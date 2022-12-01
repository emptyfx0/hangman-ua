import words
import random

class Hangman():
    _current_word   = ''
    _points         = 3
    _strike         = 0
    _window_handler = None
    _tries_limit    = 5
    _image_index    = 2
    _in_game        = 0

    _window_handler = None

    def init(self):
        self._window_handler.updatePoints(self._points)
        self._window_handler.updateStrike(self._strike)

    def play(self, alpha_item, window_handler):

        #   Працює якщо початок раунду
        if(self._in_game == 0):
            window_handler.updateImage(1, '#FFFFFF')
            self.word_letters = set(self._current_word)
            self.used_letters = set()
            self._tries_limit = 5
            self._in_game     = 1
            self._image_index = 2
            self._helped_word = list(set(self._current_word))
            
        lives = self._tries_limit

        #   Логіка гри
        if lives > 0:
            if(alpha_item == 'help' and self._points > 0):
                user_letter = random.choice(self._helped_word)
                self._helped_word.remove(user_letter)
                self._points -= 1
                window_handler.updatePoints(self._points)
            elif(alpha_item == 'help' and self._points <= 0):
                return
            else:
                user_letter = window_handler._alphabet[alpha_item].upper()
            self.used_letters.add(user_letter)
            if user_letter in self.word_letters:
                self.word_letters.remove(user_letter)
                window_handler.updateButton(user_letter, '#44FF89', 'disabled')
                word_list = [letter if letter in self.used_letters else ' _ ' for letter in self._current_word]
                if(alpha_item != 'help'): self._helped_word.remove(user_letter)
                window_handler.updateWord(''.join(word_list))
            else:
                lives = lives - 1
                self._tries_limit = lives
                window_handler.updateButton(user_letter, '#FF4B4B', 'disabled')
                self._image_index += 1
                window_handler.updateImage(self._image_index)

        if lives == 0:
            self._in_game = 0
            self._points -= 1
            self._strike = 0
            window_handler.updateOldWord(self._current_word, '#FF4B4B')
            window_handler.updatePoints(self._points)
            window_handler.updateStrike(self._strike)

            window_handler.updateWord(self.setNewWordMaskByWindow(), '#FFFFFF')
            window_handler.updateAllButtons()
            
            
        elif ((lives != 0) and (len(self.word_letters) == 0)):
            self._in_game = 0
            self._points += 3
            self._strike += 1
            window_handler.updateOldWord(self._current_word, '#44FF89')
            window_handler.updatePoints(self._points)
            window_handler.updateStrike(self._strike)

            window_handler.updateWord(self.setNewWordMaskByWindow(), '#FFFFFF')
            window_handler.updateAllButtons()            
        
    def setNewWordMaskByWindow(self):
        self._current_word = random.choice(words._word_list)
        self._current_word = self._current_word.upper()
        print(self._current_word)
        word_mask = ''
        for item in range(0, len(self._current_word)):
            word_mask += ' _ '
        return word_mask
