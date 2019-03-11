<template>
  <div v-cloak id="app">
    <router-view></router-view>
  </div>
</template>

<script>
  export default {
    name: 'app-root'
  }
</script>

<style scoped>
  #app {
    height: 100%;
  }
</style>
