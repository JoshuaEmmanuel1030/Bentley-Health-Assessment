function startScreening() {
  document.getElementById("screening").classList.remove("hidden");
}

function categorizeUser() {
  const mentalHealth = document.getElementById("mentalHealth").value;
  const physicalHealth = document.getElementById("physicalHealth").value;
  const assimilation = document.getElementById("assimilation").value;
  document.getElementById("screeningForm").reset();
  
  if (mentalHealth === "High") {
    displayResource("mentalResource");
  } else if (physicalHealth === "High") {
    displayResource("physicalResource");
  } else if (assimilation === "Low") {
    displayResource("assimilationResource");
  }
}

function displayResource(resourceId) {
  document.getElementById("resources").classList.remove("hidden");
  document.getElementById(resourceId).classList.remove("hidden");
}
