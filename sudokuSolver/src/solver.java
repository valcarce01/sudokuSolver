import java.util.*;


public class solver {
    // Solves simple sudoku
    public static int[] get_sudoku(){
        int[] sudoku = {0, 0, 1, 3, 7, 8, 0, 0, 9,
                3, 2, 0, 9, 0, 0, 0, 5, 0,
                9, 7, 4, 1, 0, 2, 6, 3, 0,
                0, 1, 6, 0, 8, 0, 0, 0, 0,
                7, 9, 0, 0, 0, 0, 0, 8, 5,
                0, 0, 0, 0, 3, 0, 1, 9, 0,
                0, 6, 9, 4, 0, 3, 8, 7, 2,
                8, 4, 0, 0, 0, 7, 5, 1, 3,
                1, 0, 0, 8, 2, 5, 9, 0, 0};
        return sudoku;
    }

    public static boolean check_win(Map<Integer, List<Integer>> dict){
        // Checks whether the sudoku is solved or not
        Iterator<Map.Entry<Integer, List<Integer>>> it = dict.entrySet().iterator();
        boolean result = true;
        while (it.hasNext()){
            Map.Entry<Integer, List<Integer>> pair = (Map.Entry<Integer, List<Integer>>) it.next();
            result = result && pair.getValue().size() == 1;
            it.remove();
        }
        return result;
    }

    public static void graph_solve(map map_object, graph g){
        int removed_values = 0;
        int added = 0;
        boolean continue_ = true;
        while (continue_){
            // map aux_dic = (map)((map)map_object.dictionary).clone();
            Map aux_dict = new HashMap<>(map_object.dictionary);
            for (int i = 0; i < 81; i++){
                List<Integer> values = map_object.get_value(i);
                if (values.size() == 1){
                    List<Integer> pointer = g.points_to(i);
                    // In this case, we can remove the value
                    for (int p:pointer){
                        added += map_object.remove_value(p, values.get(0));
                    }
                }
            }
            continue_ = removed_values + added > removed_values;
            removed_values += added;
            added = 0;
        }
    }


    public static void main(String[] args) {
        graph g = new graph();
        g.specify(); // creates the matrix for the sudoku
        map map_object = new map();
        map_object.create_map(get_sudoku());

        System.out.println(map_object.dictionary.toString());
        graph_solve(map_object, g);

        System.out.println(map_object.dictionary.toString());
        System.out.println(check_win(map_object.dictionary));
        // Now depending in whether we just won (more usual for ez games) we need to
        // decide what to do
        if (check_win(map_object.dictionary)){
            // End of the game
        }else{
            // We need to approach it in another way.
            // One easy way would be to check the existence of pairs, triples and beyond.
            // After that we will need to play the b+ tree structure
            // be checking
        }
    }




}
