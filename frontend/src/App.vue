<template>
  <div id="app">
    <div id="main">
      <div class="grid-container">
        <h1 id="logo">
          <img src="./assets/icon.gif" />
        </h1>

        <h3>IoTQuarium</h3>

        <h2 id="dash">|</h2>

        <h1 id="welcome">Welcome back!</h1>
      </div>

      <DashBoard />
    </div>

    <footer class="footer">
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
};
</script>

<style>
html,
body {
  margin: 0;
  padding: 0;
  height: 100%; /* Ensure the full height is considered */
  display: flex;
  flex-direction: column;
  font-family: Avenir, Helvetica, Arial, sans-serif;
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
}

#dash {
  position: relative;
  left: 2.3cm;
  font-size: xx-large;
  padding-bottom: 0.1cm;
}

h3 {
  text-align: center;
  padding-top: 0.5cm;
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
</style>
