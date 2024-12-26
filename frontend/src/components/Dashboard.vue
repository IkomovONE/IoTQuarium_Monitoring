<template>
  <div class="grid grid-cols-3 gap-4 p-4">
    <DashWidget v-for="widget in widgets" :key="widget.id" :data="widget" />
    <DashWidget v-for="widget in widgets" :key="widget.id" :data="widget" />
    <DashWidget v-for="widget in widgets" :key="widget.id" :data="widget" />
    <DashWidget v-for="widget in widgets" :key="widget.id" :data="widget" />
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
        { id: 1, title: "Latest Uploads", description: "987 files", icon: "icon1.png" },
        { id: 2, title: "What's Your Plan?", description: "36°C, looks like a shady day", icon: "icon2.png" },
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

.widget {
  background: linear-gradient(145deg, #ececec, #ffffff);
  box-shadow: 5px 5px 15px #bebebe, -5px -5px 15px #ffffff;
  border-radius: 12px;
  padding: 16px;
  transition: transform 0.2s ease-in-out;
}

.widget:hover {
  transform: scale(1.05);
}
</style>
