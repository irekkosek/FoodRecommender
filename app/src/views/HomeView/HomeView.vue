<script setup lang="ts">
import CarouselOfRecipes from '@/components/TheCarousel/CarouselOfRecipes.vue'
import { onMounted, ref } from 'vue'
import Divider from 'primevue/divider'
import { RecipesData } from '../database'
import Loader from '@/components/common/Loader.vue'

const items = ref()
const userName = ref()

onMounted(() => {
  setTimeout(() => {
    RecipesData.getProducts().then((data: any) => (items.value = data))
    // name should be taken from api
    userName.value = 'Cukinia'
  }, 2000)
})

const randomEmojis = ['😃', '😍', '😎', '😋', '😉', '👇']
</script>

<template>
  <div v-if="items">
    <div class="headers">
      <h2>Welcome back {{ userName }}!</h2>
      <h3>
        Check out this recipes!
        {{ randomEmojis[Math.floor(Math.random() * (randomEmojis.length - 1))] }}
      </h3>
    </div>

    <Divider />
    <CarouselOfRecipes :items="items" />
  </div>
  <Loader v-else />
</template>

<style lang="scss"></style>
