# INF05010-Otimizacao-Combinatoria

- Meta-heurística e relatório preliminar:
  - (a) Um código-fonte e um relatório em formato PDF.
  - (b) O código-fonte pode estar em qualquer linguagem mas deve possuir instruções claras para compilação/execução em Linux.
  - (c) O ‘programa’ se refere a execução do código-fonte interpretado ou a execução do binário compilado a partir do código-fonte.
  - (d) O programa deve receber a sua entrada por meio de parâmetros posicionais da linha de comando na seguinte ordem: (i) o caminho até o arquivo de entrada (incluíndo seu nome); (ii) um valor que controla o critério de parada escolhido (e.g., iterações por elemento do arquivo de entrada); (iii) a semente de aleatóriedade (se a heurística é não-deterministica) ou o parâmetro escolhido para variação (se a heurística é deterministica). A partir da quarta posição, ou por meio de flags/opções, os alunos podem passar quaisquer outros parâmetros opcionais que eles queiram.
  - (e) Após a geração da solução inicial, e toda a vez que o programa encontra uma solução melhor que a melhor conhecida até o momento, esta deve escrever na saída padrão: (i) a quantidade de 
 segundos (com duas casas após a vírgula) desde o começo da execução; (ii) o valor dessa soluão; (iii) uma representação da mesma que seja possível de ser compreendida por um ser humano. Além disso, a implementação também deve escrever na saída padrão quaisquer outras informções usadas para montagem das tabelas do relatório preliminar.
  - (f) O programa deve executar de forma determinística. Ou seja, dadas as exatas mesmas entradas, ele precisa retornar os mesmos resultados, independente da m´aquina utilizada. Dessa forma, o parâmetro indicando o critério de parada NAO PODE SER TEMPO. Os experimentos exigem rodar o código por “cerca de” 5s e 300s por´em o recomendado ´e que o aluno codifique um controle que escreva no terminal o número da primeira iteração após 5s de execução (e o mesmo para 300s), e então adote esses números como parâmetos de critério de parada para os experimentos do trabalho.
  - (g) O código deve implementar a meta-heurística escolhida. Cada meta-heurística tem lacunas que variam com o problema e decisõess de implementação que ficam a critério dos alunos, mas também
tem partes que caracterizam ela como aquela meta-heurística (estas precisam estar presentes no código).
  - (h) São critérios de avaliação da implementação da meta-heurística:
    - i. a sua corretude (e.g., n˜ao retorna soluções inválidas),
    - ii. a sua legibilidade (e.g., organização, nomes, e comentários),
    - iii. a adequação a meta-heurística escolhida (como explicado acima),
    - iv. e a sua performance (especialmente no que tange a escolha de representação da solução e como esta é alterada, a exagerada criação novos objetos de solução ao invés de sua alteração, e o recálculo do valor da função objetivo do a partir zero ao invés de por delta).
  - (i) A versão do código-fonte entregue deve ser exatamente a mesma utilizada para a escrita do relatório preliminar entregue.
  - (j) O relatório preliminar deve possuir no máximo 4 páginas e no mínimo fonte de tamanho 12.
  - (k) O relatório preliminar deve possuir uma descrição clara e completa da implementação:
    - i. Escolha de representação do problema.
    - ii. Construção da solução inicial.
    - iii. Principais estruturas de dados.
    - iv. Vizinhançaa e a estratégia de escolha de vizinhos (quando aplicável).
    - v. Processo de recombinação e factibilização (quando aplicável).
    - vi. Parâmetros do método (valores usados nos experimentos).
    - vii. Critério de parada (NâO pode ser diretamente tempo).
  - (l) Comparações preliminares: Com a intenção de apresentar a versão da sua meta-heurística com os melhores resultados possíveis, é esperado que os alunos variem e testem diferentes valores para os diferentes parâmetros. Essa experimentação pode ser exploratória e não envolver um método sistemático mas, ao invés disso, uma breve justificativa deve ser dada para porque se escolheu os valores para cada parâmetro da meta-heurística. No relatório final, os parâmetros terâo valores fixados baseado no que foi considerado melhor durante essa análise preliminar (com exceção dos métodos completamente determinísticos que ainda variarão o parâmetro considerado de maior impacto por esses experimentos dentro de um intervalo também justificado por esses experimentos).
  - (m) Execuções mínimas: Embora os experimentos sejam exploratórios, é necessário que o aluno apresente uma tabela com todos os parâmetros de entrada e o valor da função objetivo retornado para, pelo menos, uma run para cada instância (para permitir ao professor aferir que o código realmente funciona como esperado).
