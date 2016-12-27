# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 10:37:51 2016

Class find longest chain on given board.
'find_best' method return coordinates of best start point.

@author: Przemyslaw Bieganski, przemyslaw.bieganski88@gmail.com // bieg4n@gmail.com
"""
# imports
import copy

# sample data
sample = [
    ['u', 'd', 'u', 'u'], # ↑ ↓ ↑ ↑
    ['u', 'r', 'l', 'l'], # ↑ → ← ←
    ['u', 'u', 'l', 'u'], # ↑ ↑ ← ↑
    ['l', 'd', 'u', 'l'], # ← ↓ ↑ ←
]

sample2 = [
    ['r', 'r', 'r', 'd'], # → → → ↓
    ['d', 'l', 'l', 'l'], # ↓ ← ← ←
    ['r', 'r', 'r', 'd'], # → → → ↓
    ['l', 'l', 'l', 'l'], # ← ← ← ←
]


# main class
class GrotGame(object):
    '''
    Class find longest chain on given board.
    'find_best' method return coordinates of best start point.
    
    Logic based on rules of this game:
    http://grot.hackathons.stxnext.pl/game.html
    '''   
    
    def __init__(self, board, startposition=(0,0)):
        '''   
        Initialization. Assigns boards to the game and calculate its size.
        '''
        self._start_board = copy.deepcopy(board) # initial board
        self._board = copy.deepcopy(board)
        self._height = len(self._board)
        self._width = len(self._board[0])
        self.position = startposition
    
    
    def __str__(self):
        '''
        Displays the current board in accordance with the declared
        visualization pattern.
        '''
        self.print_board(self._start_board)
        return ''


    def print_board(self, board):
        '''
        Prints current board.
        '''
        wizualizacja = { 'u': '↑', 'd': '↓', 'l': '←', 'r': '→', 'x': 'x'}  
        content = ''
        for row in board:
            for element in row:
                content += element.replace(element, wizualizacja[element])
                content += ' '
            content += '\n'
        print content


    def find_best(self, log=False):
        '''
        It takes all possible scenarios and searching the best.
        As the optimum should be understood that with the longest sequence.
        '''
        results = {}
        # iteruje po calej planszy
        for row in range(self._width):
            for column in range(self._height):
                pos = (row,column)
                results[pos]=self.play_sequence(board=copy.deepcopy(self._board),
                                                position=pos)

        seq_length = {key: len(value) for key, value in results.iteritems()}
        longest = max(seq_length, key=seq_length.get)
        
        print '** Longest sequence **'
        print 'Start position: {}; Length of sequence: {}'.format(longest, seq_length[longest])
        print 'Steps: {}\n'.format(results[longest])

        return longest


    def play_sequence(self, board, position):
        '''
        Takes and play a single scenario
        '''
        sequence = []
        sequence.append(position)

        end_game = False
        
        while end_game is False:
            #print 'RUCH: {}'.format(position)
            end_game, position = self.move(position, board)
            if position:
                sequence.append(position)
            if end_game is True:
                print 'Start position: {}; Length of sequence: {}'.format(sequence[0], len(sequence))
                print 'Board after move:'
                self.print_board(board)

        return sequence


    def move(self, position, board):
        '''
        A single movement on the board. Plus update the value array.
        Input:
        position - tuple with the starting position.
        board - board to test
        Its return two values:
        end_game - boolean value is end_game or not,
        list - start position of next move
        '''
        # check value for a given position
        column = position[1]
        row = position[0]
        # assigns the old value
        direction = board[row][column]

        # changing the value that you can't use it again
        board[row][column] = 'x'
        
        new_column, new_row = column, row
        new_direction = False
        
        # flags
        found = False # true if next move is possible
        end_game = False # true if next move is impossible
        
        while not found and not end_game:
            # some logic
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

            # whether the new position is still in board range
            if new_row in range(self._width) and new_column in range(self._height):
                new_direction = board[new_row][new_column]
            else:
                end_game = True
                return end_game, None
            
            # 'X' Means that field was used earlier 
            if new_direction and new_direction != 'x':
                found = True
        
        if end_game is True:
            return end_game, []
        else:
            return end_game, [new_row, new_column]


x = GrotGame(sample2)
best = x.find_best()
