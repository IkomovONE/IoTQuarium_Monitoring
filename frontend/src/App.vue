<template>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Flex:opsz,wght@8..144,100..1000&display=swap" rel="stylesheet">
  </head>
  
  <div id="app" refs="app">
    <div id="main">
      <div class="grid-container-top-bar">
        <h1 id="logo">
          <img src="./assets/icon.gif" id="logo_img"/>
        </h1>

        <h3 id="logo_title">IoTQuarium</h3>

        <h2 id="dash">|</h2>

        <h1 id="welcome">Welcome back!</h1>

        
      </div>

      <router-view></router-view>
    </div>

    
  </div>
</template>

<script>


export default {
  name: "App",
  components: {
    
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
    scrollToTop() {
        const app = this.$refs.app;  // Get the chat container using ref

        // Ensure it's scrollable and scroll to the bottom
        if (app) {
          app.scrollTop = app.scrollHeight;  // Scroll to the bottom
        }
      }
  },
  mounted() {
    // Apply dark mode based on the initial system preference
    this.setDarkModeBasedOnSystem();

    this.scrollToTop();

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




.no-scroll {
  overflow-y: hidden; /* Disable scrolling */
}

.dash-no-scroll {
  overflow-x: hidden; /* Disable scrolling */
  
}



html,
body {
  background: linear-gradient(360deg, #aac5ff7b 0% 10%, #ffffff);

  
  margin: 0;
  padding: 0;
  height: 100vh;
  overflow: hidden;
  

  min-width: 10vh;
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  
  
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
  z-index: 0;

  overflow-y: auto;

  overflow-x: hidden;

  overscroll-behavior: contain;

  

 
  
  height: 100%; /* Full viewport height */
}





h1 {
  text-align: start;
  z-index: 0;
}

a {
  position: relative;
  z-index: 10;
}

#logo {
  text-align: start;

  filter: drop-shadow(2px 7px 5px 1px rgb(255, 255, 255));

}

#logo_img {
  

  filter: drop-shadow(2px 7px 5px rgb(255, 255, 255));

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

#logo_title {
  text-align: center;
  padding-top: 0.5cm;

  font-weight: 500;
}

img {
  width: 50px;
  height: 50px;

  
}

.grid-container-top-bar {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(30px, 1fr));
  gap: 30px;
  position: relative;
  left: 0.5cm;
  bottom: 0.2cm;
  padding-bottom: 0.01cm;
}






body[data-theme="dark"] {
  background: linear-gradient(180deg, #000000, #131212);
  color: #fdfeff;
  background-color: black;
}




body[data-theme="dark"] .footer {
  background-color: #21212100; /* Dark background */
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



body[data-theme="dark"] #logo  {
  filter: drop-shadow(1px 1px 1px 1px rgb(0, 0, 0));


  
}

body[data-theme="dark"] #logo_img {
  filter: invert(1) drop-shadow(2px 7px 5px rgb(0, 0, 0)) grayscale(90%);

  

}






@media (max-width: 768px) {


  html, body {

    

    box-sizing: border-box;

    min-height: 30%;

    max-height: 100%;

    overflow-x: hidden;

    

    

    

    max-width: 100%;




  }


  .grid-container-top-bar {

    position: sticky;

    top: 0cm;

    

    padding-left: 0.5cm;

    

      

    z-index: 9999;

    background-color: #f7f9fc;

    height: 2.35cm;
  }


  body[data-theme="dark"] .grid-container-top-bar {


    background-color: #000000;

  }

    


  .grid-container-top-bar,
  .grid-container-small {
    max-width: 100%; /* Prevent grids from exceeding viewport width */

}
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

@media only screen and (min-width: 768px) and (max-width: 1024px) and (orientation: portrait) {

  body {

    overflow-x: hidden;





    margin: 0;
    padding: 0;
    box-sizing: border-box;

    }

.footer {


  margin-bottom: 2cm;

  

}

.grid-container-top-bar {

  position: sticky;

  top: 0cm;

    

  z-index: 9999;

  background-color: #f7f9fc;

  height: 2.35cm;



}

body[data-theme="dark"] .grid-container-top-bar {


  background-color: #000000;

}

#logo {

  margin-left: 0.5cm;

  




}

#logo_title {

  margin-left: 0.6cm;
}




}

@media only screen and (min-width: 1024px) and (max-width: 1366px) and (orientation: landscape) {

  


  .grid-container-top-bar {

    position: sticky;


    top: 0;

    

      

    z-index: 9999;

    background-color: #f7f9fc;

    height: 2.35cm;



  }

  body[data-theme="dark"] .grid-container-top-bar {


    background-color: #000000;

  }

  #logo {

    margin-left: 0.5cm;

    


  }

  #logo_title {

    margin-left: 0.6cm;
}


}




</style>
