<template>
    <div class="bg-white rounded-xl shadow-lg p-4 flex flex-col items-start ">
      
      <h3 class="text-lg font-semibold">{{ data.role }}</h3>
      <h1 class="text-sm text-gray-500">{{ data.content }}</h1>
      
      
      
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
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 15px;
    padding: 10px;
    transition: transform 0.2s ease-in-out;
  }
  
  h3 {
  
    text-align: left;
  
    position: relative;
  
    bottom: 0.8cm;
  
    font-size: 0.4cm;
  
  
  }
  
  img {
  
    position: relative;
  
    left: 6cm;
  
    bottom: 0.7cm;
  
    height: 1cm;
  
    width: 1cm;
  
    filter: invert(1);
  
  
  }
  
  
  h1 {
  
  
  
  position: relative;
  
  
  
  left: 0.1cm;
  
  
  
  bottom: 0.9cm;
  
  
  
  font-size: 0.5cm;
  
  font-weight: 400;
  
  
  }
  
  div:hover {
    transform: scale(1.05);
  }
  
  
  
  body[data-theme="dark"] div {
    background: linear-gradient(195deg, #0f0f48, #131314);
    
    color:  #fdfeff;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 15px;
    padding: 10px;
    transition: transform 0.2s ease-in-out;
  
    width: 10cm;
    height: 5cm;
  }
  
  
  
  @media (max-width: 768px) {


    h1 {

      font-size: small;

    }
    
    
  
    div:hover {
    transform: scale(1);
    }
  
  
  }
  
  @media only screen and (min-width: 768px) and (max-width: 1024px) and (orientation: portrait) {
  
  
  
  div:hover {
    transform: scale(1);
    }
  }
  
  @media only screen and (min-width: 1024px) and (max-width: 1366px) and (orientation: landscape) {
  
  
  
  div:hover {
    transform: scale(1);
    }
  
  
  
  
  }
  
  
  
  </style>