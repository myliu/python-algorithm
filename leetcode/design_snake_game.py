from collections import deque

class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.snake = deque([[0, 0]])
        self.width = width
        self.height = height
        self.food = deque(food)
        self.directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}


    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        snake = self.snake
        food = self.food
        x, y = self.directions[direction]
        new_head = [snake[0][0]+x, snake[0][1]+y]

        if new_head[0] < 0 or new_head[0] >= self.height or new_head[1] < 0 or new_head[1] >= self.width or \
            (new_head in snake and new_head != snake[-1]):
                return -1

        if food and new_head == food[0]:
            snake.appendleft(new_head)
            food.popleft()
        else:
            snake.appendleft(new_head)
            snake.pop()

        return len(snake)-1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)