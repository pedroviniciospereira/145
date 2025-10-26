// Espera o documento carregar completamente
document.addEventListener("DOMContentLoaded", function() {
            
    // Busca os elementos do formulário de cadastro
    const cpfInput = document.getElementById("cpf");
    const form = document.getElementById("colaborador-form"); // Pega o formulário

    // --- IMPORTANTE ---
    // Esta verificação garante que o script só execute se os elementos
    // existirem nesta página (ex: só na 'cadastro.html' e não na 'index.html')
    if (form && cpfInput) {

        // 1. Máscara de CPF simples
        // Esta parte funciona perfeitamente com o Django
        cpfInput.addEventListener("input", function(e) {
            let value = e.target.value.replace(/\D/g, ""); // Remove tudo que não é número
            
            if (value.length > 11) {
                value = value.substring(0, 11);
            }

            // Aplica a formatação
            if (value.length > 9) {
                value = value.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4");
            } else if (value.length > 6) {
                value = value.replace(/(\d{3})(\d{3})(\d{1,3})/, "$1.$2.$3");
            } else if (value.length > 3) {
                value = value.replace(/(\d{3})(\d{1,3})/, "$1.$2");
            }
            
            e.target.value = value;
        });
    }
});