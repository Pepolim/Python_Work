# Python_Work
Trabalho de Python

# Nuno Miguel Pepolim Marques

# UFCD 10793 - Fundamentos de Python
# UFCD 10790 - Projeto de Programação


# Coleção de mecanicas de jogos simples

Uma coleção de mecanicas de jogos simples para uso futuro onde cada nivel vai adicionar uma nova mecânica de jogo. 

## Índice

- [Introdução](#introdução)
- [Âmbito do Projeto](#âmbito-do-projeto)
- [Levantamento de Requisitos](#levantamento-de-requisitos)
- [Elaboração do Projeto](#elaboração-do-projeto)
- [Desempenho do Projeto](#desempenho-do-projeto)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Resultados](#resultados)
- [Conclusão](#conclusão)
- [Trabalhos Futuros](#trabalhos-futuros)

## Introdução

Este projeto consiste mum jogo simples com varias mecanicas diferentes que vao sendo adicionadas ao longo do tempo.

## Âmbito do Projeto

- **Objetivo**: Desenvolver uma aplicação simples para guardar mecânicas para uso futuro.

- **Público-Alvo**: a mim mesmo

- ## **Limitações**: 
Os meus conhecimentos de python e pygame 

## Levantamento de Requisitos

### Requisitos Funcionais

- **RF01**: A aplicação deve ter um menu principal com opções para para entrar nos jogos, listar os jogos, opcoes do jogo(som, tamanho da tela), sair do programa.
- **RF02**: A aplicação deve de adicionar uma mecanica de jogo nova a cada nivel:
            - **Nivel 1**: um cubo que se move para a direita e esquerda- 
            - **Nivel 2**: um cubo que se move para a direita e esquerda, mas agora é mais suave á andar e nao para de repente
            - **Nivel 3**: introduzo uma mecânica nova de saltar e gravidade, também existem obstaculos
            - **Nivel 4**: o cubo faz o mesmo, mas agora no nível existe um buraco onde se o cubo cair faz reset ao nivel
            - **Nivel 5**: o mesmo acima, mas agora existem plataformas
            - **Nivel 6**: introduzo uma mecânica nova onde se o cubo estiver em cima de uma certa plataforma e pressionar a tecla ‘E’ o tamanho do cubo diminui ou aumenta se estiver pequeno
            - **Nivel 7**: usa a mecânica anterior e plataforma para passar o nivel
            - **Nivel 8**: introduzo uma mecânica nova onde se o cubo estiver em cima de uma certa plataforma e pressionar a tecla ‘E’ a gravidade inverte


### Requisitos Não Funcionais

- **RNF01**: Um menu principal com opções para entrar listar os niveis, opções do jogo (som,
 tamanho da tela)

## Desenvolvimento do Projeto

### Arquitetura

A arquitetura da aplicação é dividida em ..

- **Front-End**: Interface grafica que permite interagir com o utilizador.
- **Back-End**: Lógica de interação com os objetos e a lógica de jogo.

### Tecnologias Utilizadas

- **Linguagens**: Python 3.10
- **Bibliotecas**:
  - `pygame`: Para a criação de jogos simples.
- **Ferramentas**:
  - GitHub para controlo de versão.
  - Visual Studio Code como IDE.

### Implementação

- Documentar ficheiros do projeto com os comentários para perceber as funcionalidades

## Desempenho do Projeto

### Testes Realizados

- **Testes funcionais**: Verificação da funcionalidade do jogo

## Como Executar o Projeto

```bash
# Clonar o repositório
git clone https://github.com/Pepolim/Python_Work

# Navegar até ao diretório do projeto
cd Python_Work

# Instalar as dependências (se necessário)
pip install pygame

# Executar a applicação
python main.py
```
