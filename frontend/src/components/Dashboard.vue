<template>
  <h2>Dashboard</h2>
  <div class="grid-container">
    <DashWidget  v-for="widget in widgets" :key="widget.id" :data="widget"  />
    <DashWidget  v-for="widget in widgets" :key="widget.id" :data="widget"  />
    <DashWidget v-for="widget in widgets" :key="widget.id" :data="widget"  />
    <DashWidget v-for="widget in widgets" :key="widget.id" :data="widget"  />
  </div>
</template>

<script>
import DashWidget from './DashWidget.vue';

export default {
  name: 'DashBoard',
  components: {
    DashWidget
  },

  data() {
    return {
      widgets: [
        { id: 1, title: "Water Temperature", description: "24°C", icon: require('@/assets/therm.png') },
        { id: 2, title: "What's Your Plan?", description: "No plan", icon: require('@/assets/therm.png') },
      ],
    };
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

h2 {

  text-align: start;

  



}

.grid-container {
     display: grid;
     grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
     gap: 15px;

     position: relative;

     top: 1cm;

     left: 0.01cm;

     

   }


</style>
