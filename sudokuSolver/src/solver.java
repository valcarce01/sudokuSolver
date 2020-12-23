import java.util.*;


public class solver {
    // Solves simple sudoku
    public static int[] get_sudoku(){
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




    public static void main(String[] args) {
        graph g = new graph();
        g.specify(); // creates the matrix for the sudoku
        map map_object = new map();
        map_object.create_map(get_sudoku());

        System.out.println(map_object.dictionary.toString());
        // Now we need to remove applying the coloring strategy
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
            System.out.println(continue_);
        }
        /*
        for (int i = 0; i < 81; i++){
            List<Integer> values = map_object.get_value(i);
            if (values.size() == 1){
                List<Integer> pointer = g.points_to(i);
                // In this case, we can remove the value
                for (int p:pointer){
                    map_object.remove_value(p, values.get(0));
                }
            }
        }
         */
        System.out.println(map_object.dictionary.toString());



    }

}
