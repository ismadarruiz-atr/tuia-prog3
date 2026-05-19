from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        
        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        frontier = PriorityQueueFrontier()
        frontier.add(root, root.cost)

        # TODO Complete the rest!!
        while True:
            if frontier.is_empty():
                return NoSolution(reached)
            
            node = frontier.pop()

            if grid.objective_test(node.state):
                return Solution(node, reached)
            
            for action in grid.actions(node.state):
                successor = grid.result(node.state, action)
                cost_succesor = node.cost + grid.individual_cost(node.state, action)

                if successor not in reached or cost_succesor < reached[successor]:
                    son = Node("", successor, cost_succesor, node, action)
                    reached[successor] = cost_succesor
                    frontier.add(son, cost_succesor)

   
