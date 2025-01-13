<template>
  <div  @mouseleave="toggleInfoFalse" class="bg-white rounded-xl shadow-lg p-4 flex flex-col items-start ">
    
    <h3 class="text-lg font-semibold">{{ data.title }}</h3>
    <h1 class="text-sm text-gray-500">{{ data.description }}</h1>

    <button  @click="toggleInfo" class="bg-white rounded-xl shadow-lg p-4 flex flex-col items-start "><a id="i">i</a></button>

    <div v-if="showInfo" class="context-window">
      <p>{{ infoText }}</p>
    </div>


    

   
    
    
  </div>

  
</template>

<script>
export default {
  name: 'DashWidget',
  props: {
    data: Object,
  },
  data() {

    return {

      showInfo: false,
      infoText: '',
    }
  },
  methods: {

    toggleInfoFalse() {
      this.showInfo = false; // Toggle the context window
    },

    toggleInfo() {
      this.showInfo = !this.showInfo; // Toggle the context window
    },

    handleClickOutside(event) {
      if (this.$refs.contextWindow && !this.$refs.contextWindow.contains(event.target)) {
        this.showInfo = false; // Close the context window if click is outside
      }
    },
  


  },
  mounted() {

    document.addEventListener('click', this.handleClickOutside);

    if (this.data.title== "Total Dissolved Solids (ppm)") {

      this.infoText= "Total Dissolved Solids (TDS) in an aquarium measure the concentration of dissolved substances, including salts and minerals. The optimal TDS range typically lies between 200-400 ppm for freshwater aquariums, depending on the species kept. Lower TDS indicates better water quality and is essential for fish health, promoting osmoregulation and reducing stress. High TDS levels can lead to poor water quality, affecting fish behavior and overall well-being. Regular monitoring helps ensure a stable environment, promoting a thriving aquarium ecosystem."

    }

    if (this.data.title== "pH value of the water") {

      this.infoText= "The optimal pH range for most freshwater aquariums is between 6.5 and 7.5. A pH of 7.0 is neutral, which is ideal for many species. It's important to maintain stable pH levels because extreme fluctuations can stress fish, leading to health issues. Certain species are more sensitive to pH changes, and maintaining the correct range ensures the well-being of the aquatic life and the effectiveness of beneficial bacteria in the filtration system. Regular monitoring and gradual adjustments are key to keeping the environment healthy."

    }

    if (this.data.title== "Water Temperature") {

      this.infoText= "The optimal temperature range for most freshwater aquarium fish is typically between 22°C and 28°C. Each species has specific temperature needs. Maintaining a stable temperature is crucial because fluctuations can cause stress, weaken immune systems, and lead to illness. Proper temperature regulation also supports the overall health of beneficial bacteria, which are vital for biological filtration. Regular monitoring with a reliable thermometer ensures a healthy environment for your aquatic life."

    }



  }
};
</script>

<style scoped>

.context-window {
  position: relative;
  
  bottom: 10cm;
  
  left: 0cm;
  width: 7cm;
  height: fit-content;
  padding: 10px;
  background-color: #ffffff;
  color: #ffffff;
  border: 1px solid #ccc;
  border-radius: 1px 30px 10px 30px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  opacity: 100%;
  animation: fadeInScale 0.4s forwards;;  /* Animation to show the context window */
  z-index: 99999;
  
}

.context-window p {
  margin: 0;
  font-size: 0.45cm;
  font-weight: 100;
  text-align: start;
 
}

/* Animation for the context window */
@keyframes fadeInScale {
  from {
    opacity: 0;
    transform: scale(0.8);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* Optional: Dark theme adjustments */
body[data-theme="dark"] .context-window {
  background-color: #262a5c;
  color: #e6e6e6;
  border: 1px solid #444;
  border-radius: 1px 30px 10px 30px;

}

div {
  background: linear-gradient(145deg, #14cbc894, #3f4aee);
  color: #ffffff;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 15px;
  padding: 10px;
  transition: transform 0.2s ease-in-out;

  width: 10cm;
  height: 5cm;
}

h3 {

  text-align: left;

  position: relative;

  bottom: 1.45cm;

  font-size: 1cm;


}

#i {

text-align: center;

position: relative;

bottom: 0.1cm;

font-size: 0.7cm;

font-weight: 100;


}

button {

  position: relative;

  text-align: center;


  bottom: 1.8cm;

  left: 5.8cm;

  font-size: 1cm;

  font-style: normal;

  border-width: 0cm;

  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);

  

  width: 1.3cm;
  height: 1.3cm;

  /*background: linear-gradient(145deg, #14cbc894, #3f4aee);*/

  background: linear-gradient(145deg, #3d7f99b6, #51b3ddab);
  color: #ffffff;

  border-radius: 20px;

  transition: transform 0.4s ease-in-out;

  

  


}

body[data-theme="dark"] button {
  background: linear-gradient(195deg, #20202caf, #262a5c);
  
  color:  #fdfeff;
  box-shadow: 7px 7px 15px #080919, -7px -7px 15px #080919;
  
  
  transition: transform 0.2s ease-in-out;

  
}

button:hover {
  transform: scale(1.1);
}


h1 {



position: relative;

top: 0.6cm;

left: 0.3cm;



font-size: 1.3cm;

font-weight: 400;


}

div:hover {
  transform: scale(1.05);
}


body[data-theme="dark"] div {
  background: linear-gradient(195deg, #0f0f48, #1b1b1d);
  
  color:  #fdfeff;
  box-shadow: 7px 7px 15px #080919, -7px -7px 15px #080919;
  border-radius: 15px;
  padding: 10px;
  transition: transform 0.2s ease-in-out;

  
}


body[data-theme="dark"] button {

  color: #e6e6e6;

  background-color: #262a5c;

  box-shadow: 10px 10px 10px #26295438, -1px -1px 10px #21245153;
  

  
}

@media (max-width: 768px) {

  .context-window {

    position: absolute;
    top: 0.5cm;
    bottom: 0cm;
    
    left: 0cm;
    width: 7cm;
    height: fit-content;
    padding: 10px;

    
   
    
  }

  .context-window p {
    margin: 0;
    font-size: 0.45cm;
    font-weight: 100;
    text-align: start;
  
  }
  
  button {

    left: 5.3cm;

    

    

  }

  div:hover {
  transform: scale(1);
  }


}


@media only screen and (min-width: 768px) and (max-width: 1024px) and (orientation: portrait) {

  .context-window {

    position: absolute;
    top: 0.5cm;
    bottom: 0cm;

    left: 0cm;
    width: 7cm;
    height: fit-content;
    padding: 10px;




    }

  button {

    left: 5.2cm;

    width: 2cm;


  }
  div:hover {
    transform: scale(1);
  }
}

@media only screen and (min-width: 1024px) and (max-width: 1366px) and (orientation: landscape) {

  .context-window {

    position: absolute;
    
    bottom: 0.5cm;

    left: 0cm;
    width: 8cm;
    height: fit-content;
    padding: 10px;




    }

button {

  left: 5.2cm;

  width: 2cm;


}

div:hover {
  transform: scale(1);
}




}




</style>