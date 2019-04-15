import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Map.Entry;


public class Grafo {
	
	
	List<List<String>> adj = new ArrayList<>();
	
	public int getKey(String valor, Map<String, Integer> dictionary) {


		Set<Entry<String, Integer>> entries = dictionary.entrySet();
        Iterator<Entry<String, Integer>> iter = entries.iterator();
	    int i = 0;
	        while(iter.hasNext()) {
	            Entry<?, ?> entry = iter.next();
	            if(valor.equals(entry.getKey()) == true) {
	            	return i;
	            }
	            i++;
	        }
	        return -1;		
	}
	
	public Grafo(List<Aresta> edges, Map<String, Integer> dictionary){
		
		for (int i = 0; i < edges.size()  ; i++)
			adj.add(i, new ArrayList<>());

		for (Aresta current : edges){
//			System.out.println(current.src.indice);
			int i = getKey(current.src.valor, dictionary);
//			adj.get(current.src.indice).add(current.dest.valor);
			adj.get(i).add(current.rel+ " " + current.dest.valor);
		}
	}
	
	public List<List<String>> getAdj() {
		return adj;
	}

	public void setAdj(List<List<String>> adj) {
		this.adj = adj;
	}

}
