package interview.coding.airbnb;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class FloorCeil {

	static class Node {
		int index;
		double decimal;
		public Node(int i, double d) {
			index = i;
			decimal = d;
		}
	}
	
	public static int[] convert(double[] A) {
		int[] B = new int[A.length];
		List<Node> nodes = new ArrayList<>();
		double T = 0;
		int floorSum = 0;
		for (int i = 0; i < A.length; i++) {
			T += A[i];
			floorSum += Math.floor(A[i]);
			if (Math.ceil(A[i]) != A[i]) {
				nodes.add(new Node(i, Math.ceil(A[i])-A[i]));
			}
		}
		
		T = Math.round(T);
		int count = (int)T - floorSum;
		Set<Integer> ceilIndex = new HashSet<>();
		Collections.sort(nodes, (Object n1, Object n2) -> {
			Node nn1 = (Node)n1;
			Node nn2 = (Node)n2;
			if (nn1.decimal == nn2.decimal) {
				return 0;
			} else if (nn1.decimal < nn2.decimal) {
				return -1;
			} else {
				return 1;
			}
		});
		
		for (int i = 0; i < count; i++) {
			ceilIndex.add(nodes.get(i).index);
		}
		for (int i = 0; i < B.length; i++) {
			if (ceilIndex.contains(i)) {
				B[i] = (int)Math.ceil(A[i]);
			} else {
				B[i] = (int)Math.floor(A[i]);
			}
		}
		return B;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		double[] A = new double[]{2.2, 3.8, 4.0, 6.7};
		int[] B = convert(A);
		for (int i : B) {
			System.out.println(i);
		}
	}

}
