# 🧮 Projeto Calculadora


## 📌 Sobre o projeto


Este projeto foi desenvolvido como atividade prática do curso de **Analista de Dados da EBAC**, com o objetivo de colocar em prática conceitos básicos de programação em Python e utilização do terminal Linux.


A aplicação consiste em uma calculadora simples executada pelo terminal. O programa interage com o usuário, solicita seu nome, recebe dois números e permite escolher entre quatro operações matemáticas: soma, subtração, multiplicação e divisão.


O projeto também conta com um script Shell (Bash), utilizado para facilitar a execução da aplicação em ambiente Linux.


## 🛠️ Tecnologias utilizadas



- Python 3

- Shell Script (Bash)

- Linux / Ubuntu

- Git

- GitHub

- Google Colab



## ⚙️ Funcionalidades


A calculadora permite realizar as seguintes operações:



- ➕ Soma

- ➖ Subtração

- ✖️ Multiplicação

- ➗ Divisão



Ao iniciar o programa, o usuário informa seu nome e, em seguida, digita dois números.


Depois disso, é apresentado um menu para que o usuário escolha a operação desejada. O resultado é calculado e exibido diretamente no terminal.


## 💻 Como funciona


Primeiramente, o programa solicita o nome do usuário:


Plain text






```
Digite seu nome: Eduardo
Olá, Eduardo, vamos começar!


```





Em seguida, são solicitados dois números:


Plain text






```
Digite um número: 10
Digite um número: 5


```





O programa apresenta as opções disponíveis:


Plain text






```
Escolha a operação:
1 - soma
2 - subtração
3 - multiplicação
4 - divisão


```





Após a escolha, a operação correspondente é realizada e o resultado apresentado.


## ▶️ Como executar


### Executando pelo Python


Abra o terminal, navegue até a pasta do projeto e execute:


Plain text






```
python3 calculadora.py


```





### Executando pelo Shell Script


Primeiro, conceda permissão de execução ao arquivo:


Plain text






```
sudo chmod +x calculadora.sh


```





Depois, execute o script:


Plain text






```
./calculadora.sh


```





Os comandos utilizados durante a configuração e execução do projeto estão registrados no arquivo `comandos_usados.txt`.


## 📂 Estrutura do projeto


Plain text






```
projetocalculadora/
├── calculadora.py
├── calculadora.sh
├── comandos_usados.txt
└── README.md


```





## 🧠 Conceitos de programação utilizados


Durante o desenvolvimento foram utilizados conceitos fundamentais de programação em Python, como:



- Variáveis

- Entrada de dados com `input()`

- Saída de dados com `print()`

- Conversão de dados utilizando `float()`

- Operadores matemáticos

- Estruturas condicionais `if`, `elif` e `else`

- Interação com o usuário pelo terminal

- Execução de scripts no Linux



A escolha da operação é realizada através de uma estrutura condicional, que verifica a opção informada pelo usuário e executa o cálculo correspondente.


## 📋 Exemplo de utilização


Plain text






```
Digite seu nome: Eduardo
Olá, Eduardo, vamos começar!

Digite um número: 10
Digite um número: 5

Escolha a operação:
1 - soma
2 - subtração
3 - multiplicação
4 - divisão

Digite o número da operação desejada: 3

O resultado da multiplicação é: 50.0


```





## 🎯 Objetivo


O objetivo deste projeto foi desenvolver uma aplicação simples em Python para praticar os fundamentos da programação, além de aprender a utilizar o terminal Linux e comandos básicos para execução de scripts.


O projeto também faz parte do meu processo de aprendizado no curso de **Analista de Dados da EBAC**, servindo como uma das primeiras aplicações desenvolvidas durante minha formação.


## 👨‍💻 Autor


**Eduardo Silva**


Projeto desenvolvido como parte dos estudos em **Analista de Dados — EBAC**.
