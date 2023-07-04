<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { RecipesData } from '../database'
import RecipeForm from '@/components/TheRecipeForm/RecipeForm.vue'

const route = useRoute()
const recipe = ref()

onMounted(() => {
  recipe.value = RecipesData.getProductsData().find(
    ({ id }) => id == (route.query.id as unknown as number)
  )
})
// get record from api
</script>

<template>
  <div>
    <RecipeForm v-if="recipe" :pageTitle="`Edit ${recipe.title} recipe`" />
  </div>
</template>
