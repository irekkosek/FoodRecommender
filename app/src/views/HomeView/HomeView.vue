<script setup lang="ts">
import CarouselOfRecipes from '@/components/TheCarousel/CarouselOfRecipes.vue'
import { onMounted, ref } from 'vue'
import Divider from 'primevue/divider'
import Loader from '@/components/common/Loader.vue'
import axios from 'axios'

const items = ref()
const userName = ref()

onMounted(async () => {
  items.value = await axios
    .get('http://127.0.0.1:8000/recipes')
    .then((response) => {
      return response.data
    })
    .catch((err) => console.log(err))
  userName.value = 'Cukinia'
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
