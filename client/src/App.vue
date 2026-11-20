<script setup>
import NavBar from './components/NavBar.vue';
</script>

<template>

  <NavBar></NavBar>

    <div class = "container mt-4">
        <router-view></router-view>
    </div>

</template>

<style scoped>
</style>
