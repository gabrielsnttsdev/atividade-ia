# To-Do App

Aplicação de gerenciamento de tarefas desenvolvida com HTML, CSS e JavaScript vanilla, sem nenhuma dependência de backend ou servidor.

## Tecnologias

- HTML5 semântico
- Tailwind CSS via CDN
- JavaScript puro (ES6+)
- localStorage como banco de dados no navegador

## Funcionalidades

### Autenticação
- Cadastro de usuário com nome, e-mail e senha
- Login com validação de credenciais
- Sessão persistida via `currentUser` no localStorage
- Logout com limpeza de sessão

### Validações
- Campos obrigatórios verificados antes do envio
- Verificação de e-mail já cadastrado no registro
- Mensagens de erro exibidas inline em cada campo
- Feedback visual de sucesso no cadastro

### Tarefas
- Criação de tarefas com título (obrigatório), tipo e descrição (opcional)
- Tipos disponíveis: Trabalho, Pessoal, Estudos
- Badges coloridos por tipo:
  - Trabalho — azul
  - Pessoal — roxo
  - Estudos — verde
- Marcar tarefa como concluída (texto riscado + opacidade reduzida)
- Tarefas concluídas aparecem no final da lista
- Cada usuário vê somente suas próprias tarefas (filtro por e-mail)
- Dados persistidos entre sessões via localStorage

## Estrutura do projeto

```
to-do-app/
├── index.html   # Estrutura das telas: login, cadastro e dashboard
└── app.js       # Toda a lógica da aplicação
```

## Estrutura do localStorage

```json
{
  "users": [
    {
      "id": "1234567890",
      "name": "Nome do Usuario",
      "email": "usuario@exemplo.com",
      "password": "senha"
    }
  ],
  "todos": [
    {
      "id": "1234567891",
      "userId": "usuario@exemplo.com",
      "title": "Titulo da tarefa",
      "type": "work",
      "description": "Descricao opcional",
      "done": false
    }
  ],
  "currentUser": {
    "id": "1234567890",
    "name": "Nome do Usuario",
    "email": "usuario@exemplo.com"
  }
}
```

## Como executar

Por ser uma aplicação puramente client-side, basta abrir o arquivo `index.html` em qualquer navegador moderno.

Para rodar com um servidor local (recomendado para evitar restrições de CORS):

```bash
# Com Node.js instalado
node -e "const http=require('http'),fs=require('fs'),path=require('path');http.createServer((req,res)=>{let f=path.join('.',req.url==='/'?'index.html':req.url);fs.readFile(f,(e,d)=>{res.writeHead(e?404:200,{'Content-Type':{'html':'text/html','js':'application/javascript'}[path.extname(f).slice(1)]||'text/plain'});res.end(e?'Not found':d)})}).listen(8765,()=>console.log('Rodando em http://localhost:8765'))"
```

Acesse: [http://localhost:8765](http://localhost:8765)

## Design

- Tema escuro com fundo `#0f172a`
- Cards com efeito glassmorphism (backdrop-blur + borda sutil)
- Tipografia Inter via Google Fonts
- Animacoes suaves de entrada (fade-in)
- Hover states e transicoes em todos os elementos interativos

## Autor

Gabriel Santos — [@gabrielsnttsdev](https://github.com/gabrielsnttsdev)
