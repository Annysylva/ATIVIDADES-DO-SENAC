Sistema bancário com POO
Criar o sistema bancário com orientação a objetos

<h1>Objetivos</h1>
O objetivo geral é iniciar A modelagem no sistema bancário em programação voltada para objetos e adição de classes para cliente e operações bancárias de depósito e saque.
O que precisamos fazer é atualizar a implementação do sistema bancário para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários.
O código deve seguir o modelo UML de classes a seguir:
Diagrama de classes - Sistema bancário
Classe conta
<h1>Uma conta de classe deve ter:</h1>

![imagem_diagrama](https://publish-01.obsidian.md/access/0facd8b3adf554bc13eca4d061b8d846/Programador/Desafios/sistema%20bancario/anexos/diagrama-sistema-bancario.png)
saldo;
número;
agência;
cliente;
e histórico;
todos como atributos da classe e eles são privados (sinal de menos)
<h1>4 métodos:</h1>
saldo - não recebe nenhum argumento ele retorna float;
nova conta - é um método que cria uma conta (método de fábrica) então ele vai receber um cliente e o número da conta que pode ser um temporário, e tem retornar o objeto contra;
a operação de sacar - recebe um valor que é float e retorna um boleano;
e o depositar recebe um valor que é float e retorna boleano, para que se a operação aconteceu com sucesso ou falha retorna True se deu certo sacar, e caso se não depositar retorna falso, se deu errado e não depositar, por falso se deu errado também .
Conta corrente com herança
A Conta ela tem uma classe filha, então aqui a conta corrente estende a conta porque é uma classe do tipo conta, então ela tem tudo que a conta tem mais dois atributos que seriam: o limite e o limite de saques.

<h1>Atributo Histórico</h1>
Ainda continuando na conta temos o histórico, ele é um tipo de classe e essa classe é histórica, então uma conta tem um histórico, que pertence a uma conta.

<h1>Interface Transação</h1>
O histórico tem um método que é adicionar transação, ele também tem um argumento de que são as transações, onde se depositando transações, que é do tipo transação, esta é uma interface, onde essa interface que seria a classe abstrata.
A classe abstrata Interface, é uma classe pai, então ela tem um método registrador que recebe uma conta, assim também temos duas classes que implementam essa interface.
As classes que implementam a abstrata da transação são: uma de depósito e a outra é a de saque, ambos têm os atributos do valor e consequentemente a implementação do método registrador.
Cliente de classe
<h1>A classe cliente tem:</h1>

endereço;
e tem uma lista de contas - que é do tipo conta;
2 operações:
o primeiro é realizar a transação - ele recebe dois atributos, que seria uma conta e a transação, onde a conta é do tipo conta e a transação é do tipo aqui da classe que estava na transação, então pode ser um saque, passar um depósito, mas a gente vai olhar ai para saber se temos um polimorfismo .
conta - lembrando que o Adicionar meu cliente pode ter várias contas, e com várias contas onde a conta é relacionada a um cliente e temos uma generalização .
Pessoa física
<h1>A classe pessoa física e é um tipo de cliente, ela tem:</h1>

CPF;
nome;
dados de nascimento.