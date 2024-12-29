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
     grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
     

     row-gap: 20px;

     column-gap: 115px;

     

     position: relative;

     

     bottom: 0.1cm;

     left: 0.5cm;

     

   }


   .grid-container-small {
     display: grid;
     grid-template-columns: repeat(auto-fill, minmax(50px, 1fr));
     

     row-gap: 20px;

     column-gap: 70px;

     

     position: relative;

     

     right: 1cm;

     

   }

   #small {

    height: 3cm;

    width: 3cm;


   }

   #big {

    height: 7cm;

    width: 7cm;


    }


</style>
