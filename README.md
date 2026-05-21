# atividade-ia

Repositório de projetos desenvolvidos como atividades práticas de Inteligência Artificial e desenvolvimento de software.

## Projetos

### To-Do App

Aplicacao de gerenciamento de tarefas desenvolvida com HTML, CSS e JavaScript puro, sem backend ou dependências de servidor.

**Pasta:** `to-do-app/`

**Tecnologias:** HTML5, Tailwind CSS (CDN), JavaScript vanilla, localStorage

**Funcionalidades:**
- Autenticacao com login e cadastro de usuarios
- Sessao persistida via localStorage
- Dashboard com criacao e listagem de tarefas
- Tipos de tarefa: Trabalho, Pessoal, Estudos
- Marcar tarefas como concluidas
- Dados isolados por usuario

**Como rodar:**
```bash
# Abra diretamente no navegador ou use um servidor local:
node -e "require('http').createServer((q,r)=>{require('fs').readFile('to-do-app'+(q.url=='/'?'/index.html':q.url),(e,d)=>{r.writeHead(e?404:200);r.end(e?'404':d)})}).listen(8765)"
# Acesse: http://localhost:8765
```

---

### Space Invaders Classico

Jogo arcade inspirado no Space Invaders original, desenvolvido em Python com Pygame.

**Pasta:** `space-invaders/`

**Tecnologias:** Python 3, Pygame

**Funcionalidades:**
- Nave jogável com movimento e disparo
- 40 inimigos em grade 4x10 com movimentação progressiva
- Sistema de pontuacao e vidas
- Ondas infinitas com aumento de dificuldade
- Tela de Game Over com reinicio

**Como rodar:**
```bash
pip install pygame
python space-invaders/main.py
```

**Controles:** `←` `→` mover | `Espaco` atirar | `R` reiniciar

---

## Estrutura do repositorio

```
atividade-ia/
├── to-do-app/
│   ├── index.html
│   ├── app.js
│   └── README.md
├── space-invaders/
│   ├── main.py
│   └── README.md
├── atividade-ia-main/
│   └── teste-code-assistent/
├── .agent/
└── .gitignore
```

## Autor

Gabriel Santos — [@gabrielsnttsdev](https://github.com/gabrielsnttsdev)
