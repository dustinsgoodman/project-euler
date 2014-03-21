package utils;

public class BTNode {
	public BTNode left, right, parent;
	public int data;
	
	public BTNode(int data) {
		this.data = data;
		this.left = null;
		this.right = null;
		this.parent = null;
	}
	
	public BTNode(int data, BTNode parent) {
		this.data = data;
		this.left = null;
		this.right = null;
		this.parent = parent;
	}
	
	public int children_count() {
		int count = 0;
		if (this.left != null) count++;
		if (this.right != null) count++;
		return count;
	}

	@Override
	public String toString() {
		return String.format("%d", this.data);
	}
}
