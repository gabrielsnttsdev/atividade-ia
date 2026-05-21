# Atividade IA

Projeto de práticas e demonstrações para a disciplina de Fundamentos de Inteligência Artificial.

## Visão geral

Este repositório reúne:
- Uma página web com um classificador de imagem em tempo real feito com Teachable Machine e TensorFlow.js (`index.html`).
- Diversos exercícios em Python que exploram lógica, refatoração, debug e explicação de código.

## Estrutura do projeto

- `index.html`
  - Página web que carrega um modelo Teachable Machine para classificação de imagens usando webcam.
  - Usa Bootstrap para layout e TensorFlow.js para inferência em tempo real.
- `README.md`
  - Guia do projeto.
- `teste-code-assistent/`
  - `explicacao_num_primo.md`
    - Documento explicando a lógica de verificação de número primo e apresentando a versão otimizada do algoritmo.
  - `pratica1.py`
    - Verificação de número primo com duas versões: uma simples e outra otimizada com tipagem e docstring.
  - `pratica2.py`
    - Refatoração de uma função que calcula estatísticas básicas de uma lista de números.
  - `pratica3.py`
    - Exemplo de debug em código Python que calcula o total de uma compra com imposto e desconto.
  - `pratica4.py`
    - Explicação detalhada do código de estatísticas, linha a linha.

## Como executar

### Página web

1. Abra `index.html` em um navegador moderno.
2. Conceda permissão para usar a webcam.
3. Clique em **Iniciar câmera**.

> Observação: o modelo é carregado de um servidor externo do Teachable Machine, portanto é necessária conexão com a internet.

### Scripts Python

1. Abra um terminal no diretório `teste-code-assistent`.
2. Execute os arquivos desejados com Python 3:

```bash
python pratica1.py
python pratica2.py
python pratica3.py
python pratica4.py
```

## Tecnologias usadas

- HTML, CSS e JavaScript
- Bootstrap 5
- TensorFlow.js
- Teachable Machine
- Python 3

## Notas importantes

- `index.html` não depende de um servidor local, basta abrir o arquivo no navegador.
- Os scripts Python são exemplos didáticos e não exigem bibliotecas externas além da própria linguagem.
- O arquivo `pratica3.py` inclui correções de lógica e ilustra o processo de debugging.

## Melhoria sugerida

- Adicionar testes automatizados para os scripts Python.
- Separar o código JavaScript em um arquivo externo para facilitar manutenção.
- Incluir validação de entrada nos scripts Python.
