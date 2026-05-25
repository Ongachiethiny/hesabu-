const routes = {
  mechanical: "/api/calculators/mechanical/preview",
  structural: "/api/calculators/structural/preview",
  electrical: "/api/calculators/electrical/preview",
};

document.querySelectorAll("[data-calculator]").forEach((card) => {
  const calculator = card.dataset.calculator;
  const button = card.querySelector("button");
  const result = card.querySelector(".result");
  const formFields = card.querySelectorAll("input");

  button.addEventListener("click", async (event) => {
    event.preventDefault();

    const payload = {};
    formFields.forEach((field) => {
      payload[field.name] = field.type === "number" ? Number(field.value) : field.value;
    });

    button.disabled = true;
    button.textContent = "Running...";
    result.textContent = "Calling backend preview endpoint...";

    try {
      const response = await fetch(routes[calculator], {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }

      const data = await response.json();
      result.textContent = `${data.domain.toUpperCase()} preview\n${JSON.stringify(data.result, null, 2)}`;
    } catch (error) {
      result.textContent = `Unable to reach the backend: ${error.message}`;
    } finally {
      button.disabled = false;
      button.textContent = "Run preview";
    }
  });
});