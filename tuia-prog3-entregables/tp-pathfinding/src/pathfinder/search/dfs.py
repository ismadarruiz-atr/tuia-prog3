from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        # Initialize frontier with the root node
        frontier = StackFrontier()
        frontier.add(root)

       # Check if root is solution
        if grid.objective_test(root.state):
            return Solution(root, expanded)

        # TODO Complete the rest!!
        while True:
            if frontier.is_empty():
                return NoSolution(expanded)
            node = frontier.remove()
            
            if node.state in expanded:
                continue            
            expanded[node.state] = True
            for action in grid.actions(node.state):
                successor = grid.result(node.state, action)
                if successor not in expanded:
                    son = Node("", successor, node.cost + grid.individual_cost(node.state, action), node, action)
                    if grid.objective_test(son.state):
                        return Solution(son, expanded)
                    frontier.add(son)

