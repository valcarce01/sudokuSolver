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
        int[] sudoku2 = {
                4, 6, 0, 0, 9, 0, 0, 0, 0,
                0, 5, 2, 1, 0, 0, 0, 9, 0,
                0, 0, 0, 2, 3, 0, 5, 0, 0,
                8, 0, 0, 0, 0, 0, 0, 0, 7,
                0, 0, 0, 0, 2, 0, 0, 0, 8,
                3, 0, 0, 0, 0, 0, 0, 0, 9,
                0, 0, 0, 5, 1, 0, 8, 0, 0,
                0, 7, 8, 6, 0, 0, 0, 2, 0,
                6, 1, 0, 0, 8, 0, 0, 0, 0
        };
        return sudoku2;
    }

    public static boolean check_win(Map<Integer, List<Integer>> dict){
        // Checks whether the sudoku is solved or not
        Map aux_dict = new HashMap<>(dict);
        Iterator<Map.Entry<Integer, List<Integer>>> it = aux_dict.entrySet().iterator();
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
            for (int i = 0; i < 81; i++){
                List<Integer> values = map_object.get_value(i);
                if (values.size() == 1){
                    List<Integer> pointer = g.points_to(i);
                    // In this case, we can remove the value
                    for (int p:pointer){
                        if (!(map_object.dictionary.get(p).size() == 1)) {
                            added += map_object.remove_value(p, values.get(0));
                        }
                    }
                }
            }
            continue_ = removed_values + added > removed_values;
            removed_values += added;
            added = 0;
        }
    }

    public static void pairs(map map_object, graph g) {
        // If 2 numbers are only available in 2 cells, all the other numbers
        // can't go there
        boolean continue_ = true;
        int removed_values = 0;
        int added = 0;
        while (continue_) {
            for (int i = 0; i < 81; i++) {
                List<Integer> aux = map_object.dictionary.get(i);

                if (aux.size() == 2) {
                    // System.out.println(aux.toString());
                    // lets check if there is another aux list with the same structure
                    List<Integer> pointer = g.points_to(i);
                    int number_of_equals = 0;
                    int actual_pair = 0;
                    for (int p : pointer) {
                        List<Integer> values = map_object.dictionary.get(p);
                        if (values.equals(aux)) {
                            // they have the same values
                            number_of_equals += 1;
                            actual_pair = p;
                        }
                    }
                    if (number_of_equals == 1) {
                        print_dict(map_object);
                        System.out.println(aux);
                        // We can remove the values of the pair to all the pointers (except themselves)
                        // System.out.printf("%d %d\n", i, actual_pair);
                        //System.out.println(aux);
                        //System.out.print(i);
                        //System.out.print(actual_pair);
                        int difference = Math.abs(i - actual_pair);
                        if (difference < 9){
                            // they are in the same row, so we can remove them from the row and its blocks
                            // Get the row
                            int min_multiple = (i)/9 * 9 + 9; // max
                            for (int aux_row = min_multiple - 9; aux_row < min_multiple; aux_row++){
                                //System.out.print(aux_row);
                                // We can remove the values if they are not one of the pair members
                                if (aux_row != i && aux_row != actual_pair){
                                    //System.out.println(aux_row);
                                    // We can remove them
                                    for (int to_remove:aux){
                                        if (!(map_object.dictionary.get(aux_row).size() == 1)) {
                                            added += map_object.remove_value(aux_row, to_remove);
                                        }
                                    }
                                }
                            }
                        }else if(difference%9 == 0){
                            // they are in columns
                            for (int aux_col = 0; aux_col < 81; aux_col+=9){
                                if (aux_col != i && aux_col != actual_pair){
                                    // We can remove them
                                    for (int to_remove:aux){
                                        if (!(map_object.dictionary.get(aux_col).size() == 1)) {
                                            added += map_object.remove_value(aux_col, to_remove);
                                        }
                                    }
                                }
                            }
                        }
                        // Whatever it is, we can remove both of them from its respective blocks
                        // First check the position
                        int aux_row = i / 9; int aux_row_pair = actual_pair / 9;
                        int aux_col = i % 9; int aux_col_pair = actual_pair % 9;
                        // And now lets check the start of its block
                        int start_row = (aux_row) / 3 * 3;
                        int start_col = (aux_col) / 3 * 3;
                        //System.out.printf("\nPosición %d %d y auxiliar %d %d", aux_row, aux_col, aux_row_pair, aux_col_pair);
                        //System.out.printf("\n Bloque comienza en %d %d", start_row, start_col); //
                        // Now travel the block
                        for (int r = start_row; r < start_row + 3; r++){ // outside the columns
                            for (int c = start_col; c < start_col + 3; c++){
                                //System.out.printf("Position %d %d\n", r, c);
                                if ((r != aux_row || c != aux_col) &&
                                        (r != aux_row_pair || c != aux_col_pair)){
                                    //System.out.print("\nSe borra ");
                                    //System.out.print(r); System.out.print(c);
                                    for (int to_remove:aux){
                                        if (!(map_object.dictionary.get(r * 9 + c).size() == 1)) {
                                            added += map_object.remove_value(r * 9 + c, to_remove);
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            continue_ = removed_values + added > removed_values;
            removed_values += added;
            added = 0;
        }
    }

    public static boolean check_differences(Map dict1, Map dict2){
        // Checks whether 2 map objects have the same values or not
        boolean are_equal = true;
        for (int i = 0; i < 81; i++){
            are_equal = are_equal && (dict1.get(i).equals(dict2.get(i)));
        }
        return are_equal;
    }

    public static void print_dict(map map_object){
        // ez method for printing the values
        for (int i = 0; i < 81; i++){
            System.out.print(map_object.dictionary.get(i).toString());
            if ((i+1)%9 == 0){
                System.out.print("\n");
            }
        }
    }


    public static void main(String[] args) {
        // First we create the objects we will need in a future
        graph g = new graph();
        g.specify(); // creates the matrix for the sudoku
        map map_object = new map();
        map_object.create_map(get_sudoku());
        // we try first to solve it as a simple graph
        graph_solve(map_object, g);

        // System.out.println(map_object.dictionary.toString());
        print_dict(map_object);

        // Now depending in whether we just won (more usual for ez games) we need to
        // decide what to do
        boolean win = check_win(map_object.dictionary);
        // System.out.println(win);
        if (win){
            // End of the game
        }else{
            // We need to approach it in another way.
            // One easy way would be to check the existence of pairs, triples and beyond.
            // After that we will need to play the b+ tree structure
            // be checking
            // Apply the technics
            pairs(map_object, g);
            graph_solve(map_object, g);
            pairs(map_object, g);
            print_dict(map_object);
            graph_solve(map_object, g);
            // pairs(map_object, g);


            System.out.println("");
            print_dict(map_object);
            /*
            System.out.println("\n");
            print_dict(map_object);
            pairs(map_object, g);
            System.out.println("\n");
            print_dict(map_object);
            pairs(map_object, g);
            System.out.println("\n");
            print_dict(map_object);
            // graph_solve(map_object, g);
            System.out.println(check_win(map_object.dictionary));
             */
        }
    }




}
