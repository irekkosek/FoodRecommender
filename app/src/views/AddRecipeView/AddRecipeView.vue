<script setup lang="ts">
import RecipeForm from '@/components/TheRecipeForm/RecipeForm.vue'
import { ref, watch } from 'vue'

const isSaveRecipeButtonClicked = ref()

watch(isSaveRecipeButtonClicked, () => {
  console.log('Create new record in database')
})
</script>

<template>
  <div>
    <RecipeForm
      @save-recipe-button-clicked="isSaveRecipeButtonClicked = true"
      pageTitle="Add new recipe"
    />
  </div>
</template>

<style lang="scss" scoped></style>
