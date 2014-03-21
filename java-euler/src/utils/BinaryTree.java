package utils;

import java.util.Stack;
import java.util.concurrent.ConcurrentLinkedQueue;

public class BinaryTree {
	public BTNode root;
	private int node_count;
	
	public BinaryTree() {
		this.root = null;
		this.node_count = 0;
	}
	
	public BTNode search(int value) {
		BTNode current = this.root;
					
		while (current != null) {
			if (current.data < value) {
				current = current.left;
			} else if (current.data > value) {
				current = current.right;
			} else {
				return current;
			}
		}
		
		return null;
	}
	
	public BTNode insert(int value) {
		BTNode current, prev;
		
		if (this.root == null) {
			this.root = new BTNode(value);
			return this.root;
		}
		
		current = this.root;
		prev = this.root;
		while (current != null) {
			if (current.data > value) {
				if (current.left != null)
					current = current.left;
				else {
					current.left = new BTNode(value, current);
					this.node_count++;
					return current.left;
				}
			} else if (current.data < value) {
				if (current.right != null) {
					current = current.right;
				} else {
					current.right = new BTNode(value, current);
					this.node_count++;
					return current.right;
				}
			} else {
				return current;
			}
		}
		return current;
	}

	public void remove(int value) {
		BTNode parent, successor, current = this.search(value);
		
		if (current == null) return;

		this.node_count--;
		parent = current.parent;
		if (current.left == null && current.right == null) {
			if (parent.left == current) {
				parent.left = null;
			} else {
				parent.right = null;
			}
			return;
		} else if (current.left == null) {
			if (parent.left == current) {
				parent.left = current.right;
			} else {
				parent.right = current.right;
			}
			return;
		} else if (current.right == null) {
			if (parent.left == current) {
				parent.left = current.left;
			} else {
				parent.right = current.left;
			}
			return;
		} else {
			successor = minimum(current.right);
			if (successor.parent != current) {
				successor.parent.left = null;
			}
			successor.parent = current.parent;
			
			successor.left = current.left;
			current.left.parent = successor;
			successor.right = current.right;
			current.right.parent = successor;
			
			if (current.parent.left == current) {
				current.parent.left = successor;
			} else {
				current.parent.right = successor;
			}
			return;
		}
	}
	
	public int size() {
		return this.node_count;
	}
	
	public boolean isEmpty() {
		return this.node_count == 0;
	}
	
	public boolean isRoot(BTNode node) {
		return node == this.root;
	}
	
	public static BTNode minimum(BTNode node) {
		if (node == null) return null;
		while (node.left != null)
			node = node.left;
		return node;
	}
	
	public static BTNode maximum(BTNode node) {
		if (node == null) return null;
		while (node.right != null)
			node = node.right;
		return node;
	}
	
	public static boolean isInternal(BTNode node) {
		return !isExternal(node);
	}
	
	public static boolean isExternal(BTNode node) {
		return node.left == null && node.right == null;
	}
	
	public void print_dfs() {
		BTNode current = this.root;
		Stack<BTNode> stack = new Stack<BTNode>();
		stack.push(current);
		
		while (!stack.isEmpty()) {
			current = stack.pop();
			System.out.print(current + " ");
			if (current.right != null) stack.push(current.right);
			if (current.left != null) stack.push(current.left);
		}
	}
	
	public void print_bfs() {
		BTNode current = this.root;
		ConcurrentLinkedQueue<BTNode> queue = new ConcurrentLinkedQueue<BTNode>();
		queue.add(current);
		
		while (!queue.isEmpty()) {
			current = queue.poll();
			System.out.print(current + " ");
			if (current.left != null) queue.add(current.left);
			if (current.right != null) queue.add(current.right);
		}
	}
	
	public static void print_inorder(BTNode node) {
		if (node == null) return;
		print_inorder(node.left);
		System.out.print(node + " ");
		print_inorder(node.right);
	}
	
	public static void print_preorder(BTNode node) {
		if (node == null) return;
		System.out.print(node + " ");
		print_preorder(node.left);
		print_preorder(node.right);
	}
	
	public static void print_postorder(BTNode node) {
		if (node == null) return;
		print_postorder(node.left);
		print_postorder(node.right);
		System.out.print(node + " ");
	}
	
	public void printnode(BTNode x, int h) {
		for (int i = 0; i < h; i++)
			System.out.print("               ");

		System.out.println(x);
	}
	
	void printBST() {
		showR( root, 0 );
		System.out.println("================================");
	}

	public void showR(BTNode t, int h) {
		if (t == null) return;
		
		showR(t.right, h+1);
		printnode(t, h);
		showR(t.left, h+1);
	}
}

/*
    def out(self, start_node = None):
        if start_node == None:
            start_node = self.root
        space_symbol = " "
        spaces_count = 80
        out_string = ""
        initial_spaces_string  = space_symbol * spaces_count + "\n" 
        if not start_node:
            return "Tree is empty"
        else:
            level = [start_node]
            while (len([i for i in level if (not i is None)])>0):
                level_string = initial_spaces_string
                for i in xrange(len(level)):
                    j = (i+1)* spaces_count / (len(level)+1)
                    level_string = level_string[:j] + (str(level[i]) if level[i] else space_symbol) + level_string[j+1:]
                level_next = []
                for i in level:
                    level_next += ([i.left, i.right] if i else [None, None])
                level = level_next
                out_string += level_string
*/