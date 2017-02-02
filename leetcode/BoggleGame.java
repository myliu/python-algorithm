package interview.coding.airbnb;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class BoggleGame {    
//    public static class TrieNode{
//        public boolean isStr;
//        public String content;
//        public HashMap<Character,TrieNode> children;
//        public TrieNode(){
//            this.children = new HashMap<Character, TrieNode>();
//        }
//    }
//    
//    TrieNode root;
//    private int[] xRotate = {-1,1,0,0};
//    private int[] yRotate = {0,0,-1,1};
//    
//    private void insert(String s){
//        TrieNode runner = root;
//        for(int i = 0; i < s.length(); i++){
//            char curChar = s.charAt(i);
//            if(!runner.children.containsKey(curChar)) runner.children.put(curChar, new TrieNode());
//            runner = runner.children.get(curChar);
//        }
//        runner.isStr = true;
//        runner.content = s;
//    }
//    
//    private List<String> res = new ArrayList<String>();
//    
//    private List<String> longestPath(char[][] grid, List<String> strs){
//        if(grid == null || grid.length == 0 || strs == null || strs.size() == 0) return res;
//        this.root = new TrieNode();
//        for(String s : strs) insert(s);
//        int height = grid.length;
//        int width = grid[0].length;
//        List<String> buffer = new ArrayList<String>();
//        boolean[][] visited = new boolean[height][width];
//        for(int i = 0; i < height;i++){
//            for(int j = 0; j < width; j++){
//                if(root.children.containsKey(grid[i][j])){
//                    dfs(buffer,grid,root,i,j,visited);
//                }
//            }
//        }
//        return res;
//    }    
//    
//    private void dfs(List<String> buffer, char[][] grid, TrieNode root, int x, int y, boolean[][] visited){
//        if(x < 0 || x >= grid.length || y < 0 || y >= grid[0].length || visited[x][y]) return;
//        else{
//            if(!root.children.containsKey(grid[x][y])) return;
//            else{
//                visited[x][y] = true;
//                char curChar = grid[x][y];
//                root = root.children.get(curChar);
//                if(root.isStr){
//                    //use it
//                    buffer.add(root.content);
//                    if(buffer.size() > res.size()) res = new ArrayList<String>(buffer);
//                    for(int i = 0; i < 4; i++){
//                         dfs(buffer,grid, root, x + xRotate[i], y +  yRotate[i], visited);
//                    }
//                    buffer.remove(buffer.size() - 1);
//                }
//                for(int i = 0; i < 4; i++){
//                    dfs(buffer,grid, root, x + xRotate[i], y +  yRotate[i], visited);
//                }
//                visited[x][y] = false;
//            }
//        }
//    }
	
	class TrieNode {
		boolean isWord;
		TrieNode[] children = new TrieNode[26];
	}
	
	public List<String> longestPath(char[][] matrix, List<String> dic) {
		List<String> result = new ArrayList<>();
		if (dic.size() == 0 || matrix == null) {
			return result;
		}
		TrieNode root = buildTrie(dic);
		for (int i = 0; i < matrix.length; i++) {
			for (int j = 0; j < matrix[0].length; j++) {
				dfs(matrix, i, j, root, root, new ArrayList<>(), result, new StringBuilder());
			}
		}
		
		return result;
	}
	
	private void dfs(char[][] matrix, int i, int j, TrieNode root, TrieNode node, List<String> path, List<String> result, StringBuilder builder) {
		if (i < 0 || i >= matrix.length || j < 0 || j >= matrix[0].length || node == null) { return; }
		if (matrix[i][j] == '*') { return; }
		char ch = matrix[i][j];
		if (node.children[ch-'a'] == null) { return; }
		matrix[i][j] = '*';
		builder.append(ch);
		TrieNode next = node.children[ch-'a'];
		
		if (next.isWord) {
			path.add(builder.toString());
			if (path.size() > result.size()) {
				result.clear();
				result.addAll(new ArrayList<>(path));
			}
			dfs(matrix, i+1, j, root, root, path, result, new StringBuilder());
			dfs(matrix, i-1, j, root, root, path, result, new StringBuilder());
			dfs(matrix, i, j+1, root, root, path, result, new StringBuilder());
			dfs(matrix, i, j-1, root, root, path, result, new StringBuilder());
		
			path.remove(path.size()-1);
		}
		
		dfs(matrix, i+1, j, root, next, path, result, builder);
		dfs(matrix, i-1, j, root, next, path, result, builder);
		dfs(matrix, i, j+1, root, next, path, result, builder);
		dfs(matrix, i, j-1, root, next, path, result, builder);
		
		builder.deleteCharAt(builder.length()-1);
		matrix[i][j] = ch;
	}
	
	private TrieNode buildTrie(List<String> dic) {
		TrieNode root = new TrieNode();
		for (String s : dic) {
			TrieNode node = root;
			for (char c : s.toCharArray()) {
				if (node.children[c-'a'] == null) {
					node.children[c-'a'] = new TrieNode();
				}
				node = node.children[c-'a'];
			}
			node.isWord = true;
		}
		return root;
	}
	
    public static void main(String[] args) {
    	BoggleGame g = new BoggleGame();
    	List<String> p = g.longestPath(new char[][]{
    		{'a', 'b', 'c', 'd'},
    		{'x', 'c', 'b', 'a'}
    	}, Arrays.asList("abc", "abcd"));
    	
    	System.out.println(p);
    }
}
