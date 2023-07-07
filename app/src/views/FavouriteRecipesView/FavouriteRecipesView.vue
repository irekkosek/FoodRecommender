<script setup lang="ts">
import SearchResultCarousel from '@/components/TheSearchResultsCarousel/SearchResultsCarousel.vue'
import Divider from 'primevue/divider'
import { onMounted, ref } from 'vue'
import Loader from '@/components/common/Loader.vue'
import axios from 'axios'
import { useUserLoginStore } from '@/stores/userLogin'

const userLogin = useUserLoginStore()

const items = ref()

onMounted(async () => {
  items.value = await axios
    .get(`http://127.0.0.1:8000/liked-recipes/${userLogin.getUserId()}`)
    .then((response) => {
      return response.data.map((obj: any) => ({ ...obj, USER_likes_RECIPES: 1 }))
    })
    .catch((err) => console.log(err))
})
</script>

<template>
  <div v-if="items">
    <h2>Favourites</h2>
    <Divider />
    <SearchResultCarousel :items="items" :show-sorting="false" />
  </div>
  <Loader v-else />
</template>

<style lang="scss"></style>
