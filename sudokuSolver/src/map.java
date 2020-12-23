import java.util.*;

public class map {
    Map<Integer, List<Integer>> dictionary = new HashMap<>();

    public void create_map(int[] sudoku){
        // Now fill the object
        for (int idx = 0; idx < 81; idx++){
            List<Integer> aux_list = new ArrayList<>();
            if (sudoku[idx] != 0){
                // we actually now what the value is
                aux_list.add(sudoku[idx]);
            }else{
                // we need to put all posibble values
                for (int aux = 1; aux < 10; aux++){
                    aux_list.add(aux);
                }
            }
            dictionary.put(idx, aux_list);
        }
    }

    public int remove_value(int key, int value){
        // Removes a value of a given key
        // First get the values
        List<Integer> values = dictionary.get(key);
        int aux1 = values.size();
        values.removeAll(Arrays.asList(value));
        // values.remove(value);
        // Introduce into the dict
        dictionary.put(key, values);
        return aux1 - values.size();
    }

    public List<Integer> get_value(int from){
        //
        return dictionary.get(from);
    }


    public static void main(String[] args) {
        map m = new map();
        int[] sudoku = {5, 3, 0, 0, 7, 0, 0, 0, 0,
                6, 0, 0, 1, 9, 5, 0, 0, 0,
                0, 9, 8, 0, 0, 0, 0, 6, 0,
                8, 0, 0, 0, 6, 0, 0, 0, 3,
                4, 0, 0, 8, 0, 3, 0, 0, 1,
                7, 0, 0, 0, 2, 0, 0, 0, 6,
                0, 6, 0, 0, 0, 0, 2, 8, 0,
                0, 0, 0, 4, 1, 9, 0, 0, 5,
                0, 0, 0, 0, 8, 0, 0, 7, 9};
        m.create_map(sudoku);
        m.remove_value(0, 189);
    }
}
















