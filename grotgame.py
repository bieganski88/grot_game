# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 19:37:51 2016

Algorytm ma odszukac najdluzszy ciag dla zadanej planszy.
Jako wynik ma zwrocic wspolrzedne punktu startowego najlepszego pola.

@author: Przemyslaw Bieganski, przemyslaw.bieganski88@gmail.com // bieg4n@gmail.com
"""
# sample data
sample = [
    ['u', 'd', 'u', 'u'], # ↑ ↓ ↑ ↑
    ['u', 'r', 'l', 'l'], # ↑ → ← ←
    ['u', 'u', 'l', 'u'], # ↑ ↑ ← ↑
    ['l', 'd', 'u', 'l'], # ← ↓ ↑ ←
]


class GrotGame(object):
    '''
    Tresc, tresc, tresc
    '''   
    
    def __init__(self, board, startposition=(0,0)):
        '''
        Inicjalizacja. Przypisuje tablice do gry i oblicza jej rozmiary.
        '''
        self._board = board
        self._height = len(self._board)
        self._width = len(self._board[0])
        self.position = startposition
    
    
    def __str__(self):
        '''
        Wyswietla aktualna tablice zgodnie z zadeklarowanym wzorcem
        wizualizacji.
        '''
        wizualizacja = { 'u': '↑', 'd': '↓', 'l': '←', 'r': '→', 'x': 'x'}  
        content = '' # kontener na tresc do wyswietlenia
        board = self._board
        for row in board:
            for element in row:
                content += element.replace(element, wizualizacja[element])
                content += ' '
            content += '\n'
        print content
        return ''


    def move(self, position):
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
        direction = self._board[row][column]

        new_column = column
        new_row = row
        found = False # nowy ruch mozliwy - znaleziono
        end_game = False # nowu ruch niemozliwy - koniec gry
        
        while (found and end_game) is False:
            # nowa pozycja
            if direction == 'u':
                new_row -= 1
            elif direction == 'd':
                


    def play_game(self):
        '''
        Rozgrywa pojedynczy scenariusz 
        '''
        pass


    def find_best(self):
        '''
        Rozgrywa wszystkie mozliwe scenariusze. Wyszukujac tego optymalnego.
        Jako optymalny nalezy rozumiec ten, w ktorym da sie wykonac najwiecej ruchow.
        '''
        pass
        



















