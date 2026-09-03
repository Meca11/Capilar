document.addEventListener("DOMContentLoaded", function() {
    const procedimento = document.getElementById("procedimento_quimico");
    const tiposQuimica = document.getElementById("tipos_quimica");

    procedimento.addEventListener("change", function() {
        if (procedimento.value === "sim") {
            tiposQuimica.style.display = "block";
        } else {
            tiposQuimica.style.display = "none";
        }      
    });

});