<script setup lang="ts">
import CarouselOfRecipes from '@/components/TheCarousel/CarouselOfRecipes.vue'
import { ref } from 'vue'

// name should be taken from api
const userName = ref('Cukinia')
const randomEmojis = ['😃', '😍', '😎', '😋', '😉', '👇']
</script>

<template>
  <div>
    <h2>Welcome back {{ userName }}!</h2>
    <h3>
      Check this recipes!
      {{ randomEmojis[Math.floor(Math.random() * (randomEmojis.length - 1))] }}
    </h3>
    <CarouselOfRecipes />
  </div>
</template>

<style lang="scss"></style>
