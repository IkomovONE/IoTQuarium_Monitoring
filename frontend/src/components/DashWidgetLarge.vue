<template>
  <div class="bg-white rounded-xl shadow-lg p-4 flex flex-col items-start ">
    
    <h3 class="text-lg font-semibold">{{ data.title }}</h3>
    <h1 class="text-sm text-gray-500">{{ data.description }}</h1>

  <div id="buttons">

    

    <button @click="goToChat">Ask GPT</button>


  </div>

    

   
    
    
  </div>
</template>

<script>
export default {
  name: 'DashWidget',
  props: {
    data: Object,
  },
  methods: {
    goToChat() {
      this.$router.push('/chat'); // Navigate to the Chat view
    },
  },
};
</script>

<style scoped>

div {
  background: linear-gradient(145deg, #14cbc894, #3f4aee);
  color: #ffffff;
  box-shadow: 5px 5px 15px #bebebe, -5px -5px 15px #ffffff;
  border-radius: 15px;
  padding: 10px;
  transition: transform 0.2s ease-in-out;
  
  width: 10cm;
  height: 5cm;
}

#buttons {

  box-shadow: none;

  background: none;

  width: fit-content;

  height: fit-content;

  


  position: relative;

  bottom: 2cm;

  left: 20cm;

  

}

h3 {

  text-align: left;

  position: relative;

  bottom: 1.45cm;

  font-size: 1cm;

  font-weight: 400;


}

#i {

text-align: center;

position: relative;



font-weight: 100;

font-size: 0.5cm;




}




button {

  position: relative;

  text-align: center;


  

  font-weight: lighter;

  font-size: large;

  margin-right: 0.5cm;

  

  border-width: 0cm;

  
  background: linear-gradient(145deg, #14cbc894, #3f4aee);
  color: #ffffff;
  box-shadow: 10px 10px 10px #26295475, -1px -1px 10px #21245178;
  border-radius: 20px;
  padding: 10px;
  transition: transform 0.2s ease-in-out;

  height: 1.5cm;

  width: 6cm;

 



}



button:hover {
  transform: scale(1.03);
}


h1 {



position: relative;

bottom: 1.5cm;

left: 0.3cm;

width: 26cm;
z-index: 0;

height: 2.9cm;



font-size: 0.8cm;

font-weight: 100;


}

div:hover {
  transform: scale(1.01);

  
}

#buttons:hover {
  transform: scale(1);
}


body[data-theme="dark"] div {
  background: linear-gradient(195deg, #0f0f48, #131314);
  
  color:  #fdfeff;
  box-shadow: 7px 7px 15px #080919, -7px -7px 15px #080919;
  border-radius: 15px;
  padding: 10px;
  transition: transform 0.2s ease-in-out;

  
}


body[data-theme="dark"] button {
  background: linear-gradient(195deg, #20202caf, #262a5c);
  
  color:  #fdfeff;
  box-shadow: 7px 7px 15px #080919, -7px -7px 15px #080919;
  
  
  transition: transform 0.2s ease-in-out;

  
}

@media (max-width: 768px) {
  
  #buttons {

    

    bottom: 1cm;

    left: 0.3cm;

  }

  button {

    margin-bottom: 0.3cm;

  }

  div:hover {
  transform: scale(1);
  }

  h1 {

    width: 7cm;

    height: 10cm;

    font-size: 0.7cm;




  }


}


@media only screen and (min-width: 768px) and (max-width: 1024px) and (orientation: portrait) {

  #buttons {

    left: 10cm;

    margin-top: 0cm;

    bottom: 1.8cm;

    


}

h1 {

  font-size: 0.6cm;

  width: 16cm;

}

  div:hover {
    transform: scale(1);
    }
  }

@media only screen and (min-width: 1024px) and (max-width: 1366px) and (orientation: landscape) {

  #buttons {

    left: 20cm;


  }

  div:hover {
    transform: scale(1);
    }




  }




</style>