<script setup lang="ts">
import SearchResultCarousel from '@/components/TheSearchResultsCarousel/SearchResultsCarousel.vue'
import Divider from 'primevue/divider'
import { onMounted, ref } from 'vue'
import { RecipesData } from '../database'
import Loader from '@/components/common/Loader.vue'

const items = ref()

onMounted(() => {
  setTimeout(() => {
    RecipesData.getProducts().then((data: any) => (items.value = data))
  }, 2000)
})
</script>

<template>
  <div v-if="items">
    <h2>Favourites</h2>
    <Divider />
    <SearchResultCarousel :items="items" :recipes-to-show="'favourite'" />
  </div>
  <Loader v-else />
</template>

<style lang="scss"></style>
