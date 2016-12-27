# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 19:37:51 2016

Algorytm ma odszukac najdluzszy ciag dla zadanej planszy.
Jako wynik ma zwrocic wspolrzedne punktu startowego najlepszego pola.

@author: Przemyslaw Bieganski, przemyslaw.bieganski88@gmail.com // bieg4n@gmail.com
"""
# sample data
sample = [
    ['r', 'd', 'u', 'u'], # ↑ ↓ ↑ ↑
    ['u', 'r', 'l', 'l'], # ↑ → ← ←
    ['u', 'u', 'l', 'u'], # ↑ ↑ ← ↑
    ['l', 'd', 'u', 'l'], # ← ↓ ↑ ←
]


class GrotGame(object):
    '''
    Testowa implementacja gry GROT.
    Zasady:
    Pola pokazuja cztery kierunki. Po wybraniu pola startowego,
    przekazywanego do obiektu jako 'startposition' uruchamiana jest
    sekwencja ruchow - wskazywane sa sasiednie pola zgodnie z grotem strzalki.
    Pole raz wybrane znika. Sekwencja konczy sie gdy grot strzalki nie jest
    w stanie wskazac kolejnego pola.
    '''   
    
    def __init__(self, board, startposition=(0,0)):
        '''
        Inicjalizacja. Przypisuje tablice do gry i oblicza jej rozmiary.
        '''
        self._start_board = board # plansza poczatkowa
        self._board = self._start_board
        self._height = len(self._board)
        self._width = len(self._board[0])
        self.position = startposition
    
    
    def __str__(self):
        '''
        Wyswietla aktualna tablice zgodnie z zadeklarowanym wzorcem
        wizualizacji.
        '''
        self.print_board(self._start_board)
        return ''


    def move(self, position, board):
        '''
        Pojedynczy ruch na tablicy. Plus update wartosci tablicy.
        Argument wejsciowy:
        tuple z pozycja startowa ruchu.
        Zwraca wartosc logiczna: prawda/falsz
        w zaleznosci czy nastepny ruch byl mozliwy do przeprowadzenia czy tez nie.
        '''
        # sprawdzam wartosc dla podanej pozycji
        column = position[1]
        row = position[0]
        # pobieram stara wartosc
        direction = board[row][column]
        # wstawiam nowa - jako uzyte pole
        board[row][column] = 'x'
        print 'Kierunek ruchu: {}'.format(direction)
        
        new_column, new_row = column, row
        new_direction = False
        found = False # nowy ruch mozliwy - znaleziono
        end_game = False # nowu ruch niemozliwy - koniec gry
        
        while not found and not end_game:
            # nowa pozycja
            if direction == 'u':
                new_row -= 1
            elif direction == 'd':
                new_row += 1
            elif direction == 'r':
                new_column += 1
            elif direction == 'l':
                new_column -= 1
            else:
                end_game = True

            # czy nowa pozycja w zakresie tablicy
            if new_row in range(self._width) and new_column in range(self._height):
                new_direction = board[new_row][new_column]
            else:
                end_game = True
                return end_game, None

            if new_direction and new_direction != 'x':
                found = True
        
        if end_game is True:
            return end_game, []
        else:
            return end_game, [new_row, new_column]


    def play_sequence(self, board, position):
        '''
        Rozgrywa pojedynczy scenariusz 
        '''
        sequence = []
        sequence.append(position)

        end_game = False

        print 'START!!'
        self.print_board(board)
        
        while end_game is False:
            print 'RUCH: {}'.format(position)
            end_game, position = self.move(position, board)
            sequence.append(position)
            if end_game is False:
                self.print_board(board)

        print 'KONIEC GRY!!\n{}'.format(sequence)

    
    def find_best(self):
        '''
        Rozgrywa wszystkie mozliwe scenariusze. Wyszukujac tego optymalnego.
        Jako optymalny nalezy rozumiec ten, w ktorym da sie wykonac najwiecej ruchow.
        '''
        pass


    def print_board(self, board):
        '''
        Wyswietla w konsoli aktualna tablice.
        '''
        wizualizacja = { 'u': '↑', 'd': '↓', 'l': '←', 'r': '→', 'x': 'x'}  
        content = '' # kontener na tresc do wyswietlenia
        for row in board:
            for element in row:
                content += element.replace(element, wizualizacja[element])
                content += ' '
            content += '\n'
        print content
        

x = GrotGame(sample)
x.play_sequence(position=(2,0), board=x._board[::])

















