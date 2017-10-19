// ================= Colocar nome da empresa no botão 'submit' do Modal ================ //

var botaoEmpresa = document.querySelectorAll(".rx");
var botaoForm = document.querySelector(".modal_enviar");

for(var i = 0; i < botaoEmpresa.length; i++){
    botaoEmpresa[i].addEventListener("click", function(){
        var valorBotaoEmpresa = this.getAttribute("empresa");
        botaoForm.value = "Enviar_Modal" + valorBotaoEmpresa;
    });
}