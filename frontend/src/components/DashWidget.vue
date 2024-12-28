<template>
  <div class="bg-white rounded-xl shadow-lg p-4 flex flex-col items-start ">
    
    <h3 class="text-lg font-semibold">{{ data.title }}</h3>
    <h1 class="text-sm text-gray-500">{{ data.description }}</h1>
    <img :src="data.icon" alt="Widget icon" />
    
    
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
  background: linear-gradient(145deg, #14cbc894, #0815c3);
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

  bottom: 0.8cm;

  font-size: x-large;


}

img {

  position: relative;

  left: 3.5cm;

  bottom: 1cm;

  height: 2.5cm;

  width: 2.5cm;


}


h1 {



position: relative;

top: 1.8cm;

left: 0.2cm;

bottom: 0.8cm;



font-size: xx-large;

font-weight: bold;


}

div:hover {
  transform: scale(1.05);
}
</style>