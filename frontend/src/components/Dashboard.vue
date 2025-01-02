<template>

  
  <h2>Dashboard</h2>
  <div class="grid-container">
    <DashWidget  id="big" v-for="widget in widgets.slice(0, 1)" :key="widget.id" :data="widget"  />
    <div class="grid-container-small">

      <DashWidgetSmall id="small" v-for="widget in widgets.slice(4, 6)" :key="widget.id" :data="widget"  />

      <DashWidgetMid id="mid" v-for="widget in widgets.slice(7,8)" :key="widget.id" :data="widget"  />

      
    </div>

    <div class="grid-container-mid">

      <DashWidgetMid id="mid" v-for="widget in widgets.slice(8,9)" :key="widget.id" :data="widget"  />


      <div class="grid-container-small">



        <DashWidgetSmall id="small" v-for="widget in widgets.slice(6, 7)" :key="widget.id" :data="widget"  />

        

        




      </div>



      
      


    </div>


    <DashWidget  id="big" v-for="widget in widgets.slice(1, 2)" :key="widget.id" :data="widget"  />
    <DashWidget  id="big" v-for="widget in widgets.slice(2, 3)" :key="widget.id" :data="widget"  />


    <DashWidgetLarge  id="large" v-for="widget in widgets.slice(9, 10)" :key="widget.id" :data="widget"  />

    

    
  </div>
  
</template>

<script>
import DashWidget from './DashWidget.vue';
import DashWidgetSmall from './DashWidgetSmall.vue';
import DashWidgetMid from './DashWidgetMid.vue';
import DashWidgetLarge from './DashWidgetLarge.vue';

export default {
  name: 'DashBoard',
  components: {
    DashWidget,
    DashWidgetSmall,
    DashWidgetMid,
    DashWidgetLarge
  },

  data() {
    return {
      widgets: [
        { id: 1, title: "Water Temperature", description: "24°C", icon: require('@/assets/therm.png') },
        { id: 2, title: "pH value of the water", description: "7.4", icon: require('@/assets/therm.png') },
        { id: 3, title: "Water hardness (GH)", description: "6 dGH", icon: require('@/assets/therm.png') },
        { id: 4, title: "Have questions?", description: "Ask me!", icon: require('@/assets/light.png') },
        { id: 5, title: "Liquid level", description: "OK", icon: require('@/assets/water-level.png') },
        { id: 6, title: "Aquarium Lamp", description: "ON", icon: require('@/assets/light.png') },
        { id: 7, title: "Filter water flow", description: "Normal", icon: require('@/assets/waves.png') },
        { id: 8, title: "Recorded at", description: "0.24", icon: require('@/assets/light.png') },
        { id: 9, title: "Daily averages", description: "0.24", icon: require('@/assets/light.png') },
        { id: 10, title: "Overall evaluation", description: "Good conditions! Temperature is appropriate, liquid level is sufficient, pH is balanced, water TDS is normal. You can press 'Ask GPT' to ask me anything!", icon: require('@/assets/light.png') },
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
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); /* Flexible layout */
  row-gap: 30px;
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

.grid-container-mid {

      
  display: grid;

  grid-template-columns: auto;

  
  


  grid-auto-rows: 70px; /* Consistent row height */
  row-gap: 85px;
  column-gap: 10px;
  position: relative;

  right: 0.3cm;
  margin-left: 0.2cm; /* Center the grid */


}

   #small {

    height: 3cm;

    width: 3cm;


   }


   #mid {

    height: 3cm;

    width: 7.25cm;


}

   #big {

    height: 7cm;

    width: 7.25cm;


    }


    #large {

      height: 7cm;

      width: 37.8cm;


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


        #large {

        height: 17cm;

        width: 7.25cm;


        }

    }


</style>
