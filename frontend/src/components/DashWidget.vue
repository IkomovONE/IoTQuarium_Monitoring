<template>
  <div class="bg-white rounded-xl shadow-lg p-4 flex flex-col items-start ">
    
    <h3 class="text-lg font-semibold">{{ data.title }}</h3>
    <h1 class="text-sm text-gray-500">{{ data.description }}</h1>

    <button class="bg-white rounded-xl shadow-lg p-4 flex flex-col items-start "><a id="i">i</a></button>
    
    
  </div>
</template>

<script>
export default {
  name: 'DashWidget',
  props: {
    data: Object,
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

  left: 5.45cm;

  font-size: 1cm;

  font-style: normal;

  border-width: 0cm;

  box-shadow: 10px 10px 10px #26295475, -1px -1px 10px #21245178;

  

  width: 1.3cm;
  height: 1.3cm;

  color: #000000;

  background-color: #f0f1f4e1;

  border-radius: 20px;

  transition: transform 0.4s ease-in-out;

  

  


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
  
  button {

    left: 4.8cm;

    

    

  }


}


@media only screen and (min-width: 768px) and (max-width: 1024px) and (orientation: portrait) {

  button {

    left: 4.8cm;





}
}

@media only screen and (min-width: 1024px) and (max-width: 1366px) and (orientation: landscape) {

button {

  left: 4.8cm;





}




}




</style>