// modal.js
const infoButtons = document.querySelectorAll(".uiverse");
const modalOverlay = document.querySelector(".modal-overlay");
const modalContainer = document.querySelector(".modal-container");
const closeBtn = document.querySelector(".close-btn");
const modalPhoto = document.querySelector("#modal-photo");
const modalNom = document.querySelector("#modal-nom");
const modalPrenom = document.querySelector("#modal-prenom");
const modalSexe = document.querySelector("#modal-sexe");
const modalParent = document.querySelector("#modal-parent");
const modalTel = document.querySelector("#modal-tel");
const modalEmailParent = document.querySelector("#modal-email-parent");
const modalDateNaissance = document.querySelector("#modal-date-naissance");
const modalSection = document.querySelector("#modal-section");
// ... autres éléments du formulaire ...

function showModal() {
    modalOverlay.classList.add("modal-show");
    modalContainer.classList.add("modal-show");
}

function hideModal() {
    modalOverlay.classList.remove("modal-show");
    modalContainer.classList.remove("modal-show");
}

infoButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
        event.preventDefault();
        showModal();
          // Récupérer les données de l'enfant à partir des attributs personnalisés du bouton
          const id = button.dataset.id;
          const nom = button.dataset.nom;
          const prenom = button.dataset.prenom;
          const sexe = button.dataset.sexe;
          const parent = button.dataset.parent;
          const telParent = button.dataset.tel;
          const emailParent = button.dataset.email_parent;
          const dateNaissance = button.dataset.date_naissance;
          const photoUrl = button.dataset.photo;
          const section = button.dataset.section;
  
          // Afficher les informations de l'enfant dans le modal
          modalNom.textContent = nom;
          modalPrenom.textContent = prenom;
          modalSexe.textContent = sexe;
          modalParent.textContent = parent;
          modalTel.textContent = telParent;
          modalEmailParent.textContent = emailParent;
          modalDateNaissance.textContent = dateNaissance;
          modalPhoto.src = photoUrl;
          modalSection.textContent = section;
    });
});

modalOverlay.addEventListener("click", hideModal);
closeBtn.addEventListener("click", hideModal);
