package interview.coding.airbnb;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class FreeInterval {

	static class Interval {
		int start;
		int end;
		public Interval(int s, int e) {
			start = s;
			end = e;
		}
		public String toString() {
			return start + "-" + end;
		}
	}
	
	static public List<Interval> getFreeIntervals(List<Interval> list) {
		Collections.sort(list, (Interval i1, Interval i2) -> {
			if (i1.start == i2.start) {
				return i1.end - i2.end;
			}
			return i1.start - i2.start;
		});
		
		int[] start = new int[list.size()];
		int[] end = new int[list.size()];
		
		int index = 0;
		for (Interval it : list) {
			start[index] = it.start;
			end[index++] = it.end;
		}
		
		List<Interval> result = new LinkedList<>();
		int count = 0;
		int i1 = 0, i2 = 0;
		while (i1 < start.length && i2 < end.length) {
			if (start[i1] <= end[i2]) {
				i1++;
				count++;
			} else {
				i2++;
				count--;
			}
			if (count == 0) {
				result.add(new Interval(end[i2-1], start[i1]));
			}
		}
		return result;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<Interval> input = new ArrayList<>();
		input.add(new Interval(1,3));
		input.add(new Interval(6,7));
		input.add(new Interval(2,3));
		input.add(new Interval(9,12));
		input.add(new Interval(2,4));
		System.out.println(getFreeIntervals(input));
		
	}

}
