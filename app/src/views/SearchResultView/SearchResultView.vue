<script setup lang="ts">
import SearchResultCarousel from '@/components/TheSearchResultsCarousel/SearchResultsCarousel.vue'
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
  <SearchResultCarousel :items="items" v-if="items" />
  <Loader v-else />
</template>

<style lang="scss"></style>
