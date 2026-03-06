# -*- coding: utf-8 -*-
"""Grille 2D pour la représentation du monde."""

import random


class Grid:
    """Grille bidimensionnelle permettant la manipulation des cellules.

    Attributes:
        grid: Matrice 2D des valeurs de la grille.
        lines_count: Nombre de lignes.
        columns_count: Nombre de colonnes.
    """

    def __init__(self, grid_init):
        self.grid = grid_init
        self.lines_count = len(grid_init)
        self.columns_count = len(grid_init[0]) if len(grid_init) else 0

    def fill_random(self, values):
        self.grid = [[random.choice(values) for _ in range(self.columns_count)] for _ in range(self.lines_count)]

    def get_line(self, line_number):
        return self.grid[line_number]

    def get_column(self, column_number):
        return [line[column_number] for line in self.grid]

    def get_grid_str(self, separator="\t"):
        return "\n".join(self.get_line_str(line_number, separator) for line_number in range(self.lines_count))

    def get_diagonal(self):
        diagonal_size = min(self.lines_count, self.columns_count)
        return [self.grid[line_number][line_number] for line_number in range(diagonal_size)]

    def get_anti_diagonal(self):
        diagonal_size = min(self.lines_count, self.columns_count)
        return [self.grid[line_number][self.columns_count - line_number - 1] for line_number in range(diagonal_size)]

    def is_square(self):
        return self.lines_count == self.columns_count

    def get_coordinates_from_cell_number(self, cell_number):
        return cell_number // self.columns_count, cell_number % self.columns_count

    def get_cell_number_from_coordinates(self, line_number, column_number):
        return line_number * self.columns_count + column_number

    def get_cell(self, cell_number):
        line_number, column_number = self.get_coordinates_from_cell_number(cell_number)
        return self.grid[line_number][column_number]

    def set_cell(self, cell_number, value):
        line_number, column_number = self.get_coordinates_from_cell_number(cell_number)
        self.grid[line_number][column_number] = value

    def get_neighbour(self, line_number, column_number, delta, is_tore=False):
        new_line_number, new_column_number = line_number + delta[0], column_number + delta[1]
        if is_tore:
            return self.grid[new_line_number % self.lines_count][new_column_number % self.columns_count]
        if 0 <= new_line_number < self.lines_count and 0 <= new_column_number < self.columns_count:
            return self.grid[new_line_number][new_column_number]
        return None

    def get_neighborhood(self, line_number, column_number, deltas, is_tore=False):
        return [self.get_neighbour(line_number, column_number, delta, is_tore) for delta in deltas]

    def has_equal_values(self, value):
        return all(all(type(grid_value) is type(value) for grid_value in line) for line in self.grid)

    def get_same_value_cell_numbers(self, value):
        return [
            cell_number
            for cell_number in range(self.lines_count * self.columns_count)
            if type(self.get_cell(cell_number)) is type(value)
        ]

    def get_line_str(self, line_number, separator="\t"):
        return separator.join(str(value) for value in self.grid[line_number])
