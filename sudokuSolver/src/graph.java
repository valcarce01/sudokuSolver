import java.util.*;

public class graph {
    // Implementation of an undirected graph for sudoku solving
    // Will work with its adjacency matrix and a dictionary
    private boolean adjMatrix[][] = new boolean[81][81];

    public void add_vertex(int i, int j){
        adjMatrix[i][j] = true;
        adjMatrix[j][i] = true;
    }
    public void remove_vertex(int i, int j){
        adjMatrix[i][j] = false;
        adjMatrix[j][i] = false;
    }

    // Now specify for a sudoku (true stands for values that can not have the same value)
    private void specify(){
        // We need to 'join' columns, rows and blocks
        for (int i = 0; i < 81; i++){
            // System.out.println(i);
            int row_cell = i / 9;
            int col_cell = i % 9;
            //System.out.printf("%d %d\n", row_cell, col_cell);



            int min_multiple = (i )/9 * 9 + 9;
            // System.out.println(min_multiple);
            // We select the rows
            for (int aux = i; aux < min_multiple; aux++){ // if starts in i more efficient (rather than min - 9)
                add_vertex(i, aux);
            }
            // Now the columns
            for (int aux = i; aux < 81; aux += 9){
                add_vertex(i, aux);
            }
        }
        // Now the blocks
        for (int r = 0; r < 81; r += 27){
            for (int c = r; c < r + 9; c += 3){
                System.out.printf("%d %d\n", r, c);
                List<Integer> to_permute = new ArrayList<Integer>();
                for (int aux_row = c; aux_row < c + 27; aux_row+=9){
                    for (int aux_col = aux_row; aux_col < aux_row + 3; aux_col++){
                        to_permute.add(aux_col);
                    }
                }
                System.out.println(to_permute.toString());
                // Now we need to add the combinations of the permute list to the graph
                for (int i:to_permute){
                    for (int aux = to_permute.indexOf(i); aux < to_permute.size(); aux++){
                        add_vertex(i, to_permute.get(aux)); // add to the graph
                    }
                }
            }
        }
    }
    // Adjacency matrix created







    public static void main(String[] args) {
        graph g = new graph();
        g.specify();
        System.out.println(Arrays.deepToString(g.adjMatrix));
        System.out.println(g.adjMatrix[50][80]); // DE REVENS
    }
}
