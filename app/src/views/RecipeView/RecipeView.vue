<script setup lang="ts">
import { useRoute } from 'vue-router'
import { RecipesData } from '../database'
import { onMounted, ref, watch } from 'vue'
import Checkbox from 'primevue/checkbox'
import Button from 'primevue/button'
import ToggleButton from 'primevue/togglebutton'

const route = useRoute()
const recipe = ref()
const checkedIngredients = ref()
const isLiked = ref(false)

watch(checkedIngredients, (newVal) => {
  localStorage.ingredients = newVal
})

onMounted(() => {
  checkedIngredients.value = localStorage.ingredients
    .split(',')
    .filter((ingredient: string) => ingredient !== '')
  recipe.value = RecipesData.getProductsData().find(
    ({ id }) => id == (route.query.id as unknown as number)
  )
  if (!recipe.value.isFavourite) return
  isLiked.value = recipe.value.isFavourite
})

const goToSource = (url: string) => {
  window.location.href = url
}
</script>

<template>
  <div>
    <div class="recipe" v-if="recipe">
      <div v-if="recipe.isOwned" class="recipe__owned-marker"></div>

      <div class="recipe__image" :style="`background-image: url(${recipe.imageURL});`">
        <div class="recipe__image__overlay">
          <span class="recipe__title">{{ recipe.title }}</span>
          <div class="recipe__tags">
            <div class="recipe__tags__tags">
              <span v-for="tag in recipe.tags">#{{ tag }} </span>
            </div>
            <div class="recipe__tags__cuisines">
              <span v-for="cuisine in recipe.cuisines">#{{ cuisine }} </span>
            </div>
          </div>
        </div>
      </div>
      <ToggleButton
        v-model="isLiked"
        class="like-button"
        onLabel=""
        offLabel=""
        onIcon="pi pi-heart-fill"
        offIcon="pi pi-heart"
      />
      <div class="recipe__info">
        <div class="recipe__ingredients-section">
          <span class="recipe__ingredients-section__title">Ingredients</span>
          <div class="recipe__ingredients-section__list">
            <div v-for="(value, index) in recipe.ingredients" :key="index">
              <Checkbox
                v-model="checkedIngredients"
                :inputId="`ingredient-${index}`"
                :name="value"
                :value="value"
              />
              <label :for="`ingredient-${index}`"> {{ value }} </label>
            </div>
          </div>
        </div>
        <div class="recipe__steps-section">
          <span class="recipe__steps-section__title">Steps</span>
          <span v-for="(step, index) in recipe.steps">{{ `${index + 1}. ${step}` }}</span>
        </div>
        <Button
          @click="goToSource(recipe.sourceURL)"
          icon="pi pi-arrow-right"
          iconPos="right"
          label="Go to source"
          rounded
          aria-label="Go to source"
          class="search-button"
        />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.recipe {
  transform: translateY(-5rem);

  .like-button {
    position: absolute;
    top: 13rem;
    right: 4rem;
    z-index: 3;
    border-radius: 100%;
  }

  &__info {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    border-radius: 3rem 3rem 0 0;
    transform: translateY(-2rem);
    z-index: 2;
    background-color: white;
  }

  &__owned-marker {
    position: absolute;
    overflow: hidden;
    top: 0;
    right: 0;
    width: 0;
    height: 0;
    border-style: solid;
    border-width: 0 4rem 4rem 0;
    border-color: transparent #097e2a transparent transparent;
  }

  &__image {
    min-width: 100vw;
    height: 16.125rem;
    // border-radius: 0 0 40px 40px;
    background: #d9d9d9;
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;

    &__overlay {
      background: rgba(0, 0, 0, 0.36);
      height: 100%;
      width: 100%;
      float: right;
      border-radius: inherit;

      padding: 4rem 2rem;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      gap: 1rem;
    }
  }
  &__title {
    color: #fff;
    font-size: 1.25rem;
  }
  &__tags {
    display: flex;
    flex-direction: column;
    &__cuisines,
    &__tags {
      color: #fff;
      font-size: 1rem;
      display: flex;
      flex-direction: row;
      flex-wrap: wrap;
      gap: 0.5rem;
    }
  }
  &__steps-section,
  &__ingredients-section {
    &__title {
      font-size: 1.5rem;
      margin-bottom: 1.5rem;
    }
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    width: 100vw;
    padding: 3rem 3rem;
  }
  &__ingredients-section {
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
}
</style>
