<template>
  <h1>Welcome back to IoTQuarium!

    
  </h1>

  
  
  <h2>Dashboard</h2>
  
  <DashBoard/>
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
  color: #2c3e50;
  margin-top: 60px;
}

h1 {

  text-align: left;
  


}

h2 {

text-align: left;



}
</style>
