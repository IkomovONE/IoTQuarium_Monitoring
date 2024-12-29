<template>

  
  <h2>Dashboard</h2>
  <div class="grid-container">
    <DashWidget  id="big" v-for="widget in widgets.slice(0, 1)" :key="widget.id" :data="widget"  />
    <div class="grid-container-small">

      <DashWidgetSmall id="small" v-for="widget in widgets.slice(3)" :key="widget.id" :data="widget"  />



    </div>
    
    <DashWidget  id="big" v-for="widget in widgets.slice(1, 2)" :key="widget.id" :data="widget"  />
    <DashWidget  id="big" v-for="widget in widgets.slice(2, 3)" :key="widget.id" :data="widget"  />
  </div>
</template>

<script>
import DashWidget from './DashWidget.vue';
import DashWidgetSmall from './DashWidgetSmall.vue';

export default {
  name: 'DashBoard',
  components: {
    DashWidget,
    DashWidgetSmall
  },

  data() {
    return {
      widgets: [
        { id: 1, title: "Water Temperature", description: "24°C", icon: require('@/assets/therm.png') },
        { id: 2, title: "pH value of the water", description: "7.4", icon: require('@/assets/therm.png') },
        { id: 3, title: "Water hardness (GH)", description: "6 dGH", icon: require('@/assets/therm.png') },
        { id: 4, title: "Liquid level", description: "OK", icon: require('@/assets/therm.png') },
        { id: 5, title: "Aquarium Lamp", description: "ON", icon: require('@/assets/therm.png') },
        { id: 6, title: "Filter water flow", description: "Normal", icon: require('@/assets/therm.png') },
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

  position: relative;

  bottom: 0.5cm;

  left: 0.5cm;

  text-align: start;

  font-weight: 100;


}



.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); /* Flexible layout */
  row-gap: 100px;
  column-gap: 1px; /* Reduced column gap */
  position: relative;
  margin: 0 auto; /* Centers the container */
}


   .grid-container-small {

      
      display: grid;
      grid-template-columns: repeat(2, 150px); /* Fixed number of columns */
      grid-auto-rows: 70px; /* Consistent row height */
      row-gap: 85px;
      column-gap: 10px;
      position: relative;

      right: 0.3cm;
      margin-left: 0.3cm; /* Center the grid */

      
}

   #small {

    height: 3cm;

    width: 3cm;


   }

   #big {

    height: 7cm;

    width: 7cm;


    }


    @media (max-width: 768px) {

      .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(400px, 1fr)); /* Flexible layout */
        row-gap: 100px;
        column-gap: 1px; /* Reduced column gap */
        position: relative;
        margin: 0 auto; /* Centers the container */
}







    }


</style>
