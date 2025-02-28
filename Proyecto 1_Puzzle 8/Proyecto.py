import tkinter as tk
import random
import heapq
import time

def manhattan_distance(puzzle, goal):
    distance = 0
    goal_positions = {value: (i, j) for i, row in enumerate(goal) for j, value in enumerate(row)}
    for i in range(3):
        for j in range(3):
            value = puzzle[i][j]
            if value != 0:
                goal_i, goal_j = goal_positions[value]
                distance += abs(goal_i - i) + abs(goal_j - j)
    return distance

def a_star_search(start, goal):
    visited = set()
    frontier = []
    heapq.heappush(frontier, start)
    while frontier:
        current = heapq.heappop(frontier)
        if current.puzzle == goal.puzzle:
            return current
        visited.add(str(current.puzzle))
        for next_node in current.find_next_nodes():
            if str(next_node.puzzle) not in visited:
                heapq.heappush(frontier, next_node)
    return None

def generate_puzzle():
    numbers = list(range(1, 9)) + [0]
    random.shuffle(numbers)
    puzzle = [numbers[i * 3:(i + 1) * 3] for i in range(3)]
    return puzzle

class Node:
    def __init__(self, puzzle, movement, depth, manhattan, previous):
        self.depth = depth
        self.puzzle = puzzle
        self.movement = movement
        self.manhattan = manhattan
        self.previous = previous
    
    def __lt__(self, other):
        return (self.depth + self.manhattan) < (other.depth + other.manhattan)
    
    def move_piece(self, movement):
        new_puzzle = [row.copy() for row in self.puzzle]
        x, y = next((i, j) for i in range(3) for j in range(3) if self.puzzle[i][j] == 0)
        if movement == 'Arriba' and x > 0:
            new_puzzle[x][y], new_puzzle[x - 1][y] = new_puzzle[x - 1][y], new_puzzle[x][y]
        elif movement == 'Abajo' and x < 2:
            new_puzzle[x][y], new_puzzle[x + 1][y] = new_puzzle[x + 1][y], new_puzzle[x][y]
        elif movement == 'Izquierda' and y > 0:
            new_puzzle[x][y], new_puzzle[x][y - 1] = new_puzzle[x][y - 1], new_puzzle[x][y]
        elif movement == 'Derecha' and y < 2:
            new_puzzle[x][y], new_puzzle[x][y + 1] = new_puzzle[x][y + 1], new_puzzle[x][y]
        else:
            return None
        return new_puzzle
    
    def find_next_nodes(self):
        next_nodes = []
        for movement in ['Arriba', 'Abajo', 'Izquierda', 'Derecha']:
            new_puzzle = self.move_piece(movement)
            if new_puzzle is not None:
                next_nodes.append(Node(new_puzzle, movement, self.depth + 1, manhattan_distance(new_puzzle, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]), self))
        return next_nodes
    
    def next_way(self, start):
        way = []
        current = self
        while current != start:
            way.append(current)
            current = current.previous
        way.append(start)
        way.reverse()
        return way
        

class PuzzleGUI:
    def __init__(self, root, solution_path, result_depth):
        self.root = root
        self.solution_path = solution_path
        self.current_step = 0
        self.grid_size = 3
        self.labels = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.result_label = tk.Label(self.root, text=f'Solución encontrada en: {result_depth} movimientos', font=('Helvetica', 14))
        self.result_label.grid(row=4, column=0, columnspan=3, pady=10)
        self.create_grid()
        self.update_grid()
        self.root.after(1000, self.next_step)

    def create_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                label = tk.Label(self.root, text='', font=('Helvetica', 24), width=4, height=2, borderwidth=2, relief='solid')
                label.grid(row=i, column=j, padx=5, pady=5)
                self.labels[i][j] = label
    
    def update_grid(self):
        puzzle = self.solution_path[self.current_step].puzzle
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                value = puzzle[i][j]
                self.labels[i][j].config(text=str(value) if value != 0 else '', bg='white' if value != 0 else 'lightgray')
    
    def next_step(self):
        if self.current_step < len(self.solution_path) - 1:
            self.current_step += 1
            self.update_grid()
            self.root.after(800, self.next_step)

def main():
    #puzzle = generate_puzzle()
    puzzle = [[1, 2, 4], [4, 6, 5 ], [7, 8, 0]]  

    start = Node(puzzle, '', 0, manhattan_distance(puzzle, [[1, 2, 3], [4, 6, 5], [7, 8, 0]]), None)
    goal = Node([[1, 2, 3], [4, 5, 6], [7, 8, 0]], '', 0, 0, None)
    result = a_star_search(start, goal)
    
    if result is not None:
        path = result.next_way(start)
        root = tk.Tk()
        root.title('8-Puzzle')
        gui = PuzzleGUI(root, path, result.depth)
        root.mainloop()
    else:
        print('No se encontró solución')

if __name__ == '__main__':
    main()
