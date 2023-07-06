<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import RecipeForm from '@/components/TheRecipeForm/RecipeForm.vue'
import axios from 'axios'

const route = useRoute()
const recipe = ref()

onMounted(async () => {
  const recipeID = route.query.id as unknown as string
  recipe.value = await axios
    .get(`http://127.0.0.1:8000/recipes/${recipeID}`)
    .then((response) => {
      return response.data[0]
    })
    .catch((err) => console.log(err))
  console.log(recipe.value)
})
// get record from api
</script>

<template>
  <div>
    <RecipeForm v-if="recipe" :recipe="recipe" :pageTitle="`Edit \'${recipe.name}\' recipe`" />
  </div>
</template>
