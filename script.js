// Espera o documento carregar completamente
document.addEventListener("DOMContentLoaded", function() {
            
    const form = document.getElementById("colaborador-form");
    const cpfInput = document.getElementById("cpf");
    const successAlert = document.getElementById("alert-success");

    // 1. Simulação de envio do formulário
    form.addEventListener("submit", function(event) {
        // Impede o recarregamento da página (comportamento padrão do form)
        event.preventDefault(); 
        
        // Pega os valores (em um projeto real, você enviaria isso para o backend)
        const nome = document.getElementById("nome").value;
        const cpf = cpfInput.value;
        const funcao = document.getElementById("funcao").value;
        
        console.log("--- Formulário Enviado (Simulação) ---");
        console.log("Nome:", nome);
        console.log("CPF:", cpf);
        console.log("Função:", funcao);
        
        // Mostra o alerta de sucesso
        successAlert.style.display = "block";
        
        // Reseta o formulário
        form.reset();
        // Seta o foco de volta no primeiro campo
        document.getElementById("nome").focus();

        // Esconde o alerta depois de 3 segundos
        setTimeout(function() {
            successAlert.style.display = "none";
        }, 3000);
    });

    // 2. Máscara de CPF simples
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
});

// Espera o documento carregar completamente
document.addEventListener("DOMContentLoaded", function() {
            
    const form = document.getElementById("colaborador-form");
    const cpfInput = document.getElementById("cpf");
    const successAlert = document.getElementById("alert-success");

    // Verifica se estamos na página de cadastro
    if (form && cpfInput && successAlert) {

        // 1. Simulação de envio do formulário
        form.addEventListener("submit", function(event) {
            // Impede o recarregamento da página (comportamento padrão do form)
            event.preventDefault(); 
            
            // Pega os valores (em um projeto real, você enviaria isso para o backend)
            const nome = document.getElementById("nome").value;
            const cpf = cpfInput.value;
            const funcao = document.getElementById("funcao").value;
            
            console.log("--- Formulário Enviado (Simulação) ---");
            console.log("Nome:", nome);
            console.log("CPF:", cpf);
            console.log("Função:", funcao);
            
            // Mostra o alerta de sucesso
            successAlert.style.display = "block";
            
            // Reseta o formulário
            form.reset();
            // Seta o foco de volta no primeiro campo
            document.getElementById("nome").focus();

            // Esconde o alerta depois de 3 segundos
            setTimeout(function() {
                successAlert.style.display = "none";
            }, 3000);
        });

        // 2. Máscara de CPF simples
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
