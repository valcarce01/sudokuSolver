import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class solver {
    // comentario


    public static int[] s(){
        int[] sudoku = {5, 3, 0, 0, 7, 0, 0, 0, 0,
                6, 0, 0, 1, 9, 5, 0, 0, 0,
                0, 9, 8, 0, 0, 0, 0, 6, 0,
                8, 0, 0, 0, 6, 0, 0, 0, 3,
                4, 0, 0, 8, 0, 3, 0, 0, 1,
                7, 0, 0, 0, 2, 0, 0, 0, 6,
                0, 6, 0, 0, 0, 0, 2, 8, 0,
                0, 0, 0, 4, 1, 9, 0, 0, 5,
                0, 0, 0, 0, 8, 0, 0, 7, 9};
        return sudoku;
    }

    private void permute(int[] l){
        // Create permutations given a list
        List<List> result;
        Arrays a = Arrays.asList(l);
        
        for (int i:l){
            int idx = Arrays.asList(l).indexOf(i);
            for (int j:){

            }
        }
    }

    private void create_graph(){
        /* Creates the graph containing the rules*/
        grafo_no_dirigido graph = new grafo_no_dirigido();

        // Let's create the array of the indices of the sudoku
        int[][] sudoku_positions = new int[9][9];
        for (int i = 0; i < 81; i++){
            System.out.println(i);
            int row = i / 9;
            int col = i % 9;
            sudoku_positions[row][col] = i + 1;
        }
        System.out.println(Arrays.deepToString(sudoku_positions));

        // Now we need to create the rules
        // First the rows
        for (int[] row:sudoku_positions){

        }
    }


    public static void main(String[] args) {
        System.out.println(s().toString());

        solver s = new solver();
        s.create_graph();
    }

}
