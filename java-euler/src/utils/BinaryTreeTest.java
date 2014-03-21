package utils;

public class BinaryTreeTest {

	public static void main(String[] args) {
		BinaryTree x = new BinaryTree();
		
		x.insert(9999);
		x.printBST();
		x.insert(1000);
		x.printBST();
		x.insert(8888);
		x.printBST();
		x.insert(500);
		x.printBST();
		x.insert(2000);
		x.printBST();
		x.insert(1500);
		x.printBST();
		x.insert(700);
		x.printBST();
		x.insert(1900);
		x.printBST();
		x.insert(4000);
		x.printBST();
		x.insert(2000);
		x.printBST();
		x.insert(5000);
		x.printBST();
		x.insert(1600);
		x.printBST();
		
		x.remove(9999);
		x.printBST();
		x.remove(1000);
		x.printBST();
	}
}
