Project for assessment in "Principles of Computing (Part 2)" course at Rice university.  
https://www.coursera.org/learn/principles-of-computing-2  
#**Assessment: MiniMax Tick Tack Toe**

The general idea on Minimax is to search the entire game tree alternating between minimizing and maximizing the score at each level. For thi
s to work, you need to start at the bottom of the tree and work back towards the root. However, instead of actually building the game tree t
o do this, you should use recursion to search the tree in a depth-first manner. Your recursive function should call itself on each child of
the current board position and then pick the move that maximizes (or minimizes, as appropriate) the score. If you do this, your recursive fu
nction will naturally explore all the way down to the bottom of the tree along each path in turn, leading to a depth first search that will
implement Minimax.  
For this mini-project, you need only implement one function:

- mm_move(board, player): This function takes a current board and which player should move next. The function should use Minimax to return
 a tuple which is a score for the current board and the best move for the player in the form of a (row, column) tuple. In situations in whic
h the game is over, you should return a valid score and the move (-1, -1). As (-1, -1) is an illegal move, it should only be returned in cas
es where there is no move that can be made.




