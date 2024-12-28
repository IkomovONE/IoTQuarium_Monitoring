<template>

  <h1>————————</h1>
  <h2>Dashboard</h2>
  <div class="grid-container">
    <DashWidget  id="big" v-for="widget in widgets.slice(0, 3)" :key="widget.id" :data="widget"  />
    <DashWidgetSmall id="small" v-for="widget in widgets.slice(3)" :key="widget.id" :data="widget"  />
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
        { id: 2, title: "Light", description: "No plan", icon: require('@/assets/therm.png') },
        { id: 3, title: "What's Your Plan?", description: "No plan", icon: require('@/assets/therm.png') },
        { id: 4, title: "Water Temperature", description: "24°C", icon: require('@/assets/therm.png') },
        { id: 5, title: "What's Your Plan?", description: "No plan", icon: require('@/assets/therm.png') },
        { id: 6, title: "What's Your Plan?", description: "No plan", icon: require('@/assets/therm.png') },
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

  bottom: 2.7cm;

  text-align: start;


}

h1 {

position: relative;

bottom: 2cm;

text-align: start;





}

.grid-container {
     display: grid;
     grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
     

     row-gap: 20px;

     column-gap: 50px;

     

     position: relative;

     

     bottom: 2cm;

     left: 0.01cm;

     

   }

   #small {

    height: 3cm;

    width: 3cm;


   }

   #big {

    height: 6cm;

    width: 6cm;


    }


</style>
