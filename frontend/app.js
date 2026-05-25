const buttons = document.querySelectorAll(".panel .button");

buttons.forEach((button) => {
  button.addEventListener("click", (event) => {
    event.preventDefault();
    button.textContent = "Coming soon";
    window.setTimeout(() => {
      button.textContent = "Run preview";
    }, 1100);
  });
});