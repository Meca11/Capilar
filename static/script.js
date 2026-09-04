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
const secoes = document.querySelectorAll(".secao-site");
const linksMenu = document.querySelectorAll(".menu-lateral a");

const observer = new IntersectionObserver(
    (entries) => {

        entries.forEach((entry) => {

            if (entry.isIntersecting) {

                linksMenu.forEach((link) => {
                    link.classList.remove("ativo");
                });

                const linkAtual = document.querySelector(
                    `.menu-lateral a[href="#${entry.target.id}"]`
                );

                if (linkAtual) {
                    linkAtual.classList.add("ativo");
                }
            }

        });

    },
    {
        threshold: 0.45
    }
);

secoes.forEach((secao) => {
    observer.observe(secao);
});