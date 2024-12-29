<template>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Flex:opsz,wght@8..144,100..1000&display=swap" rel="stylesheet">
  </head>
  
  <div id="app">
    <div id="main">
      <div class="grid-container">
        <h1 id="logo">
          <img src="./assets/icon.gif" />
        </h1>

        <h3 id="logo2">IoTQuarium</h3>

        <h2 id="dash">|</h2>

        <h1 id="welcome">Welcome back!</h1>

        
      </div>

      <DashBoard />
    </div>

    <footer class="footer" id="footer">
      <div class="footer-content">
        <div class="footer-links">
          <a
            href="https://github.com/IkomovONE/IoTQuarium_Monitoring"
            target="_blank"
            rel="noopener noreferrer"
            >View on GitHub</a
          >
          <a href="/about">About the project</a>

          <a
            href="https://www.flaticon.com/free-animated-icons"
            target="_blank"
            title="animated icons"
            >Animated and other icons created by Freepik - Flaticon</a
          >
        </div>

        <p>
          This is an open-source project. Feel free to contribute, report
          issues, or check out the code!
        </p>
        <p class="footer-copyright">2025 Daniil Komov</p>
      </div>
    </footer>
  </div>
</template>

<script>
import DashBoard from "./components/Dashboard.vue";

export default {
  name: "App",
  components: {
    DashBoard,
  },
  data() {
    return {
      isDarkMode: false, // Default state
    };
  },
  methods: {
    setDarkModeBasedOnSystem() {
      const prefersDarkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;
      this.isDarkMode = prefersDarkMode;
      document.body.setAttribute("data-theme", prefersDarkMode ? "dark" : "light");
    },
  },
  mounted() {
    // Apply dark mode based on the initial system preference
    this.setDarkModeBasedOnSystem();

    // Listen for changes in system preference and update dynamically
    window
      .matchMedia("(prefers-color-scheme: dark)")
      .addEventListener("change", (event) => {
        this.isDarkMode = event.matches;
        document.body.setAttribute("data-theme", event.matches ? "dark" : "light");
      });
  },

};
</script>

<style>
html,
body {
  margin: 0;
  padding: 0;
  height: 100%; /* Ensure the full height is considered */
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  overflow-x: hidden;
  font-family: "Roboto Flex", serif;
  font-optical-sizing: auto;
  font-weight: 100;
  font-style: normal;
  font-variation-settings:
    "slnt" 0,
    "wdth" 100,
    "GRAD" 0,
    "XOPQ" 96,
    "XTRA" 468,
    "YOPQ" 79,
    "YTAS" 750,
    "YTDE" -203,
    "YTFI" 738,
    "YTLC" 514,
    "YTUC" 712;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grawyscale;
  text-rendering: optimizeLegibility;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* Full viewport height */
}

#main {
  flex: 1; /* Pushes the footer down */
}

h1 {
  text-align: start;
}

a {
  position: relative;
  z-index: 10;
}

#logo {
  text-align: start;



}

.footer {
  background-color: #ffffff;
  color: rgb(0, 0, 0);
  padding: 10px 0;
  text-align: center;
}

.footer-links {
  margin-bottom: 10px;
}

.footer-links a {
  color: #8b8b8b;
  margin: 0 15px;
  text-decoration: none;
}

.footer-links a:hover {
  color: rgb(67, 64, 64);
}

.footer-copyright {
  margin-top: 10px;
  font-size: 14px;
}



#welcome {
  position: relative;
  top: 0.2cm;
  left: 2.3cm;
  width: 20cm;
  text-align: start;

  font-weight: 100;
  
}

#dash {
  position: relative;
  left: 2.3cm;
  font-size: xx-large;
  padding-bottom: 0.1cm;

  font-weight: 400;
}

h3 {
  text-align: center;
  padding-top: 0.5cm;

  font-weight: 100;
}

img {
  width: 50px;
  height: 50px;
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(30px, 1fr));
  gap: 30px;
  position: relative;
  left: 0.5cm;
  bottom: 0.2cm;
  padding-bottom: 0.01cm;
}






body[data-theme="dark"] {
  background-color: #0e0d14;
  color: #fdfeff;
}




body[data-theme="dark"] .footer {
  background-color: #21212196; /* Dark background */
  color: #bbbbbb; /* Light text color */
}

/* Adjust footer links for dark mode */
body[data-theme="dark"] .footer-links a {
  color: #ffffffd7; /* Light blue color for links */
}

body[data-theme="dark"] .footer-links a:hover {
  color: #787777; /* Highlighted color on hover */
}

/* Adjust footer copyright for dark mode */
body[data-theme="dark"] .footer-copyright {
  color: #bbbbbb;
}



body[data-theme="dark"] #logo img {
  filter: invert(1);

  


  
}






@media (max-width: 768px) {
  /* Adjust logo size for smaller screens */
  #logo {
    width: 40px;
    height: 40px;
  }

  /* Reduce the padding of the header on smaller screens */
  

  /* Adjust the 'Welcome back' font size for smaller screens */
  #dash {



    left: 1.5cm;

    width: 2cm;


  }

  #welcome {

    
    font-size: large;

    width: 4cm;

    top: 0.7cm;

    left: 0.7cm;

  }

  .footer {
    width: 20.2cm;




  }

  
  

  /* Adjust footer layout for mobile */
  .footer-links {
    display: block;
    text-align: center;

    width: 10.2cm;
  }

  .footer-content {

    width: 10cm;


  }

  .footer-copyright {
    width: 10.2cm;


}
}
</style>
