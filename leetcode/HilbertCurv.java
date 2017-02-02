package interview.coding.airbnb;

import java.util.HashMap;
import java.util.Map;

public class HilbertCurv {

	static Map<String, Integer> base = new HashMap<>();
	static {
		base.put("00", 1);
		base.put("01", 2);
		base.put("11", 3);
		base.put("10", 4);
	}

	static Map<String, Integer> map = new HashMap<>();
	static {
		map.put("11", 0);
		map.put("-11", 1);
		map.put("-1-1", 2);
		map.put("1-1", 3);
	}
	
	static int[][] dir = new int[][]{
		{-1, -1},
		{0, -1},
		{0, 0},
		{-1, 0}
	};
	
	static int[] time = new int[]{2, 1, 0, 3};
	
	public static int getNumber(int x, int y, int iter) {
		// recursion exit
		if (iter < 1) {
			return -1;
		} 
		if (iter == 1) {
			return base.get(x+""+y);
		}
		// calculate which region the point is in
		int rBound = (1<<(iter-1));
		int cBound = (1<<(iter-1));
		
		int xx = x < rBound ? -1 : 1;
		int yy = y < cBound ? -1 : 1;
		
		int pad = (1<<(iter-1));
		int co = map.get(xx+""+yy);
		int tempX = x + dir[co][0] * pad;
		int tempY = y + dir[co][1] * pad;
		
		int nx = tempX, ny = tempY;
		if (co == 2) {
			nx = tempY;
			ny = tempX;
		} else if (co == 3) {
			int M = (1<<iter);
			nx = M - tempY;
			ny = M - tempX;
		}
		
		return getNumber(nx, ny, iter-1) + time[co] * (1 << iter);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(getNumber(0,1,1));
		System.out.println(getNumber(1,1,2));
		System.out.println(getNumber(2,2,2));
	}

}
