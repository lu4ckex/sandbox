#GUIA BÁSICO DA PROGRAMAÇÃO EM PYTHON (SEGUINDO A METODOLOGIA DO LIVRO: PYTHON PARA TODOS - CHARLES SEVERANCE)

#"O PROGRAMADOR É O USUÁRIO FINAL DE SEUS PRÓPRIOS PROGRAMAS"

# PHASE-1

#ARQUITETURA DE HARDWARE DE COMPUTADORES
    """
    • CPU (Unidade de Processamento Central (Ou CPU): É a parte do computador que é construída para ser obcecada com a pergunta "E agora?".
    • RAM (Memória Principal):  Sendo memoria quase tão rápida quanto a CPU. Informações armazenadas nelas são temporárias, pois, somem após o desligamento da máquina.
    • ROM (Memória Secundária): É onde armazena as informações, é muito mais lenta que a memória principal. 
                                E a vantagem é que os dados podem ser guardados até quando o computador está desligado.
    • PÉRIFERICOS (Dispositivo de Entrada e Saída): Aqui é onde trás meios para a gente interagir com o computador.
        
        Obs: Conexão com Rede para receber informações vindas da rede. Podemos pensar nessa rede como um local muito devagar para armazenar e receber informação que nem sempre
            pode está a disposição. Essa rede é uma forma lenta e às vezes não confiável de Memória Secundária.
    
    O trabalho do programador é manusea esses recursos para resolver os problemas que você precisa análisa as informações obtidas da solução. Sendo assim, você
    deve escrever suas instruções antecidamente. Chamamos essas instruções de 'armazenadas de programa' e o ato de escrevê-las e garantir que estejam corretas de programar.
    """

#ENTENDENDO DE PROGRAMAÇÃO

    """
    A lógica da progrmação sempre será a mesma. Lembre-se disso. Então, se você aprender uma linguagem, logo você tem base e terá mais facilidade 
    para aprender as demais. Seja paciente quando estiver aprendendo a programar, pois é como aprender a ler pela primeira vez, no inicio é dificil, vai emperar um pouco. Porém
    na medida que for aprendendo e práticando, programar será um processo agradável e criativo.
    """

#UM POUCO SOBRE A GRAMÁTICA DO PYTHON

    """
    • Keywords (Palavras Reservadas): Palavras reservadas, ou keywords, são termos essenciais da sintaxe Python com 
    significados específicos, que não podem ser usados como nomes de 'variáveis, funções, ou classes'. Elas são fundamentais 
    para a estrutura e gramática do código Python.
        Exemplos: if, for, while, class.

    • Build in Fuctions (Função Integrada): Funções integradas, ou built-in functions, são funções fornecidas diretamente pela 
    linguagem Python, prontas para uso, sem a necessidade de importação de modulos. Elas realizam tarefas comuns, como conversões de tipo, 
    operações matemáticas e manipulação de coleções, facilitando a escrita de código eficiente e conciso.
        Exemplos: print(), len(), sum(), int().

    • Module Import (Importação de Modulos): A importação de módulos em Python é o processo de incluir código de outros arquivos (módulos) no seu programa, permitindo que 
    você reutilize funções, classes e variáveis definidas nesses módulos. Tem 3 opções de bibliotecas:

        ○ Módulos da Biblioteca Padrão:
            - Python vem com uma extensa biblioteca padrão que inclui muitos módulos prontos para uso.
                Exemplos:
                    math: Funções matemáticas básicas.
                    datetime: Manipulação de datas e horas.
                    os: Interação com o sistema operacional.
                    random: Geração de números aleatórios.
        ○ Módulos de Terceiros:
            - São módulos desenvolvidos pela comunidade ou por desenvolvedores terceiros que você pode instalar e usar em seus projetos.
                Exemplos:
                    numpy: Processamento de arrays e cálculos matemáticos avançados.
                    pandas: Manipulação e análise de dados.
                    requests: Realização de requisições HTTP.
                Para instalar módulos de terceiros, você geralmente usa o gerenciador de pacotes pip, como em: pip install requests
        ○ Módulos Personalizados:
            - São módulos que você mesmo cria para organizar e reutilizar o código dentro de seus próprios projetos.
            - Um módulo personalizado é simplesmente um arquivo Python (.py) com funções, classes, e variáveis que você quer 
            compartilhar entre diferentes partes do seu projeto.

    • Variavel (Variable): Em Python (e em outras linguagens de programação), uma variável é um nome que você dá a um espaço de memória onde um valor é armazenado. 
                        Você pode pensar em uma variável como um "rótulo" que aponta para um dado específico, como um número, uma string, uma lista, ou qualquer 
                        outro tipo de dado.
        Características de uma Variável:
            ○ Nomeação:
                O nome de uma variável deve começar com uma letra ou um sublinhado (_), seguido por letras, números ou sublinhados.
                    Exemplos válidos: idade, nome, saldo_conta, _variavel.
                    Exemplos inválidos: 2nome (não pode começar com número), nome-do-cliente (não pode conter hífen).
            ○ Atribuição de Valor:
                Para armazenar um valor em uma variável, você usa o operador de atribuição (=).
                    Exemplo: x = 10          # x agora é uma variável que contém o valor 10
                            nome = "Alice"   # nome agora é uma variável que contém a string "Alice"
                    Aqui, x e nome são variáveis, 10 e "Alice" são os valores atribuídos a essas variáveis.
            ○ Tipos de Dados:
                As variáveis em Python podem armazenar diferentes tipos de dados:
                    Inteiros (int): idade = 25
                    Números decimais (float): altura = 1.75
                    Strings (str): nome = "Carlos"
                    Listas (list): numeros = [1, 2, 3]
                    Dicionários (dict): dados = {"nome": "Alice", "idade": 30}
            ○ Mutabilidade:
                Em Python, variáveis podem ser reatribuídas com novos valores a qualquer momento:
                    x = 10
                    x = 20  # x agora contém o valor 20
            ○ Exemplo de uso das variáveis:
                # Atribuindo valores a variáveis
                    nome = "João"
                    idade = 30
                    altura = 1.75

                # Usando variáveis em operações
                    print(f"{nome} tem {idade} anos e mede {altura} metros.")
            ○ Funções das Variáveis:
                Armazenamento de Dados: Variáveis armazenam dados que serão usados mais tarde no programa.
                Manipulação de Dados: Você pode realizar operações matemáticas, concatenar strings, ou manipular coleções de dados através de variáveis.
                Legibilidade do Código: O uso de variáveis com nomes descritivos torna o código mais fácil de ler e entender.
    """
# TERMINOLOGIA: INTERPRETADOR E COMPILADOR
    """
    • High-Level Language (Linguagens de Alto Nível): É simples para um humano ler e escrever e para um computador ler e processar.
        Exemplos: Java, C++, PHP, Ruby, Basic, Perl, JavaScript.

    • Intermediate-Level language (Linguagem Intermédiaria)
        Essas linguagens oferecem um equilíbrio entre a abstração das linguagens de alto nível e o controle detalhado das linguagens de baixo nível.
            Um exemplo clássico de linguagem de médio nível é a C. A linguagem C é considerada de médio nível porque:\\
                Controle de Hardware: Permite acesso direto à memória e controle detalhado sobre o hardware, similar às linguagens de baixo nível.
                Abstração: Oferece abstrações e estruturas de controle de fluxo que são mais fáceis de usar e entender do que as linguagens de baixo nível.

    • Low-Level Language (Linguagem de Baixo Nível): Essas linguagens estão mais próximas do hardware e oferecem menos abstração em relação aos 
    detalhes da máquina. Elas são geralmente mais difíceis de usar e entender em comparação com linguagens de alto nível.
        Existem duas principais categorias de linguagens de baixo nível:
            ○ Linguagem de Montagem (Assembly Language): Uma linguagem de baixo nível que usa mnemônicos e símbolos para representar instruções de máquina, facilitando a programação 
            em um nível mais próximo ao hardware.
            ○ Linguagem de Máquina (Machine Language): O nível mais baixo de linguagem de programação, consistindo em códigos binários ou hexadecimais diretamente compreendidos pela CPU.
        Essas linguagens permitem um controle mais direto sobre o hardware e podem ser usadas para otimizar o desempenho de sistemas e aplicações.
    """

#ESCREVENDO UM PROGRAMA

    """
    - Escrever comando no Interpretador de Python é um excelente meio de experimentar os recursos da linguagem. Mas não é recomendado para resolução de problemas comlexos.
    - Quando vamos escrever um código, nós usamos um editor de texto (Notpad++, VSCode, ect) para escrever as instruções em Python em um arquivo, iso é 
    chamado de 'Script'. Os scripts em Python o formato de .py.
    - O $ é o prompt do sistema operacional.
    - A definição de um 'Programa' em seu básico é uma sequência de instruções do Python (Ou outras linguagens) que foram criadas para fazer algo.
    """

#A CONSTRUÇÃO DE BLOCOS DE PROGRAMAS
    """
    ♦   Entrada (input): Obter dados do "mundo externo". Nos nossos programas inicias, nossa entrada virá do usuário digitando dados em seu teclado.

    ♦   Saída (output): Mostra resultados de um programa na tela, ou guardá-los em um arquivo, ou talvez gravá-los em dispositivo como um alto falante, para que ele toque reproduza algo.

    ♦   Execução Sequencial (Sequential Execution): Esse termo refere-se à execução de instruções ou operações em uma ordem específica, uma após a outra, sem interrupção ou paralelismo. 
        Em programação, a execução sequencial é o modo padrão de operação, onde as instruções são processadas na ordem em que aparecem no código/script.

    ♦   Execução Condicional (Conditional Execution): Esse termo refere-se à execução de instruções que dependem de uma condição ou expressão lógica. Em outras palavras, o código é executado 
        apenas se uma determinada condição for verdadeira. Esse conceito é fundamental em estruturas de controle de fluxo, como if, else, switch, ou case nas linguagens de programação.
            Exemplo em Python: 
                if condition:
                    # Código a ser executado se a condição for verdadeira.
                else:
                    # Código a ser executado se a condição for falsa.
            Aqui, a execução do bloco de código dentro do if ou do else depende da avaliação da condição fornecida.

    ♦  Execução Repetitiva (Repetitive Execution): Esse termo refere-se à execução de um bloco de código várias vezes, geralmente até que uma condição seja satisfeita. Esse conceito é 
        implementado usando estruturas de loop, como for, while, ou do-while nas linguagens de programação.
            Exemplo em Python:
                for i in range(5):
                    print(i)
            Aqui, o bloco de código dentro do for será executado repetidamente enquanto a condição especificada no loop estiver sendo atendida, ou até que o loop alcance seu limite.

    ♦   Reuso (Code Reusability): Reusabilidade refere-se à prática de escrever código de forma que ele possa ser utilizado novamente em diferentes partes de um programa ou em diferentes 
        projetos sem precisar ser reescrito. Esse conceito é fundamental para aumentar a eficiência no desenvolvimento de software e melhorar a manutenção do código.
            Algumas formas de alcançar reusabilidade incluem:
                • Funções ou Métodos: Blocos de código que executam uma tarefa específica e podem ser chamados várias vezes com diferentes parâmetros.
                    Exemplo: 
                        def add(a, b):
                            return a + b
                • Bibliotecas e Módulos: Conjuntos de funções e classes agrupadas em arquivos que podem ser importados e reutilizados em diferentes projetos.
                    Exemplo:
                    import math
                        print(math.sqrt(16))
                • Classes e Herança: Em programação orientada a objetos, classes e herança permitem reutilizar código ao criar novas classes baseadas em classes existentes.
                • Templates ou Genéricos: Em algumas linguagens, como C++ ou Java, é possível criar código genérico que pode funcionar com diferentes tipos de dados, 
                aumentando a reusabilidade.
    Obs: A 'Arte' de escrever um programa é saber compor e tecer esses elementos básicos juntos muitas vezes para produzir algo que é útil para seus usuários.
        (Do básico você criar o avançado.)
    """

#O QUE PODERIA DA ERRADO?
    """
    => A medida que seu programa vai se tornando sofisticado e complexo, você irá se deparar com três tipos gerais de erros:

        • Erros de Sintaxe (Syntax Errors): Um erro de sintaxe significa que você violou as regras da "gramática" do Python. Em outras palavras
        a regra da linguagem da programação não foi seguida corretamente. A sintaxe é o conjunto de regras que define como as instruções devem ser 
        escritas na linguagem, como a colocação de parênteses, chaves, vírgulas, e palavras-chave.
            Exemplos: 
                ○ Não fechar corretamente parênteses, colchetes, ou chaves.
                    ► Erro: SyntaxError: unexpected EOF while parsing
                ○ Falta de Dois Pontos (:) em Estruturas de Controle: Esquecer de colocar dois pontos após uma declaração if, for, while, etc.
                    ► Erro: SyntaxError: invalid syntax
                ○ Uso Indevido de Palavras-chave: Usar uma palavra-chave reservada de forma incorreta.
                    ► Erro: SyntaxError: invalid syntax
                ○ Indentação Incorreta (Em linguagens como Python): Misturar espaços e tabulações ou não alinhar corretamente o código.
                    ► Erro: IndentationError: expected an indented block
                ○ Esquecer Aspas em Strings: Não fechar uma string com a mesma aspas que foi usada para abri-la.
                    ► Erro: SyntaxError: EOL while scanning string literal
        
        • Erros de Lógica (Logic Errors): Ocorrem quando o código é sintaticamente correto e pode ser executado, mas não produz o resultado 
        esperado ou desejado. omo resultado, o programa pode funcionar, mas os resultados ou comportamentos não são os que deveriam ser.
        Os erros lógicos podem se manifestar de várias formas, incluindo:
            • Cálculos Incorretos: Usar uma operação matemática errada ou uma fórmula incorreta.
                ► Exemplo: 
                        total = 10 / 2  # Deve ser multiplicação em vez de divisão
                ► Problema: O programador queria multiplicar, mas usou divisão, levando a um resultado incorreto.
            • Condicionais Mal Formuladas: Condições if incorretas que levam a decisões erradas.
                ► Exemplo:
                    age = 17
                    if age >= 18:
                        print("You are eligible to vote")
                    else:
                        print("You are not eligible to vote")
                ► Problema: Se a lógica do problema for que pessoas com 17 anos ou mais podem votar, o código não refletirá isso corretamente.
            • Como Corrigir Erros Lógicos?
                ○ Depuração (Debugging): Usar ferramentas de depuração para seguir o fluxo de execução e inspecionar valores de variáveis pode ajudar a identificar onde a lógica falha.
                ○ Teste de Unidade (Unit Testing): Escrever testes de unidade para funções e métodos individuais pode ajudar a garantir que cada parte do código funcione como esperado.
                ○ Revisão de Código: Revisar o código cuidadosamente, ou pedir a outra pessoa para revisar, pode ajudar a identificar lapsos lógicos que passaram despercebidos.
                ○ Refatoração: Simplificar e refatorar o código pode tornar a lógica mais clara e menos propensa a erros.
        
        • Erros de Semântica (Semantic Errors): Estão relacionados ao significado (semântica) do código. Enquanto os erros lógicos referem-se ao raciocínio incorreto, 
        os erros semânticos geralmente envolvem o uso incorreto dos recursos da linguagem ou a interpretação errada de como esses recursos devem ser usados. Esses erros podem 
        causar comportamentos inesperados ou resultados incorretos, apesar de o código parecer correto em termos de sintaxe.
            Alguns exemplos de erros semânticos incluem:
                • Uso Inadequado de Operações: Utilizar operações que são permitidas pela linguagem, mas que não fazem sentido no contexto específico.
                    ► Exemplo: 
                        average = total / count  # Supondo que count seja 0
                    ► Problema: Divisão por zero não faz sentido matemático e causa um erro de tempo de execução.
                • Escolha Errada de Tipos de Dados: Usar um tipo de dado que não é adequado para a operação que está sendo realizada.
                    ► Exemplo: 
                        result = "3" + 2  # Tentar concatenar string com inteiro
                    ► Problema: A linguagem pode não saber como combinar esses dois tipos, levando a um erro.
            • Como Corrigir Erros de Semântica?
                ○ Entendimento Claro do Problema: Assegure-se de compreender completamente o problema que está tentando resolver e como a linguagem de programação deve ser usada para resolvê-lo.
                ○ Comentários e Documentação: Adicione comentários explicando a lógica e a intenção por trás do código, o que pode ajudar a evitar mal-entendidos semânticos.
                ○ Testes Cuidadosos: Realize testes detalhados, incluindo casos extremos e inusitados, para garantir que o código funcione corretamente em todas as situações esperadas.
                ○ Revisão de Código: Revisar o código com um foco especial no significado das operações e nos resultados esperados pode ajudar a identificar erros semânticos.
                            
    """

# DEBUGGING / TRATAMENTO DE PROBLEMAS
    """
    ► O Debugging é o processo de encontrar essa causa em seu código/script.
    ► Após usa ele ou até antes, também tem uns passos para ajudar na solução do problema. Consiste em quatro etapas:
        • Ler (Read): Leia seu código. Fale-o em voz alta para si próprio e verifique se ele diz mesmo o que você quer que ele diga.
        • Testar (Test): Experimente fazer mudanças e rodar diferentes versões do seu programa. Análise e faça teste, às vezes quando você colocar a coisa no lugar
        certo o problema se torna óbvio, porém, às vezes você precisará levar um tempo para solucionar. (Tenha paciência.)
        • Refletir: Tire um tempo para pensar! Que tipo de erro está acontecendo: Sintaxe, semântica, em tempo de execução? Que informações você pode extrair das mensagens de erros
        ou da saída do programa? Que tipo de erro poderia causa o problema que você está vendo? Qual foi a ultima coisa que você alterou? (No geral fazer uma análise melimetrica técnica)
        • Retroceder: Em certo momento, o melhor a se fazer é voltar atrás. Desfazer mudanças recentes.
    Obs: Se você faz teste sem pensar, você entra na 'Programação Randômica' ou famoso 'Tapa Virtual'.
    """

# PHASE-2

#VALORES E TIPOS
    """
    • Números Inteiros (Integers): Representam números inteiros, positivos ou negativos, sem casas decimais. Exemplo: 10, -5.

    • Números de Ponto Flutuante (Floats): Representam números reais com casas decimais. Exemplo: 3.14, -0.001.

    • Strings: Sequências de caracteres delimitadas por aspas simples ou duplas. Exemplo: "Hello, World!", 'Python'.

    • Booleanos (Booleans): Representam valores de verdade, sendo True (verdadeiro) ou False (falso). Exemplo: True, False.

    • Listas: Coleções ordenadas de elementos que podem ser de diferentes tipos, delimitadas por colchetes. Exemplo: [1, 2, 3], ['a', 'b', 'c'].

    • Dicionários (Dictionaries): Estruturas de dados que armazenam pares de chave-valor, delimitadas por chaves. Exemplo: {'name': 'Alice', 'age': 25}.

    • None: Representa a ausência de valor ou um valor nulo. Exemplo: None.
           
    """

#DECLARAÇÕES & ATRIBUIÇÃO
    """
        Declaração:
            ► Uma declaração é a instrução onde você introduz uma nova entidade no programa, como uma variável, função, classe, ou estrutura de controle. 
            Em algumas linguagens, você precisa declarar o tipo de uma variável antes de usá-la, mas em Python, a declaração e a atribuição geralmente 
            acontecem simultaneamente.
                Exemplo:
                    • Declaração de Variável: 
                        x = 10  # Declaração da variável 'x' com o valor 10
                    • Declaração de Função:
                        def greet():
                            print("Hello, World!")  # Declaração da função 'greet'
                    • Declaração de Condicional:
                        if x > 5:
                            print("x is greater than 5")  # Declaração 'if'
                    • Declaração de Loop:
                        for i in range(5):
                            print(i)  # Declaração 'for'
                Resumo:
                    Declarações são instruções que introduzem novos elementos no código e definem como o programa deve operar, 
                    desde a criação de variáveis até a definição de fluxos de controle.
        Atribuição:
            ► A atribuição é a operação de dar um valor a uma variável. Em Python, a atribuição ocorre quando você usa o operador = para associar um valor a uma variável.
            
        Declaração e Atribuição em Python:
            ► Em Python, a declaração e a atribuição costumam ocorrer juntas, pois você não precisa declarar o tipo da variável explicitamente.
        Resumo de ambos:
            ► Declaração: Introduz uma nova variável, função, etc., no programa.
            ► Atribuição: Associa um valor a uma variável.
    """
#OPERADORES E OPERANDOS
    """
        Operadores:
            ► Operadores são símbolos ou palavras-chave que indicam uma operação específica a ser realizada em valores ou variáveis (os operandos). Existem diferentes tipos de operadores:

                • Operadores Aritméticos: Realizam operações matemáticas básicas.
                    Exemplo: + (adição), - (subtração), * (multiplicação), / (divisão).
                    Em Python: x + y (soma x e y).
                • Operadores de Atribuição: Atribuem valores às variáveis.
                    Exemplo: = (atribuição), += (adição e atribuição).
                    Em Python: x = 5 (atribui 5 a x), x += 3 (soma 3 a x e atualiza x).
                • Operadores de Comparação: Comparam valores e retornam um valor booleano (True ou False).
                    Exemplo: == (igual a), != (diferente de), > (maior que), < (menor que).
                    Em Python: x == y (verifica se x é igual a y).
                • Operadores Lógicos: Combinam expressões booleanas.
                    Exemplo: and, or, not.
                    Em Python: x > 5 and y < 10 (verdadeiro se ambos x > 5 e y < 10 forem verdadeiros).
        Operandos:
            ► Operandos são os valores ou variáveis sobre os quais os operadores atuam. São os "elementos" sobre os quais a operação é realizada.
                • Em x + y, x e y são operandos, e + é o operador.
                    Exemplo:
                        x = 10       # Atribuição (x é o operando, = é o operador)
                        y = 5        # Atribuição (y é o operando, = é o operador)
                        z = x + y    # Aritmético (x e y são operandos, + é o operador)
                        result = z > 10 and y < 10  # Comparação e Lógico (z e y são operandos, >, <, and são operadores)
    """
#EXPRESSÕES
    """
        ► Uma expressão em programação é uma combinação de operandos (como valores, variáveis) e operadores que o interpretador ou compilador pode avaliar para produzir um valor.
            Tipos de Expressões
                • Expressões Aritméticas: Realizam operações matemáticas e retornam um valor numérico.
                    Exemplo: 3 + 5 * 2 (primeiro multiplica 5 * 2, depois soma 3, resultando em 13).
                • Expressões de Comparação: Comparam dois valores e retornam um valor booleano (True ou False).
                    Exemplo: x > 10 (retorna True se x for maior que 10, caso contrário False).
                • Expressões Lógicas: Combinam expressões booleanas usando operadores lógicos (and, or, not).
                    Exemplo: (x > 5) and (y < 10) (retorna True se ambas as comparações forem verdadeiras).
                • Expressões de String: Manipulam ou concatenam strings.
                    Exemplo: 'Hello, ' + 'World!' (concatena duas strings, resultando em 'Hello, World!').
                • Expressões de Função: Chamam uma função e retornam o resultado da função.
                    Exemplo: len('Python') (chama a função len() e retorna 6, que é o comprimento da string 'Python').
            Exemplo Combinado:
                x = 10
                y = 5
                result = (x * 2) + (y / 2) > 15 and x != y
            Explicação do Exemplo: Neste exemplo, a expressão completa ((x * 2) + (y / 2) > 15 and x != y) é 
            avaliada combinando aritmética, comparação e lógica. A expressão resulta em um valor booleano (True ou False), dependendo 
            dos valores de x e y.
            Resumo: Uma expressão é qualquer combinação de valores, variáveis, operadores, e funções que podem ser avaliadas para produzir um resultado. 
            Expressoes são fundamentais na programação, pois elas permitem que o código execute cálculos, compare valores, e tome decisões.

    """
#ORDEM DAS OPERAÇÕES
    """
    A ordem das operações determina a sequência em que os operadores em uma expressão são avaliados. Essa ordem segue regras matemáticas bem estabelecidas, também conhecidas como precedência de operadores. Se não for explicitamente alterada com parênteses, Python segue essas regras ao avaliar expressões.

        Ordem das Operações (Precedência):
            1. Parênteses (): Operações dentro de parênteses são avaliadas primeiro.
                Exemplo: 2 * (3 + 4) avalia primeiro 3 + 4, resultando em 2 * 7 = 14.
                
            2. Expoentes **: Operações de exponenciação são avaliadas em seguida.
                Exemplo: 2 ** 3 * 4 avalia 2 ** 3 primeiro, resultando em 8 * 4 = 32.
                
            3. Multiplicação *, Divisão /, Módulo % e Divisão Inteira //: Avaliadas da esquerda para a direita.
                Exemplo: 10 / 2 * 3 avalia 10 / 2 primeiro, resultando em 5 * 3 = 15.
                
            4. Adição + e Subtração -: Avaliadas da esquerda para a direita.
                Exemplo: 10 - 2 + 3 avalia 10 - 2 primeiro, resultando em 8 + 3 = 11.
                
            5. Operadores de Comparação (==, !=, >, <, >=, <=): São avaliados após as operações aritméticas.
                Exemplo: 3 + 2 > 4 avalia 3 + 2 primeiro, resultando em 5 > 4 = True.
                
            6. Operadores Lógicos:
                    Not: Tem precedência mais alta.
                    And: Avaliado após not.
                    Or: Avaliado por último.
                Exemplo: True or False and not False avalia not False primeiro, depois False and True, e finalmente True or False, resultando em True.
        Resumo:
            A ordem das operações segue uma hierarquia que respeita as regras matemáticas convencionais, sendo parênteses a mais alta prioridade, seguidos por exponenciação, depois 
            multiplicação e divisão, e finalmente adição e subtração. Ao usar operadores lógicos, a precedência também segue uma ordem estabelecida, com not avaliando antes de and, 
            e and antes de or. O uso de parênteses é essencial para garantir que as operações sejam avaliadas na ordem desejada.
    """
#GLOSSÁRIO
    """
    Capítulo 1
    
        • Análise sintática:  Processo de examinar um programa e analisar a estrutura sintática.
        
        • Bug: Um erro em um programa.
        
        • Central Processing Unit: Unidade central de processamento, considerada o coração de qualquer computador. É o que roda o software que escrevemos,
        também chamado de “CPU” ou “processador”.
        
        • Código de Máquina: A linguagem de nível mais baixo para software, que é a linguagem que é diretamente executada pela unidade central de processamento (CPU).
        
        • Código Fonte: Um programa em uma linguagem de alto nível.

        • Compilar: Ação de traduzir um programa escrito em uma linguagem de alto nível para uma linguagem de baixo nível, tudo em preparação para a execução posterior.

        • Erro de Semântica: Um erro em um programa que faz com que, na execução, ele faça algo diferente do que o programador intencionou.

        • Função print: Instrução que faz com que o interpretador Python exiba um valor na tela.

        • Interpretar: Executar um programa em uma linguagem de alto nível, traduzindo-o uma linha por vez.

        • Linguagem de Alto Nível: Uma linguagem de programação como o Python, projetada para ser fácil para os humanos lerem e escreverem.

        • Linguagem de Baixo Nível: Uma linguagem de programação projetada para ser fácil para um computador executar; também chamado de “código de máquina” ou “linguagem de montagem (assembly)”.

        • Memória Principal: Armazena programas e dados. A memória principal perde sua informação quando a energia é desligada.

        • Memória Secundária: Armazena programas e dados e retém suas informações mesmo quando a fonte de alimentação está desligada. Geralmente mais lenta que a memória principal. Exemplos de memória secundária incluem drives de disco e memória flash em pendrives.

        • Modo Interativo: Uma maneira de usar o interpretador Python digitando comandos e expressões no prompt.

        • Portabilidade: Uma propriedade de um programa que pode ser executado em mais de um tipo de computador.

        • Programa: Um conjunto de instruções que especifica a computação a ser executada pela máquina.

        • Prompt: Quando um programa exibe uma mensagem e pausa para o usuário digitar alguma entrada para o programa.

        • Resolução de Problemas: O processo de formular um problema, encontrar uma solução e expressar a resolução.

        • Semântica: O significado de um programa.
    
    Capítulo 2

        • Atribuição: Uma declaração que atribui um valor a uma variável.
        • Concatenação: União de dois operandos de ponta a ponta.
        • Comentário: Informações em um programa destinadas a outros programadores (ou qualquer pessoa que esteja lendo o código-fonte) e que não têm efeito sobre a execução do programa.
        • Avaliar: Simplificar uma expressão executando as operações para gerar um único valor.
        • Expressão: Uma combinação de variáveis, operadores e valores que representa um único valor de resultado.
        • Ponto-Flutuante: Um tipo que representa a parte fracionária.
        • Inteiro: Um tipo que representa números inteiros.
        • Palavra-chave: Uma palavra reservada usada pelo compilador para analisar um programa; você não pode utilizar palavras-chave como if, def, e while para serem nomes de variáveis.
        • Mnemônico: Um recurso auxiliar de memória. Muitas vezes damos nomes mnemônicos a variáveis para nos ajudar a lembrar o que é armazenado na variável.
        • Modulus Operator: Um operador, denotado com um sinal de porcentagem (%), que trabalha com inteiros e produz o restante quando um número é dividido por outro.
        • Operando: Um dos valores nos quais um operador opera.
        • Operador: Um símbolo especial que representa um cálculo simples como adição, multiplicação ou concatenação de strings.
        • Regras de Precedência: O conjunto de regras que regem a ordem na qual expressões envolvendo múltiplos operadores e operandos são avaliadas.
        • Declaração: Uma seção de código que representa um comando ou uma ação. Até agora, as declarações que temos são atribuições e declarações impressas.
        • String: Um tipo que representa sequências de caracteres.
        • Tipo: Uma categoria de valores. Os tipos que vimos até agora são inteiros (tipo int), números com ponto flutuante (tipo float), e strings (tipo str).
        • Valor: Uma das unidades básicas de dados, como um número ou string, que um programa manipula.
        • Variável: Um nome que se refere a um valor.
"""
# Uso do 'Build in Fuction' int
    """
prompt = 'Qual... a velocidade rasante de um andorinha livre?\n'
velocidade = input(prompt)
int(velocidade)
int(velocidade) + 5

"""

# Pergunta & Resposta (Básico)

    """
    name = input ('name: ' )
    print ('Olá, ' + name )
    idade = input ('idade: ')
    print ('Você tem' + idade + 'anos')

    """

# Uso básico da Function com uma String

    """
    print = ('Hello World')

    """