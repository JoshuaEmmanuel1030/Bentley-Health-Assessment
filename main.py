import streamlit as st

# HTML, CSS, and JavaScript content for the app
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bentley WellConnect</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f9;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      margin: 0;
    }

    .container {
      text-align: center;
      background-color: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
      max-width: 400px;
      width: 90%;
    }

    button {
      background-color: #005a9e;
      color: #fff;
      padding: 10px 15px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    button:hover {
      background-color: #004080;
    }

    .hidden {
      display: none;
    }

    .resource {
      margin-top: 15px;
    }

    h1, h2 {
      color: #005a9e;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Welcome to Bentley WellConnect</h1>
    <p>This app will guide you to resources tailored to your well-being needs. Start the screening to begin.</p>
    <button onclick="startScreening()">Start Screening</button>

    <div id="screening" class="hidden">
      <h2>Screening Questions</h2>
      <form id="screeningForm">
        <label>How would you describe your current mental health?</label>
        <select id="mentalHealth">
          <option value="">Choose one</option>
          <option value="High">Struggling</option>
          <option value="Medium">Somewhat Okay</option>
          <option value="Low">Doing Well</option>
        </select>

        <label>How would you rate your physical health?</label>
        <select id="physicalHealth">
          <option value="">Choose one</option>
          <option value="High">Struggling</option>
          <option value="Medium">Somewhat Okay</option>
          <option value="Low">Doing Well</option>
        </select>

        <label>How connected do you feel to the Bentley community?</label>
        <select id="assimilation">
          <option value="">Choose one</option>
          <option value="Low">Not Very Connected</option>
          <option value="Medium">Somewhat Connected</option>
          <option value="High">Very Connected</option>
        </select>

        <button type="button" onclick="categorizeUser()">Submit</button>
      </form>
    </div>

    <div id="resources" class="hidden">
      <h2>Your Suggested Resources</h2>
      <div id="mentalResource" class="resource hidden">
        <p>It looks like you might benefit from mental health support.</p>
        <button onclick="window.location.href='https://www.bentley.edu/university-life/student-health/wellness-prevention'">Get Mental Health Support</button>
      </div>
      <div id="physicalResource" class="resource hidden">
        <p>It looks like you might benefit from physical health resources.</p>
        <button onclick="window.location.href='https://www.bentley.edu/university-life/student-health/health-center'">Access Physical Health Resources</button>
      </div>
      <div id="assimilationResource" class="resource hidden">
        <p>It looks like you might benefit from community connections.</p>
        <button onclick="window.location.href='COMMUNITY_LINK1'">Bentley Student Organizations</button>
        <button onclick="window.location.href='COMMUNITY_LINK2'">Support Groups</button>
        <button onclick="window.location.href='COMMUNITY_LINK3'">Clubs</button>
      </div>
    </div>
  </div>

  <script>
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
  </script>
</body>
</html>
"""

# Render HTML content in Streamlit
st.components.v1.html(html_content, height=800, scrolling=True)

