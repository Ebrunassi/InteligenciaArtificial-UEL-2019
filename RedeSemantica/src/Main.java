import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Dictionary;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.Scanner;


public class Main {
	
	public static boolean achou = false;
	public static int rela = 0;
	public static int limite = 24;
	public static String relacaoChave = null;
	public static boolean ativaRelacaoChave = false;
	public static boolean ativaE_um = false;
	
	public static int tem = 0;
	public static String relacao = null;
	
	private static void printGraph(Grafo graph)	{
		int src = 0;
		int n = graph.adj.size();

		while (src < n)	{
			// print current vertex and all its neighboring vertices
			for (String dest : graph.adj.get(src)) {
//				System.out.println("(" + graph.adj.get(src).);
				System.out.print("(" + src + " --> " + dest + ")\t");
			}					
			System.out.println();
			src++;
		}
	}
	private static void verificaDicionario(Map<String, Integer> dictionary, int cont, String s1) {
		Set<Entry<String, Integer>> entries = dictionary.entrySet();
        Iterator<Entry<String, Integer>> iter = entries.iterator();
         
        while(iter.hasNext()) {
            Entry<?, ?> entry = iter.next();
            if(s1.equals(entry.getKey()) == false) {
            	dictionary.put(s1, cont);
            }
//            System.out.println(entry.getKey() + ": " + entry.getValue());
            return;
        }
        
        dictionary.put(s1, cont);
	}
	private static void printaDicionario(Map<String, Integer> dictionary) {
		Set<Entry<String, Integer>> entries = dictionary.entrySet();
        Iterator<Entry<String, Integer>> iter = entries.iterator();
         
        while(iter.hasNext()) {
            Entry<?, ?> entry = iter.next();
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
	}
	
	public static int trataLinha(String linha, List<Aresta> arestas,Map<String, Integer> dictionary,int cont) {
		String s1,s2,s3;
		String[] textoSeparado = linha.split(" ");
		 
		Arrays.toString(textoSeparado);
		s1 = textoSeparado[0];
		s2 = textoSeparado[1];
		s3 = textoSeparado[2];
		
		cont = cont + 1;
		Tupla t1 = new Tupla(s1,cont); 	
		verificaDicionario(dictionary,cont,s1);

		cont = cont + 1;
		Tupla t2= new Tupla(s3,cont); 	
//		verificaDicionario(dictionary,cont,s3);
		
		Aresta a1 = new Aresta(t1,t2,s2);
		arestas.add(a1);
		
		return cont;
	}
	
	public static String[] trataAfirmacao(String afirmacao) {
		String[] textoSeparado = afirmacao.split(" ");
		Arrays.toString(textoSeparado);		
		return textoSeparado;
	}
	
	public static void recursao_e_um(String palavra, String comparacao, Map<String, Integer> dictionary, Grafo graph){
		int i = graph.getKey(palavra, dictionary);			// Dado o 'destino' do nó do grafo, pega o índice do grafo
//		System.out.println(palavra + "-------<");
		
		if (i == -1)										// Verifica se o índice existe
			return;

		List<List<String>> list = graph.getAdj();
		List<String> list2 = list.get(i);					// Pega a lista deste índice
		
		for(int j = 0 ; j < list2.size(); j ++) {			// Vamos percorrer a lista inteira!
			String[] vasilha = list2.get(j).split(" ");		// Separamos o conteúdo do nó dessa lista em (relacao,destino) cada nó
			Arrays.toString(vasilha);
			System.out.println("- " + vasilha[1]);
															// Verifica se os destinos e as relações são iguais
			if("e_um".equals(vasilha[0]) == true && comparacao.equals(vasilha[1]) == true) {
				System.out.println("Achou!");
				achou = true;								// Achou = true , e volta a recursão
				return;										// Verifica se o destino é igual, porém a relação não
			}
//			else if("e_um".equals(vasilha[0]) == false && comparacao.equals(vasilha[1]) == true){
//				System.out.println("oraororaora");
//				achou = false;								// Se não for, achou = false
//				j++;
//				return;			
//			}
			else if("e_um".equals(vasilha[0]) == false) {
				return;
			}else {
				if( j < list2.size()) {						// Se a lista não acabou, chama essa função recursivamente
					recursao_e_um(vasilha[1],comparacao,dictionary,graph);
				}
			}
			
		}
		
	}
	public static void recursao_tem(String palavra, String comparacao, Map<String, Integer> dictionary, Grafo graph){
		int i = graph.getKey(palavra, dictionary);				// Pega o índice no grafo da palava destino
		if (i == -1 ) {						// Verifica se o índice existe
			rela = 0;
			if(( (tem >= 0 && "tem".equals(palavra) == true) || ( tem > 0 && "e_um".equals(palavra) == true ))&& comparacao.equals(palavra) == true) {
				System.out.println("Achou!");
				achou = true;
			}
			return;
		}
		
//		if (i == -1 || rela >= limite) {						// Verifica se o índice existe
//			System.out.println("vai derrubar : "+ palavra);
//			rela = 0;
//			return;
//		}
		
		List<List<String>> list = graph.getAdj();
		List<String> list2 = list.get(i);						// Vamos pegar a lista deste índice

		for(int j = 0 ; j < list2.size(); j ++) {				// Vamos percorrer a lista inteira!
			String[] vasilha = list2.get(j).split(" ");			// Separa o conteúdo do nó do grafo em (relacao,destino)
			Arrays.toString(vasilha);
			
			if ("tem".equals(vasilha[0]) == true)				// Se a relacao == tem , tem++
				tem++;
		
			System.out.println("- " +vasilha[1]);
																
			if(((tem >= 1 /* tem > 0*/  && ("e_um".equals(vasilha[0]) == true || "tem".equals(vasilha[0]) == true)	)	) 
															&& comparacao.equals(vasilha[1]) == true) {
				System.out.println("Achou!");
				achou = true;
				return;
			}else if("e_um".equals(vasilha[0]) == false && "tem".equals(vasilha[0]) == false){
//				j++;
			}else {
				if( j < list2.size()) {
					recursao_tem(vasilha[1],comparacao,dictionary,graph);
				}
			}
			
		}
	
		
	}
	public static void recursao_relacao(String palavra, String comparacao, Map<String, Integer> dictionary, Grafo graph){
		int i = graph.getKey(palavra, dictionary);				// Pega o índice no grafo da palava destino
		if (i == -1 || rela >= limite) {						// Verifica se o índice existe
			rela = 0;
			if(( (tem == 1 && "tem".equals(palavra)==false) || ( tem == 1 && "e_um".equals(palavra) == true ))&& comparacao.equals(palavra) == true) {
				System.out.println("Achou!");
				achou = true;
			}
			return;
		}
		List<List<String>> list = graph.getAdj();
		List<String> list2 = list.get(i);						// Vamos pegar a lista deste índice

		for(int j = 0 ; j < list2.size(); j ++) {				// Vamos percorrer a lista inteira!
			String[] vasilha = list2.get(j).split(" ");			// Separa o conteúdo do nó do grafo em (relacao,destino)
			Arrays.toString(vasilha);
			
			if (relacao.equals(vasilha[0]) == true) {			// Se a relacao == tem , tem++
				tem++;
			}
		
			System.out.println("- "+vasilha[1]);
			if("tem".equals(vasilha[0])==false && "e_um".equals(vasilha[0])==false && relacao.equals(vasilha[0])==false)
				return;
																// Se a relacao ==
			if(( (tem == 1 && "tem".equals(vasilha[0])==false) || ( tem == 1 && "e_um".equals(vasilha[0]) == true ) )	&& comparacao.equals(vasilha[1]) == true) {
				System.out.println("Achou!");
				achou = true;
				return;
			}else if("e_um".equals(vasilha[0]) == false && "tem".equals(vasilha[0]) == true){
//				j++;
//				tem = 0;
//				return;
			}else {
				if( j < list2.size()) {
					recursao_relacao(vasilha[1],comparacao,dictionary,graph);
				}
			}
			
		}
	
		
	}
	public static void verificaRecursao(String palavra, String comparacao, Map<String, Integer> dictionary, Grafo graph) {
		int i = graph.getKey(palavra, dictionary);
		if (i == -1 || rela >= limite) {
			rela = 0;
			return;
		}
		List<List<String>> list = graph.getAdj();
		List<String> list2 = list.get(i);
		
		System.out.println("--> " + palavra + ": " + i);
		
		for(int j = 0 ; j < list2.size(); j ++) {		
			String[] vasilha = list2.get(j).split(" ");
			Arrays.toString(vasilha);
			
			if(ativaE_um == true && vasilha[0].equals("e_um") == false)
				return;
			
			if(vasilha[0].equals("e_um") == false && vasilha[0].equals("tem") == false 
											&& ativaRelacaoChave == true) {
				
				System.out.println("1.");
				rela++;
				relacaoChave = vasilha[0];
				ativaRelacaoChave = true;
//				System.out.println("rela : " + rela);
				if(rela >= limite)
					return;
				
				achou = false;
				return;
			}
			
//			 System.out.println(vasilha[1]);
			if(comparacao.equals(vasilha[1])) {
				System.out.println("2.");
				achou = true;
				return;
			}else {
//				System.out.println("j : " + j + "size : " + list2.size());
				if( j < list2.size()) {
					verificaRecursao(vasilha[1],comparacao,dictionary,graph);
				}
			}
		}
	}
	
	public static void verificaGrafo(String[] afirmacao,Map<String, Integer> dictionary, Grafo graph) {
		
		// SUJEITO relacao DESTINO
		int i = graph.getKey(afirmacao[0], dictionary);		// Pega o índice do grafo do SUJEITO
		System.out.println(" -- " + afirmacao[0] + " -- ");
		if(i == -1 || rela >= limite)						// Verifica se o índice existe
			return;
		List<List<String>> list = graph.getAdj();			//	Pega o grafo
		List<String> list2 = list.get(i);					// Peguei a lista correspondente do sujeito
		relacao = afirmacao[1];
		
		for(int j = 0 ; j < list2.size(); j++) {			// Vamos percorrer essa lista inteira!
			String[] vasilha = list2.get(j).split(" ");		// Separamos o conteúdo de cada elemento da lista (e_um atacante,   tem chuteira, etc...)
			Arrays.toString(vasilha);

/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
			if(afirmacao[1].equals("e_um") == true) {		// Verifica se a 'relacao' == 'e_um'
															// verifica se o 'destino' == DESTINO dado pelo usuário
				if(afirmacao[2].equals(vasilha[1]) == true && vasilha[0].equals("e_um") == true) {
					System.out.println ("Achou!");
					achou = true;							// VERDADE : achou = true 					
				}else if(vasilha[0].equals("e_um") == true) {										// FALSO : entra na recursão, passando o 'destino' como parâmetro
					System.out.println("--- " + vasilha[1]);
					recursao_e_um(vasilha[1], afirmacao[2], dictionary, graph);
				}
				
/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
															// Verifica se a 'relacao' == 'tem'
			}else if(afirmacao[1].equals("e_um") == false && afirmacao[1].equals("tem") == true) {
				tem = 0;									// tem = 0
															// Verifica se já achou a palavra
				if(afirmacao[2].equals(vasilha[1]) && "tem".equals(vasilha[0]) == true) {
					System.out.println("Achou!");
					achou = true;							// VERDADE : achou = true
				}else if(vasilha[0].equals("tem") == true || vasilha[0].equals("e_um") == true){	// FALSO : entra na recursão passando o destino como parâmetro
					System.out.println("--- " + vasilha[1]);
					recursao_tem(vasilha[1], afirmacao[2], dictionary, graph);					
				}
/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/				
			}else if(afirmacao[1].equals("e_um") == false && afirmacao[1].equals("tem") == false) {
//				tem = 0;				
//				relacao = afirmacao[1];
				
				// Verifica se já achou a palavra
				System.out.println("--- " + vasilha[1]);
				if(afirmacao[2].equals(vasilha[1]) && relacao.equals(vasilha[0]) == true) {
					System.out.println("Achou!");
					achou = true;							// VERDADE : achou = true
				}else if(vasilha[0].equals(relacao) == true || vasilha[0].equals("e_um") == true){	// FALSO : entra na recursão passando o destino como parâmetro
					recursao_relacao(vasilha[1], afirmacao[2], dictionary, graph);					
				}
			}
			
		}
		
		
		
//		
//		if(afirmacao[1].equals("e_um") == true)
//			ativaE_um = true;
//		
//		if(afirmacao[1].equals("e_um") == false && afirmacao[1].equals("tem") == false) {
//			limite = 2;
//			relacaoChave = afirmacao[1];
//			ativaRelacaoChave = true;
//		}
//		
//			 for(int j = 0 ; j < list2.size(); j ++) {
//				 String[] vasilha = list2.get(j).split(" ");
//				 Arrays.toString(vasilha);
//				 System.out.println("verifica grafo - " + vasilha[1]);
//				
//				 rela = 0;
//				 
//				 if(vasilha[0].equals("e_um") == false && vasilha[0].equals("tem") == false) {
//					 rela++;
////					 System.out.println("rela : " + rela);					 
//				 }
//				 
//				 if(afirmacao[2].equals(vasilha[1])) {
//					 	if(ativaRelacaoChave == false)
//					 		achou = true;
//						return;
//					}else {
//						if(j < list2.size())
//							verificaRecursao(vasilha[1], afirmacao[2], dictionary, graph);
//					}
//			 }


	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new FileReader("C:\\Users\\ebrun\\Documents\\arquivo.txt"));
		String linha;
		final List<Aresta> arestas = new LinkedList<Aresta>(); 
		int cont = -1;
		Map<String, Integer> dictionary = new HashMap<String, Integer>();
		Scanner sc = new Scanner(System.in);
		
		while ((linha = br.readLine()) != null) {
//		    System.out.println(linha);     //Printa a linha do arquivo
		    cont = trataLinha(linha,arestas,dictionary,cont);
		}
        
		Aresta a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21;
		Aresta a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34;
		a1 = arestas.get(0);
		a2 = arestas.get(1);
		a3 = arestas.get(2);
		a4 = arestas.get(3);
		a5 = arestas.get(4);
		a6 = arestas.get(5);
		a7 = arestas.get(6);
		a8 = arestas.get(7);
		a9 = arestas.get(8);
		a10 = arestas.get(9);
		a11= arestas.get(10);
		a12= arestas.get(11);
		a13= arestas.get(12);
		a14= arestas.get(13);
		a15= arestas.get(14);
		a16= arestas.get(15);
		a17= arestas.get(16);
		a18= arestas.get(17);
		a19= arestas.get(18);
		a20= arestas.get(19);
		a21= arestas.get(20);
		a22= arestas.get(21);
		a23= arestas.get(22);
		a24= arestas.get(23);
		a25= arestas.get(24);
		a26= arestas.get(25);
		a27= arestas.get(26);
		a28= arestas.get(27);
		a29= arestas.get(28);
		a30= arestas.get(29);
		a31= arestas.get(30);
		a32= arestas.get(31);
//		a33= arestas.get(32);
//		a34 = arestas.get(33);
		

		
		List<Aresta> edges = Arrays.asList(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32);		
		
		Grafo graph = new Grafo(edges,dictionary);
		
		printaDicionario(dictionary);       
		printGraph(graph);					
		while(true) {
			String afirmacao = sc.nextLine();
			String[] ar = trataAfirmacao(afirmacao);
			
			int i = graph.getKey(ar[0],dictionary);
//			System.out.println(i);
			verificaGrafo(ar,dictionary,graph);
			if(achou == true) {
				System.out.println("verdadeiro");
			}else {
				System.out.println("falso");
			}
			achou = false;
			rela = 0;
			limite = 2;
			relacao = null;
			tem = 0;
		}
					
		
	}

}
