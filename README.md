# EfficientBinaryTree

These header files can be used to create a data structure for storing n nodes.  Since the initial need for this system related to my university's rocket team, Rivercity Rocketry, the nodes are currently set up to hold each state of the rocket.  The program can easily be edited to hold any set of values at each node.  Using this structure instead of an array or list allows for a more efficient program.  Getting and Setting node values with this structure ensures O(log(n)) instead of O(n).

The program begins with a binary heap to develop the most efficient binary tree.  Once the binary heap is created, each value is fed into the initialization of the Binary Tree.  Once the Binary Tree is initialized with 0 values, nodes can easily be edited using the replace method which takes a key and a new state.  It is important to note that with this system, left and right children should not be edited after initialization.

For use, I imagine a state (node) will be edited throughout the program and then used to replace the current value within the tree.  This means it is important for the programmer to use a variable to keep track of the oldest data point within the tree and replace at that node.

I have developed this system in both Python and C for multiple embedded system applications.  Please feel free to reach out to me if you have any questions.
