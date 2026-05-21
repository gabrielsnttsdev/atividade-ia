// =============================================
// DATABASE LAYER (localStorage as db.json)
// =============================================
const db = {
    _KEYS: {
        USERS: 'users',
        TODOS: 'todos',
        CURRENT_USER: 'currentUser'
    },

    init() {
        if (!localStorage.getItem(this._KEYS.USERS)) {
            localStorage.setItem(this._KEYS.USERS, JSON.stringify([]));
        }
        if (!localStorage.getItem(this._KEYS.TODOS)) {
            localStorage.setItem(this._KEYS.TODOS, JSON.stringify([]));
        }
    },

    // Users
    getUsers() {
        return JSON.parse(localStorage.getItem(this._KEYS.USERS)) || [];
    },
    saveUser(user) {
        const users = this.getUsers();
        users.push(user);
        localStorage.setItem(this._KEYS.USERS, JSON.stringify(users));
    },
    findUserByEmail(email) {
        return this.getUsers().find(u => u.email === email) || null;
    },

    // Session
    getCurrentUser() {
        const raw = localStorage.getItem(this._KEYS.CURRENT_USER);
        return raw ? JSON.parse(raw) : null;
    },
    setCurrentUser(user) {
        localStorage.setItem(this._KEYS.CURRENT_USER, JSON.stringify(user));
    },
    clearCurrentUser() {
        localStorage.removeItem(this._KEYS.CURRENT_USER);
    },

    // Todos
    getTodos() {
        return JSON.parse(localStorage.getItem(this._KEYS.TODOS)) || [];
    },
    getTodosByUser(userId) {
        return this.getTodos().filter(t => t.userId === userId);
    },
    addTodo(todo) {
        const todos = this.getTodos();
        todos.push(todo);
        localStorage.setItem(this._KEYS.TODOS, JSON.stringify(todos));
    },
    toggleTodoDone(todoId) {
        const todos = this.getTodos();
        const idx = todos.findIndex(t => t.id === todoId);
        if (idx === -1) return;
        todos[idx].done = !todos[idx].done;
        localStorage.setItem(this._KEYS.TODOS, JSON.stringify(todos));
    }
};

// =============================================
// UI HELPERS
// =============================================
const ui = {
    authWrapper:   document.getElementById('auth-wrapper'),
    viewLogin:     document.getElementById('view-login'),
    viewRegister:  document.getElementById('view-register'),
    viewDashboard: document.getElementById('view-dashboard'),

    showLogin() {
        this.authWrapper.classList.remove('hide');
        this.viewLogin.classList.remove('hide');
        this.viewRegister.classList.add('hide');
        this.viewDashboard.classList.add('hide');
    },

    showRegister() {
        this.authWrapper.classList.remove('hide');
        this.viewRegister.classList.remove('hide');
        this.viewLogin.classList.add('hide');
        this.viewDashboard.classList.add('hide');
    },

    showDashboard(user) {
        this.authWrapper.classList.add('hide');
        this.viewDashboard.classList.remove('hide');
        document.getElementById('user-display-name').textContent = user.name;
    },

    showError(id, message) {
        const el = document.getElementById(id);
        if (!el) return;
        el.textContent = message;
        el.classList.remove('hide');
    },

    clearErrors(form) {
        form.querySelectorAll('[id^="error-"]').forEach(el => el.classList.add('hide'));
    },

    showGlobalSuccess(id, message) {
        const el = document.getElementById(id);
        if (!el) return;
        el.textContent = message;
        el.className = 'success-msg rounded-xl p-3 text-sm text-center';
        el.classList.remove('hide');
    },

    showGlobalError(id, message) {
        const el = document.getElementById(id);
        if (!el) return;
        el.textContent = message;
        el.className = 'error-msg rounded-xl p-3 text-sm text-center';
        el.classList.remove('hide');
    }
};

// =============================================
// TASK RENDERING
// =============================================
const BADGE_MAP = {
    work:     { label: 'Trabalho', cls: 'badge-work' },
    personal: { label: 'Pessoal',  cls: 'badge-personal' },
    study:    { label: 'Estudos',  cls: 'badge-study' }
};

function renderTasks() {
    const user = db.getCurrentUser();
    if (!user) return;

    const allTasks = db.getTodosByUser(user.email);
    const pending   = allTasks.filter(t => !t.done);
    const completed = allTasks.filter(t => t.done);
    const sorted    = [...pending, ...completed];

    const container = document.getElementById('task-list');
    const countEl   = document.getElementById('task-count');

    container.innerHTML = '';
    countEl.textContent = `${pending.length} pendente${pending.length !== 1 ? 's' : ''} / ${allTasks.length} total`;

    if (sorted.length === 0) {
        container.innerHTML = `
            <div class="glass rounded-2xl p-10 text-center border border-dashed border-slate-700/60">
                <svg class="w-12 h-12 text-slate-700 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
                </svg>
                <p class="text-slate-500 text-sm">Nenhuma tarefa cadastrada ainda.</p>
                <p class="text-slate-600 text-xs mt-1">Adicione sua primeira tarefa acima.</p>
            </div>`;
        return;
    }

    sorted.forEach(task => {
        const badge   = BADGE_MAP[task.type] || BADGE_MAP.work;
        const doneClass = task.done ? 'done' : '';
        const btnLabel  = task.done ? 'Concluida' : 'Concluir';
        const btnStyle  = task.done
            ? 'bg-slate-800/60 border border-slate-700/40 text-slate-500 cursor-default'
            : 'bg-emerald-600/20 border border-emerald-500/30 text-emerald-400 hover:bg-emerald-500/30 transition-colors';

        const descBlock = task.description
            ? `<p class="text-slate-500 text-xs mt-2 leading-relaxed">${escapeHtml(task.description)}</p>`
            : '';

        const card = document.createElement('div');
        card.className = `task-card ${doneClass} rounded-2xl p-5 fade-in`;
        card.setAttribute('data-id', task.id);
        card.innerHTML = `
            <div class="flex items-start justify-between gap-3">
                <div class="flex-1 min-w-0">
                    <div class="flex items-center gap-2 flex-wrap mb-1">
                        <span class="task-title font-semibold text-white text-sm truncate">${escapeHtml(task.title)}</span>
                        <span class="text-xs font-medium px-2.5 py-0.5 rounded-full ${badge.cls}">${badge.label}</span>
                    </div>
                    ${descBlock}
                </div>
                <button
                    class="shrink-0 btn-complete px-3 py-1.5 rounded-lg text-xs font-medium ${btnStyle}"
                    data-id="${task.id}"
                    ${task.done ? 'disabled' : ''}
                    aria-label="Marcar tarefa como concluida"
                >
                    ${task.done
                        ? `<span class="flex items-center gap-1">
                                <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
                                Concluida
                           </span>`
                        : `<span class="flex items-center gap-1">
                                <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                                Concluir
                           </span>`
                    }
                </button>
            </div>`;
        container.appendChild(card);
    });
}

function escapeHtml(str) {
    return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
}

// =============================================
// EVENT HANDLERS
// =============================================
function handleLogin(e) {
    e.preventDefault();
    ui.clearErrors(e.target);

    const email    = document.getElementById('login-email').value.trim();
    const password = document.getElementById('login-password').value.trim();
    let valid = true;

    if (!email) {
        ui.showError('error-login-email', 'O e-mail e obrigatorio.');
        valid = false;
    }
    if (!password) {
        ui.showError('error-login-password', 'A senha e obrigatoria.');
        valid = false;
    }
    if (!valid) return;

    const user = db.findUserByEmail(email);
    if (!user) {
        ui.showGlobalError('error-login-global', 'E-mail nao encontrado.');
        return;
    }
    if (user.password !== password) {
        ui.showGlobalError('error-login-global', 'Senha incorreta.');
        return;
    }

    const { password: _, ...safe } = user;
    db.setCurrentUser(safe);
    e.target.reset();
    app.checkAuth();
}

function handleRegister(e) {
    e.preventDefault();
    ui.clearErrors(e.target);

    const name     = document.getElementById('register-name').value.trim();
    const email    = document.getElementById('register-email').value.trim();
    const password = document.getElementById('register-password').value.trim();
    let valid = true;

    if (!name) {
        ui.showError('error-register-name', 'O nome e obrigatorio.');
        valid = false;
    }
    if (!email) {
        ui.showError('error-register-email', 'O e-mail e obrigatorio.');
        valid = false;
    }
    if (!password || password.length < 4) {
        ui.showError('error-register-password', 'A senha deve ter ao menos 4 caracteres.');
        valid = false;
    }
    if (!valid) return;

    if (db.findUserByEmail(email)) {
        ui.showGlobalError('error-register-global', 'Este e-mail ja esta em uso.');
        return;
    }

    db.saveUser({ id: Date.now().toString(), name, email, password });
    ui.showGlobalSuccess('error-register-global', 'Conta criada com sucesso! Redirecionando...');

    setTimeout(() => {
        e.target.reset();
        ui.clearErrors(e.target);
        ui.showLogin();
    }, 1500);
}

function handleAddTask(e) {
    e.preventDefault();
    ui.clearErrors(e.target);

    const title       = document.getElementById('task-title').value.trim();
    const type        = document.getElementById('task-type').value;
    const description = document.getElementById('task-description').value.trim();

    if (!title) {
        ui.showError('error-task-title', 'O titulo e obrigatorio.');
        return;
    }

    const user = db.getCurrentUser();
    db.addTodo({
        id:          Date.now().toString(),
        userId:      user.email,
        title,
        type,
        description,
        done:        false
    });

    e.target.reset();
    renderTasks();
}

function handleCompleteTask(taskId) {
    db.toggleTodoDone(taskId);
    renderTasks();
}

// =============================================
// APP INIT
// =============================================
const app = {
    init() {
        db.init();
        this.bindEvents();
        this.checkAuth();
    },

    bindEvents() {
        document.getElementById('form-login').addEventListener('submit', handleLogin);
        document.getElementById('form-register').addEventListener('submit', handleRegister);
        document.getElementById('form-task').addEventListener('submit', handleAddTask);

        document.getElementById('link-to-register').addEventListener('click', (e) => {
            e.preventDefault();
            document.getElementById('form-login').reset();
            ui.clearErrors(document.getElementById('form-login'));
            ui.showRegister();
        });

        document.getElementById('link-to-login').addEventListener('click', (e) => {
            e.preventDefault();
            document.getElementById('form-register').reset();
            ui.clearErrors(document.getElementById('form-register'));
            ui.showLogin();
        });

        document.getElementById('btn-logout').addEventListener('click', () => {
            db.clearCurrentUser();
            this.checkAuth();
        });

        // Delegacao de eventos para botoes de completar tarefa
        document.getElementById('task-list').addEventListener('click', (e) => {
            const btn = e.target.closest('.btn-complete');
            if (btn && !btn.disabled) {
                handleCompleteTask(btn.dataset.id);
            }
        });
    },

    checkAuth() {
        const user = db.getCurrentUser();
        if (user) {
            ui.showDashboard(user);
            renderTasks();
        } else {
            ui.showLogin();
        }
    }
};

document.addEventListener('DOMContentLoaded', () => app.init());
