# TSP-With-restrictions
A variation of the famous TSP problem with order restrictions.<br/>
Code grade at UFPR: 100<br/>
run try2.py to execute<br/>

texto.pdf: specification and resolution of the problem<br/>

boundFunc1.py: fornece as duas funções de bound, além das ferramentas wrongOrder e cost.<br/>
inputs.py: utilizado para gerar entradas aleatórias para o problema (uso opcional)<br/>
OrderAux.py: utilizado para encerrar o programa quando há duas restrições de ordem opostas, ex: [3,2] e [2,3] (uso opcinal)<br/>
readData.py: utilizado para ler a entrada do stdin<br/>
try2.py: o "main" do programa<br/>
TSP0.py: primeira versão do programa (maior confiabilidade), utilizado para verificar as respostas das versões posteriores (uso opcional)<br/>
TSP1.py: segundo versão do programa (uso opcional)<br/>
TSP2.py: terceira versão do programa, utiliza Branch and Bound<br/>
TSP2comp.py: versão para comparar número de nodos ao utilizar bound1 e bound2 (uso opcinal)<br/>

*****IMPORTANTE****** <br/>
Caso o problema não tenha solução o custo ótimo encontrado será igual a inf (infinito). Tal custo será impresso na saída padrão STDOUT<br/>
No subdiretório "exemplos" há os exemplos usados pelo autor<br/>

Fernando Zanutto
