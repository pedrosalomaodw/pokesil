// Função para verificar se o elemento está visível na janela de visualização
function isElementVisible(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Função para adicionar animações aos elementos visíveis na janela de visualização
function addScrollAnimations() {
    const elements = document.querySelectorAll('.scroll-animation');
    elements.forEach(element => {
        if (isElementVisible(element)) {
            element.classList.add('animate__animated', 'animate__fadeInUp');
        }
    });
}

// Adiciona evento de scroll para chamar a função addScrollAnimations
window.addEventListener('scroll', addScrollAnimations);

// Chama a função uma vez para animar elementos já visíveis na carga da página
addScrollAnimations();
