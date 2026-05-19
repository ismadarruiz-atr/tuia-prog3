from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)


        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        # Check if root is solution
        if grid.objective_test(root.state):
            return Solution(root, reached)

        # Initialize frontier with the root node
        frontier = QueueFrontier()
        frontier.add(root)
        i = 0


        # TODO Complete the rest!!
        while True:

            i += 1
            if frontier.is_empty():
                return NoSolution(reached)

            node = frontier.remove()

            for action in grid.actions(node.state):

                successor = grid.result(node.state, action)

                if successor not in reached:
                    son = Node(str(i), successor, node.cost + grid.individual_cost(node.state, action), node, action)
                    if grid.objective_test(son.state):
                        return Solution(son, reached)

                    reached[son.state] = True
                    frontier.add(son)
            