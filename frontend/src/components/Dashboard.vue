<template>

  
  <h2>Dashboard</h2>
  <div class="grid-container">
    <DashWidget  id="big" v-for="widget in widgets.slice(0, 1)" :key="widget.id" :data="widget"  />
    <div class="grid-container-small">

      <DashWidgetSmall id="small" v-for="widget in widgets.slice(3, 5)" :key="widget.id" :data="widget"  />

      <DashWidgetMid id="mid" v-for="widget in widgets.slice(6,7)" :key="widget.id" :data="widget"  />

      
    </div>

    <div class="grid-container-mid">

      <DashWidgetMid id="mid" v-for="widget in widgets.slice(7,8)" :key="widget.id" :data="widget"  />


      <div class="grid-container-small">



        <DashWidgetSmall id="small" v-for="widget in widgets.slice(5, 6)" :key="widget.id" :data="widget"  />

        

        




      </div>



      
      


    </div>


    <DashWidget  id="big" v-for="widget in widgets.slice(1, 2)" :key="widget.id" :data="widget"  />
    <DashWidget  id="big" v-for="widget in widgets.slice(2, 3)" :key="widget.id" :data="widget"  />


    <DashWidgetLarge  id="large" v-for="widget in widgets.slice(8, 9)" :key="widget.id" :data="widget"  />

    

    
  </div>



  <footer class="footer" id="footer">
      <div class="footer-content">
        <div class="footer-links">
          <a
            href="https://github.com/IkomovONE/IoTQuarium_Monitoring"
            target="_blank"
            rel="noopener noreferrer"
            >View on GitHub</a
          >
          <a href="/about">About the project</a>

          <a
            href="https://www.flaticon.com/"
            target="_blank"
            title="animated icons"
            >Animated and other icons created by Freepik - Flaticon</a
          >
        </div>

        <p>
          This is an open-source project. Feel free to contribute, report
          issues, or check out the code!
        </p>
        <p class="footer-copyright">2025 Daniil Komov</p>
      </div>
    </footer>
  
</template>

<script>
import DashWidget from './DashWidget.vue';
import DashWidgetSmall from './DashWidgetSmall.vue';
import DashWidgetMid from './DashWidgetMid.vue';
import DashWidgetLarge from './DashWidgetLarge.vue';
import axios from 'axios';


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
          
        { id: 1, title: "Water Temperature", description: "Loading...", icon: require('@/assets/therm.png') },
        { id: 2, title: "pH value of the water", description: "Loading...", icon: require('@/assets/therm.png') },
        { id: 3, title: "Total Dissolved Solids (ppm)", description: "Loading...", icon: require('@/assets/therm.png') },
        { id: 4, title: "Water level", description: "Loading...", icon: require('@/assets/water-level.png') },
        { id: 5, title: "Aquarium Lamp", description: "Loading...", icon: require('@/assets/light.png') },
        { id: 6, title: "Filter water flow", description: "Loading...", icon: require('@/assets/waves.png') },
        { id: 7, title: "Recorded at", description: "Loading...", icon: require('@/assets/clock.png') },
        { id: 8, title: "Daily averages", description: "Loading...", icon: require('@/assets/chart.png') },
        { id: 9, title: "Overall evaluation", description: "Loading..." },




        ], // Initialize widgets as an empty array
      };
    },

    async mounted() {

      function fixMongoDBString(str) {
          return str
            .replace(/'/g, '"')                      // Replace single quotes with double quotes
            .replace(/ObjectId\((.*?)\)/g, '"$1"')
            .replace(/""(.*?)""/g, '"$1"');   // Replace ObjectId(...) with just the string inside
        }

      function getMonthName(monthNumber) {
        const months = [
          "January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"
        ];
        return months[monthNumber - 1];
      }

      function getDayWithOrdinal(day) {
        const suffixes = ["th", "st", "nd", "rd"];
        const value = day % 100;
        return day + (suffixes[(value - 20) % 10] || suffixes[value] || suffixes[0]);
      }
      try {
        const response = await axios.get('http://192.168.3.29:3000/dashboard/');
        const response_data = response.data;
        console.log(response_data);

        // Assuming response_data is the array you want to use for widgets

        let response_current= response_data[0]

        let response_gpt= response_data[1]

        let response_daily= response_data[2]

        let current_data= response_current["content"]

        let gpt_data= response_gpt["content"]

        let daily_data= response_daily["content"]



        

        // Fix the string before parsing it
        current_data = fixMongoDBString(current_data);

        daily_data = fixMongoDBString(daily_data);

        
        current_data= JSON.parse(current_data);


        daily_data= JSON.parse(daily_data);


        let daily_data_string= "Temp: " + daily_data["AverageTemp"] + " | pH: " + daily_data["AveragepH"] + " | TDS: " + daily_data["AverageTDS"]



        let date= current_data["timestamp"]


        date = new Date(date);






        let dayWithOrdinal = getDayWithOrdinal(date.getDate());
        let monthName = getMonthName(date.getMonth() + 1); // Months are 0-indexed
        let year = date.getFullYear();
        let hours = date.getHours().toString().padStart(2, "0");
        let minutes = date.getMinutes().toString().padStart(2, "0");

        // Combine the formatted date and time
        let formattedDateTime = `${dayWithOrdinal} ${monthName} ${year}, ${hours}:${minutes}`;

        


        this.widgets = [
              { id: 1, title: "Water Temperature", description: current_data["Temp"], icon: require('@/assets/therm.png') },
              { id: 2, title: "pH value of the water", description: current_data["pH"], icon: require('@/assets/therm.png') },
              { id: 3, title: "Total Dissolved Solids (ppm)", description: current_data["TDS"], icon: require('@/assets/therm.png') },
              { id: 4, title: "Water level", description: current_data["WaterLevel"], icon: require('@/assets/water-level.png') },
              { id: 5, title: "Aquarium Lamp", description: current_data["LightNow"], icon: require('@/assets/light.png') },
              { id: 6, title: "Filter water flow", description: current_data["WaterFlow"], icon: require('@/assets/waves.png') },
              { id: 7, title: "Recorded at", description: formattedDateTime, icon: require('@/assets/clock.png') },
              { id: 8, title: "Daily averages", description: daily_data_string, icon: require('@/assets/chart.png') },
              { id: 9, title: "Overall evaluation", description: gpt_data },
            ];




      } catch (error) {
        console.error('Error fetching sensor data:', error);

        this.widgets= [
          
        { id: 1, title: "No response from server / Server error, make sure it is online", description: "", icon: require('@/assets/therm.png') },
        



        ]
      }
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
    isolation: isolate;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); /* Flexible layout */
    grid-auto-rows: auto;
    row-gap: 20px;
    column-gap: 0px; /* Reduced column gap */
    position: relative;
    margin: 0 auto; /* Centers the container */
    z-index: 0;
    min-height: 61.5%;

    
  }


  .grid-container-small {

    
    display: grid;
    grid-template-columns: repeat(2, 150px); /* Fixed number of columns */
    grid-auto-rows: 70px; /* Consistent row height */
    row-gap: 85px;
    column-gap: 10px;
    position: relative;
    z-index: 0;
    right: 0.3cm;
    margin-left: 0.3cm; /* Center the grid */

    
  }

  .grid-container-mid {

        
    display: grid;

    grid-template-columns: auto;

    
    
    z-index: 0;

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


  #mid {

  height: 3cm;

  width: 7.25cm;


  }

  #big {

  height: 7cm;

  width: 7.25cm;
  z-index: 8000;


  }


  #large {

    height: 7cm;

    width: 26.3cm;

    grid-column: span 3;


  }


  .footer {
    background-color: #adc6fc;
    color: rgb(0, 0, 0);
    padding: 10px 0;
    text-align: center;

    margin-top: 1cm;

    
  }

  .footer-links {
    margin-bottom: 10px;
  }

  .footer-links a {
    color: #0022fc;
    margin: 0 15px;
    text-decoration: none;
  }

  .footer-links a:hover {
    color: rgb(67, 64, 64);
  }

  .footer-copyright {
    margin-top: 10px;
    font-size: 14px;
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

    grid-column: span 1;


    }

    .footer {
    width: 20.2cm;
  }

  /* Adjust footer layout for mobile */
  .footer-links {
    display: block;
    text-align: center;

    width: 10.2cm;
  }

  .footer-content {

    width: 10cm;


  }

  .footer-copyright {
    width: 10.2cm;


}

  }

  @media only screen and (min-width: 768px) and (max-width: 1024px) and (orientation: portrait) {

    #large {

      width: 16.3cm;

      grid-column: span 2;


    }

    #big {

      grid-column: span 1;


    }

    .grid-container-small {

      

      grid-column: span 2;

   

    }


    .grid-container-mid {

      

      grid-column: span 3;

      margin-bottom: 2cm






    }

    .grid-container {

      

      grid-template-columns: repeat(auto-fill, minmax(250px, 9cm));

      margin-bottom: 2cm


    }

    body {

      max-width: 100%;

      overflow-x: hidden;


    }

  

  }

  @media only screen and (min-width: 1024px) and (max-width: 1366px) and (orientation: landscape) {

    #large {

    left: 14.5cm;


    }

    .grid-container-mid {

      

      grid-column: span 1;

      margin-bottom: 2cm




      }

      .grid-container {

      

        grid-template-columns: repeat(auto-fill, minmax(250px, 9cm));

      

      }

      .grid-container-small {

      

        grid-column: span 1;



}

      
  }


</style>
