# Projeto Calculadora

Calculadora simples executada pelo terminal, desenvolvida como atividade
prática do curso de Analista de Dados da EBAC.

## Funcionalidades

- Soma
- Subtração
- Multiplicação
- Divisão
- Validação de números inválidos
- Tratamento de divisão por zero

## Tecnologias

- Python 3
- Shell Script (Bash)
- Linux / Ubuntu

## Como executar

### Python

```bash
python3 calculadora.py
```

### Shell Script

Conceda permissão de execução ao script uma única vez:

```bash
chmod +x calculadora.sh
./calculadora.sh
```

O script localiza o arquivo Python automaticamente, portanto pode ser
executado a partir de qualquer diretório.

## Exemplo

```text
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

## Estrutura

```text
.
├── calculadora.py
├── calculadora.sh
├── comandos_usados.txt
└── README.md
```

## Conceitos praticados

O projeto utiliza variáveis, entrada e saída de dados, conversão com
`float()`, operadores matemáticos, estruturas condicionais e execução de
scripts no terminal.

## Autor

**Eduardo Silva**
Analista de Dados — EBAC
