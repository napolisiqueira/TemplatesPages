// Seleção de elementos DOM
const sidebarLinks = document.querySelectorAll('.sidebar__link');
const taskItems = document.querySelectorAll('.task-item__checkbox input');

// Gerenciamento da navegação na sidebar
sidebarLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        // Remove a classe active de todos os links
        sidebarLinks.forEach(l => l.classList.remove('active'));
        // Adiciona a classe active ao link clicado
        e.target.classList.add('active');
    });
});

// Gerenciamento das tarefas
taskItems.forEach(task => {
    task.addEventListener('change', (e) => {
        const taskItem = e.target.closest('.task-item');
        if (e.target.checked) {
            taskItem.classList.add('task-item--completed');
            
            // Simula uma atualização no servidor
            setTimeout(() => {
                taskItem.style.opacity = '0.5';
            }, 300);
        } else {
            taskItem.classList.remove('task-item--completed');
            taskItem.style.opacity = '1';
        }
    });
});

// Mock de dados do voluntário
const volunteerData = {
    name: 'Maria Silva',
    startDate: 'Janeiro 2025',
    completedTasks: 45,
    upcomingEvents: 3,
    trainingProgress: 75
};

// Função para atualizar dados do voluntário
function updateVolunteerStats() {
    const welcomeMessage = document.querySelector('.dashboard__welcome h2');
    welcomeMessage.textContent = `Olá, ${volunteerData.name}!`;
}

// Função para formatar data
function formatDate(date) {
    const options = { 
        day: 'numeric', 
        month: 'short'
    };
    return new Date(date).toLocaleDateString('pt-BR', options);
}

// Função para adicionar nova tarefa
function addTask(taskData) {
    const tasksList = document.querySelector('.tasks-list');
    const taskElement = document.createElement('div');
    taskElement.className = 'task-item';
    taskElement.innerHTML = `
        <label class="task-item__checkbox">
            <input type="checkbox">
            <span class="task-item__check"></span>
        </label>
        <div class="task-item__content">
            <h4>${taskData.title}</h4>
            <p>${taskData.description}</p>
            <span class="task-item__due">${taskData.dueDate}</span>
        </div>
        <span class="task-item__priority task-item__priority--${taskData.priority}">${taskData.priority}</span>
    `;
    tasksList.prepend(taskElement);

    // Adiciona o evento de change no novo checkbox
    const checkbox = taskElement.querySelector('input[type="checkbox"]');
    checkbox.addEventListener('change', (e) => {
        const taskItem = e.target.closest('.task-item');
        if (e.target.checked) {
            taskItem.classList.add('task-item--completed');
            setTimeout(() => {
                taskItem.style.opacity = '0.5';
            }, 300);
        } else {
            taskItem.classList.remove('task-item--completed');
            taskItem.style.opacity = '1';
        }
    });
}

// Função para registrar nova atividade
function registerActivity(activityData) {
    const activityList = document.querySelector('.activity-list');
    const activityElement = document.createElement('div');
    activityElement.className = 'activity-item';
    activityElement.innerHTML = `
        <div class="activity-item__icon">${activityData.icon}</div>
        <div class="activity-item__content">
            <h4>${activityData.title}</h4>
            <p>${activityData.description}</p>
            <span class="activity-item__time">Agora</span>
        </div>
    `;
    activityList.prepend(activityElement);
}

// Event Listeners para botões de ação
document.addEventListener('DOMContentLoaded', () => {
    const registerActivityBtn = document.querySelector('.btn--primary');
    const viewScheduleBtn = document.querySelector('.btn--secondary');

    if (registerActivityBtn) {
        registerActivityBtn.addEventListener('click', () => {
            // Mock de registro de atividade
            const newActivity = {
                icon: '🦮',
                title: 'Nova Atividade',
                description: 'Atividade registrada via dashboard'
            };
            registerActivity(newActivity);
        });
    }

    if (viewScheduleBtn) {
        viewScheduleBtn.addEventListener('click', () => {
            // Aqui poderia abrir um modal com a escala completa
            alert('Visualização da escala completa em desenvolvimento!');
        });
    }

    // Inicializa os dados do voluntário
    updateVolunteerStats();
});

// Exemplo de uso da função addTask
// addTask({
//     title: 'Nova Tarefa',
//     description: 'Descrição da nova tarefa',
//     dueDate: 'Hoje',
//     priority: 'high'
// });