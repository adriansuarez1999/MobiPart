document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("loginModal");
  const openBtn = document.getElementById("openLoginBtn");
  const closeBtn = document.getElementById("closeLoginBtn");

  openBtn.addEventListener("click", () => {
    modal.style.display = "flex";
  });

  closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
  });

  // Cerrar haciendo clic fuera del contenido
  window.addEventListener("click", (event) => {
    if (event.target === modal) {
      modal.style.display = "none";
    }
  });
});
