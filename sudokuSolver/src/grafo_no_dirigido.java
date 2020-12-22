import java.util.*;

public class grafo_no_dirigido {
    // Create an empty dictionary
    Map<String, List> dictionary = new HashMap<>();

    public void add_vertex(String from, String to){
        // Adds a vertex to the graph
        List<String> add;
        if (dictionary.containsKey(from)) {
            add = dictionary.get(from);
        }else {
            add = new ArrayList<String>();
        }
        add.add(to);
        dictionary.put(from, add);
    }

    public void remove_vertex(String from, String to){
        // Removes vertex
        List<String> to_remove = dictionary.get(from);
        if (to_remove.size() == 1 && to_remove.contains(to)){ // we can remove the node
            dictionary.remove(from);
        }else{
            to_remove.remove(to);
            dictionary.put(from, to_remove);
        }
    }




    public static void main(String[] args) {
        grafo_no_dirigido g = new grafo_no_dirigido();
        List<String> b = new ArrayList<String>();
        b.add("a");
        b.add("b");
        g.add_vertex("de", "a");
        g.add_vertex("de", "b");

        g.add_vertex("pene", "b");
        System.out.println(g.dictionary.toString());
        // g.forEach((key, value) -> System.out.println(key + ":" + value));
        g.remove_vertex("de", "a");
        System.out.println(g.dictionary.toString());


    }

}