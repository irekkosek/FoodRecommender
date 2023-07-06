<script setup lang="ts">
import CarouselOfRecipes from '@/components/TheCarousel/CarouselOfRecipes.vue'
import { onMounted, ref } from 'vue'
import Divider from 'primevue/divider'
import Loader from '@/components/common/Loader.vue'
import axios from 'axios'
import { useUserLoginStore } from '@/stores/userLogin'

const userLogin = useUserLoginStore()
const items = ref([])
const userName = ref()

onMounted(async () => {
  const recipesIds = await axios
    .get(`http://127.0.0.1:8000/recommend/${userLogin.getUserId()}?debug=false&verbose=true`)
    .then((response) => {
      return response.data
    })
    .catch((err) => console.log(err))

  const array = recipesIds.slice(1, -1).split(',')

  array.forEach(async (id: any) => {
    const recipe = await axios
      .get(`http://127.0.0.1:8000/recipes/${id}`)
      .then((response) => {
        return response.data
      })
      .catch((err) => console.log(err))
    if (!recipe) return
    items.value.push(recipe[0] as never)
  })
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
