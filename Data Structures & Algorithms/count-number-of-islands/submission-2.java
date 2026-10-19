class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for(int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[i].length; j++){
                count += check(grid, i, j);
            }
        }
        return count;
    }
}
public int check(char[][] grid,int row, int column){
    if(flip(grid, row, column)){
        if(column > 0){
            check(grid, row, column - 1);
        }
        if(column < grid[row].length - 1){
            check(grid, row, column + 1);
        }
        if(row < grid.length - 1){
            check(grid, row + 1, column);
        }
        if(row >  0){
            check(grid, row - 1, column);
        }
        return 1;
    }
    return 0;
}
public boolean flip(char[][] grid,int row, int column){
    if(grid[row][column] == '1'){
        grid[row][column] = '0';
        return true;
    }
    return false;
}