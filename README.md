# Design-Patterns

## O que são padrões de projeto?

-   São soluções para problemas conhecidos na arquitetura de software que foram utilizados e testados no passado e continuam relevantes nos dias atuais
-   Inicialmente, foram criados com foco na POO. Atualmente, são soluções universais que funcionam em qualquer linguagem de programação, mesmo que não suportam POO em sua totalidade (JavaScript, Python, etc...)
-   São divididos em 3 categorias: *de criação*, que visam abstrair o processo de como objetos são criados na aplicação; *estruturais*, que lidam com a composição de classes e objetos; *comportamentais*, que caracterizam como as classes e objetos interagem e distribuem responsabilidade na aplicação

## Beneficios e problemas

### Beneficios:
-   Não é necessário inventar nada, apenas implementar
-   Padrões universais facilitam o entendimento do projeto
-   Evita refatoração desnecessária
-   Ajuda na reutilização de código
-   Abstrai e nomeia partes particulares do projeto
-   Ajuda na aplicação dos principios do design orientado a objetos
-   Facilitam a criação de testes unitarios

### Maleficios:
-   Alguns padrões podem ser complexos e seu entendimento pode ser demorado
-   Muito código para atingir um objetivo simples
-   Podem trazer otimizações prematuras para o seu código
-   Se usados incorretamente, mais atrapalharão do que ajudarão.


## Principios do design orientado a objetos(SOLID)
-   Single Responsability Principle - Uma classe deve ter apenas um motivo para mudar(evitar conjunções aditivas: e, bem como, tambem), ou seja uma classe deve fazer uma única coisa, classe que por exemplo abre, le e fecha o arquivo deve ser quebrado em três classes diferentes.

-   Open/Closed principle - Classes ou objetos e metodos devem estar abertos para extensão, mas fechados para modificações

-   Liskov substitution principle - classes derivadas devem ser capazas de substituir totalmente classes-bases

-   Interface segregations principle - Os clientes não devem ser forçados a depender de interfaces que não utilizam

-   Dependency inversion principle - modulos de alto nivel não devem ser dependentes do modulos de baixo nivel; ambos devem depender de abstrações. Detalhes devem depender das abstrações, não o inverso.