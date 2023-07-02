<script setup lang="ts">
import SearchResultCarousel from '@/components/TheSearchResultsCarousel/SearchResultsCarousel.vue'
</script>

<template>
  <div>
    <h2>My recipes</h2>
    <SearchResultCarousel :recipes-to-show="'owned'" />
  </div>
</template>

<style lang="scss"></style>
