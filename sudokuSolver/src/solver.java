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

    public static void pairs(map map_object, graph g){
        // If 2 numbers are only available in 2 cells, all the other numbers
        // can't go there
        for (int i = 0; i < 81; i++){
            List<Integer> aux = map_object.dictionary.get(i);

            if (aux.size() == 2){
                // lets check if there is another aux list with the same structure
                List<Integer> pointer = g.points_to(i);
                int number_of_equals = 0;
                int actual_pair = 0;
                for (int p:pointer){
                    List<Integer> values = map_object.dictionary.get(p);
                    if (values.equals(aux)){
                        // they have the same values
                        number_of_equals += 1;
                        actual_pair = p;
                    }
                }
                if (number_of_equals == 1){
                    // We can remove the values of the pair to all the pointers (except themselves)
                    // System.out.printf("%d %d\n", i, actual_pair);
                    for (int p:pointer){
                        // we can remove to all the pointing keys except the actual pair and i
                        if (p != actual_pair && p != i){
                            // all the values
                            for (int to_remove:aux){
                                map_object.remove_value(p, to_remove);
                            }
                        }
                    }
                }
            }
        }
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
            pairs(map_object, g);
            System.out.println("\n");
            print_dict(map_object);
            graph_solve(map_object, g);
            System.out.println(check_win(map_object.dictionary));

        }
    }




}
