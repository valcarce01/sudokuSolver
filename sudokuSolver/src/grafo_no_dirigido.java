import java.util.*;

public class grafo_no_dirigido {
    // Create an empty dictionary
    Map<String, List> dictionary = new HashMap<>();


    private void _add_vertex(String from, String to){
        // Adds a vertex to the graph
        List<String> add;
        if (dictionary.containsKey(from)) {
            add = dictionary.get(from);
        }else {
            add = new ArrayList<String>();
        }
        if (!add.contains(to)){
            add.add(to);
            dictionary.put(from, add);
        }
    }

    public void add_vertex(String from, String to){
        // Adds a vertex to the graph in both directions
        _add_vertex(from, to);
        _add_vertex(to, from);
    }


    public void remove_vertex(String from, String to){
        // Removes in both direction
        _remove_vertex(from, to);
        _remove_vertex(to, from);
    }

    private void _remove_vertex(String from, String to){
        // Removes vertex
        List<String> to_remove = dictionary.get(from);
        if (to_remove.size() == 1 && to_remove.contains(to)){ // we can remove the node
            dictionary.remove(from);
        }else{
            to_remove.remove(to);
            dictionary.put(from, to_remove);
        }
    }

    public int degree(String node){
        // Returns degree of a given node, as is non directed, we can
        // actually check the outbound vertices
        return dictionary.get(node).size();
    }


    public static void main(String[] args) {
        grafo_no_dirigido g = new grafo_no_dirigido();

        g.add_vertex("de", "a");
        g.add_vertex("de", "b");

        g.add_vertex("xd", "b");
        g.add_vertex("xd", "b");
        System.out.println(g.dictionary.toString());
        // g.forEach((key, value) -> System.out.println(key + ":" + value));
        g.remove_vertex("de", "a");
        System.out.println(g.dictionary.toString());

        System.out.println(g.degree("de"));

    }
}