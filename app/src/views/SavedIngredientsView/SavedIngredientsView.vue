<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import Checkbox from 'primevue/checkbox'
import Divider from 'primevue/divider'
import { useSetSavedIngredientsStore } from '@/stores/setSavedIngredients'

const setSavedIngredients = useSetSavedIngredientsStore()

const checkedIngredients = ref()
const isListEmpty = ref()

watch(checkedIngredients, (newVal) => {
  setSavedIngredients.setIngredients(newVal)
})

onMounted(() => {
  const ing = setSavedIngredients.getIngredients()
  checkedIngredients.value = ing
    ? ing.split(',').filter((ingredient: string) => ingredient !== '')
    : []
  isListEmpty.value = checkedIngredients.value.length > 0
})
</script>

<template>
  <div>
    <h2>Shopping list</h2>
    <Divider />
    <div v-if="isListEmpty" class="ingredients-section__list">
      <div v-for="(value, index) in checkedIngredients" :key="index">
        <Checkbox
          v-model="checkedIngredients"
          :inputId="`ingredient-${index}`"
          :name="value"
          :value="value"
        />
        <label :for="`ingredient-${index}`"> {{ value }} </label>
      </div>
    </div>
    <div v-else>
      <p>Nothing here for now 😉</p>
    </div>
  </div>
</template>

<style lang="scss">
.ingredients-section {
  &__title {
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
  }
  display: flex;
  gap: 0.5rem;
  width: 100vw;
  padding: 3rem 3rem;
}
.ingredients-section {
  background-color: rgba(131, 131, 131, 0.07);
  border-radius: 0 0 3rem 3rem;
  &__list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    & > div {
      display: flex;
      gap: 0.5rem;
    }
  }
}
</style>
