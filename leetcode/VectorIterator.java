package interview.coding.airbnb;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

public class VectorIterator implements Iterator {

	   boolean hasRemoved = false;
//	    
//	    Iterator<Integer> last = null;
//	    Iterator<Integer> liter = null;
//	    boolean sameIter = false;
//	    Iterator<List<Integer>> iterator = null;
//	    public VectorIterator(List<List<Integer>> vec2d) {
//	        if (vec2d != null) {
//	            iterator = vec2d.iterator();
//	            while (iterator.hasNext()) {
//	                List<Integer> list = iterator.next();
//	                liter = list.iterator();
//	                if (liter.hasNext()) {
//	                    break;
//	                }
//	            }
//	        }
//	    }
//
//	    @Override
//	    public Integer next() {
//	        return liter.next();
//	    }
//
//	    @Override
//	    public boolean hasNext() {
//	        if (liter == null) { return false; }
//	        if (liter.hasNext()) {
//	            sameIter = true;
//	            return true;
//	        }
//	        sameIter = false;
//	        last = liter;
//	        while (iterator.hasNext()) {
//	            liter = iterator.next().iterator();
//	            if (liter.hasNext()) {
//	                return true;
//	            }
//	        }
//	        
//	        return false;
//	    }
//	    
//	    public void remove() {
//	        if (hasRemoved) {
//	            return;
//	        }
//	        hasRemoved = true;
//	        
//	        if (sameIter) {
//	            liter.remove();
//	        } else {
//	            last.remove();
//	        }
//	    }
	
	  	int currentRow = 0;
	    int currentCol = 0;
	    List<List<Integer>> vec;
	    public VectorIterator(List<List<Integer>> vec2d) {
	        vec = vec2d;
	    }

	    @Override
	    public Integer next() {
	        return vec.get(currentRow).get(currentCol++);
	    }

	    @Override
	    public boolean hasNext() {
	        if (currentRow < vec.size() && currentCol < vec.get(currentRow).size()) {
	            return true;
	        } else if (currentRow == vec.size()) {
	            return false;
	        } else {
	            do { currentRow++; } while (currentRow < vec.size() && vec.get(currentRow).size() == 0);
	            if (currentRow == vec.size()) { return false; }
	            currentCol = 0;
	            return true;
	        }
	    }
	    
	    public void remove() {
	    	if (hasRemoved) {
	    		return;
	    	}
	    	hasRemoved = true;
	        if (currentCol > 0) {
	            vec.get(currentRow).remove(currentCol-1);
	            currentCol--;
	        } else {
	            int r = currentRow;
	            do { r--; } while (r >= 0 && vec.get(r).size() == 0);
	            if (r >= 0) {
	                vec.get(r).remove(vec.get(r).size()-1);
	            }
	        }
	    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<List<Integer>> test1 = new ArrayList<>();
		test1.add(Arrays.asList());
		
		VectorIterator vi = new VectorIterator(test1);
		
		while (vi.hasNext()) {
			System.out.println(vi.next());
		}
		
		System.out.println("-----------------------");
		
		test1.add(new ArrayList<Integer>(Arrays.asList(1,2)));
		
		vi = new VectorIterator(test1);
		
		while (vi.hasNext()) {
			System.out.println(vi.next());
			vi.remove();
			break;
		}
		if (vi.hasNext()) {
			System.out.println(vi.next());
		}
		System.out.println("-----------------------");
		
//		test1.add(new ArrayList<Integer>(Arrays.asList(3)));
//		vi = new VectorIterator(test1);
//		
//		while (vi.hasNext()) {
//			int v = vi.next();
//			System.out.println(v);
////			if (v == 3) {
////				vi.remove();
////			}
//		}
//		vi.remove();
		
//		System.out.println("-----------------------");
//		vi = new VectorIterator(test1);
//		
//		while (vi.hasNext()) {
//			System.out.println(vi.next());
//		}
//		System.out.println("-----------------------");
	}

}
