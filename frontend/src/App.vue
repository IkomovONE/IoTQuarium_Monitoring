<template>



  <div id="main">


    <div class="grid-container">


      <h1 id="logo"><img src="./assets/icon.gif"> </h1>



      <h3>IoTQuarium </h3>



    </div>


    <h1 id="welcome">Welcome back!</h1>
  

  

  
  
    <DashBoard/>


    <footer class="footer">
      <div class="footer-content">
        <div class="footer-links">
          <a href="https://github.com/IkomovONE/IoTQuarium_Monitoring" target="_blank" rel="noopener noreferrer">View on GitHub</a>
          <a href="/about">About the project</a>

          <a href="https://www.flaticon.com/free-animated-icons" target="_blank" title="animated icons">Animated and other icons created by Freepik - Flaticon</a>

          
        </div>
        
        <p>This is an open-source project. Feel free to contribute, report issues, or check out the code!</p>
        <p class="footer-copyright">2025 Daniil Komov</p>
      </div>
    
  
    </footer>


    

  </div>

  
</template>

<script>
import DashBoard from './components/Dashboard.vue'



export default {
  name: 'App',
  components: {
    DashBoard
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000000;
  margin-top: 60px;
}

#main {

  align-items: center;

  


}

h1 {

  text-align: left;


  padding-bottom: 0.1cm;

  
}


a {
  position: relative;
  z-index: 10;
}


#logo {

  padding-bottom: 0.1cm;

  

  text-align: start;


}


.footer {
  background-color: #ffffff;
  color: rgb(0, 0, 0);
  padding-top: 2cm;
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

bottom: 2cm;



text-align: start;


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



     left: 0.2cm;

     
     bottom: 1.5cm;

     padding-bottom: 2cm;
     

   }
</style>
