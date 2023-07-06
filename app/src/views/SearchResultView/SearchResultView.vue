<script setup lang="ts">
import SearchResultCarousel from '@/components/TheSearchResultsCarousel/SearchResultsCarousel.vue'
import { onMounted, ref } from 'vue'
import { RecipesData } from '../database'
import Loader from '@/components/common/Loader.vue'
import axios from 'axios'
import { useRoute } from 'vue-router'

const route = useRoute()

const items = ref()

onMounted(async () => {
  if (!route.query.keywords) return
  const keyword = route.query.keywords[0]
  items.value = await axios
    .get(`http://127.0.0.1:8000/search/${keyword}`)
    .then((response) => {
      return JSON.parse(response.data)
    })
    .catch((err) => console.log(err))
})
</script>

<template>
  <SearchResultCarousel :items="items" v-if="items" />
  <Loader v-else />
</template>

<style lang="scss"></style>
