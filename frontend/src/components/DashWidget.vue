<template>
  <div class="bg-white rounded-xl shadow-lg p-4 flex flex-col items-start">
    <h3 class="text-lg font-semibold">{{ data.title }}</h3>
    <p class="text-sm text-gray-500">{{ data.description }}</p>
    
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
/* Add custom widget styles here */
</style>