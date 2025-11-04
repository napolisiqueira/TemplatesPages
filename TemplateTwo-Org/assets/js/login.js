// Dados de login mock (em produção isso seria validado no backend)
const MOCK_USERS = {
    'admin@instituto.org': {
        password: 'admin123',
        type: 'admin',
        redirect: 'admin-dashboard.html'
    },
    'voluntario@instituto.org': {
        password: 'voluntario123',
        type: 'volunteer',
        redirect: 'volunteer-dashboard.html'
    }
};

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const togglePasswordBtn = document.querySelector('.login-form__toggle-password');

    // Toggle password visibility
    togglePasswordBtn.addEventListener('click', () => {
        const type = passwordInput.type === 'password' ? 'text' : 'password';
        passwordInput.type = type;
        togglePasswordBtn.querySelector('.login-form__eye-icon').style.opacity = 
            type === 'password' ? '0.5' : '1';
    });

    // Handle form submission
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = emailInput.value.trim();
        const password = passwordInput.value;

        // Remove previous error states
        removeErrors();

        // Validate credentials
        if (!validateCredentials(email, password)) {
            showError('Email ou senha incorretos');
            return;
        }

        // Show loading state
        const submitBtn = loginForm.querySelector('.login-form__submit');
        submitBtn.classList.add('loading');
        submitBtn.disabled = true;

        // Simulate API call
        setTimeout(() => {
            const user = MOCK_USERS[email];
            window.location.href = user.redirect;
        }, 1500);
    });

    function validateCredentials(email, password) {
        const user = MOCK_USERS[email];
        return user && user.password === password;
    }

    function showError(message) {
        // Add error class to inputs
        emailInput.classList.add('error');
        passwordInput.classList.add('error');

        // Create error message
        const errorDiv = document.createElement('div');
        errorDiv.className = 'login-form__error';
        errorDiv.textContent = message;

        // Insert error message after password group
        const passwordGroup = passwordInput.closest('.login-form__group');
        passwordGroup.insertAdjacentElement('afterend', errorDiv);
    }

    function removeErrors() {
        // Remove error classes
        emailInput.classList.remove('error');
        passwordInput.classList.remove('error');

        // Remove error messages
        const errorMessage = loginForm.querySelector('.login-form__error');
        if (errorMessage) {
            errorMessage.remove();
        }
    }
});