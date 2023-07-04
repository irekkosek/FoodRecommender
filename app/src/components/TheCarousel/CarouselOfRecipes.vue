<script setup lang="ts">
import { ref, onMounted } from 'vue'
import router from '@/router'

const recipes = ref()

const props = defineProps<{ items?: any[] }>()

onMounted(() => {
  recipes.value = props.items
})

const goToRecipe = (recipeId: number, isOwned: boolean) => {
  router.push({
    path: isOwned ? '/owned-recipe' : '/recipe',
    query: {
      id: recipeId,
      previousPage: router.currentRoute.value.fullPath
    }
  })
}
</script>
<template>
  <div class="carousel__wrapper">
    <div
      class="recipe"
      v-for="{ id, imageURL, title, description, isOwned } in recipes"
      @click="goToRecipe(id, isOwned)"
    >
      <div v-if="isOwned" class="recipe__owned-marker"></div>
      <div class="recipe__image" :style="`background-image: url(${imageURL});`" />
      <div class="recipe__text">
        <span class="recipe__title">{{ title }}</span>
        <span class="recipe__desc">{{ description }}</span>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.carousel__wrapper {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}
.recipe {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
  position: relative;

  &:hover {
    cursor: pointer;
    box-shadow: 0px 20px 27px 2px rgba(119, 119, 119, 0.3);
  }

  padding: 2rem;
  width: 18.90363rem;
  border-radius: 22px;
  background: #fff;
  box-shadow: 0px 10px 10px 2px rgba(119, 119, 119, 0.2);
  transition: 0.5s;

  &__owned-marker {
    position: absolute;
    overflow: hidden;
    top: 0;
    right: 0;
    width: 0;
    height: 0;
    border-style: solid;
    border-width: 0 3rem 3rem 0;
    border-color: transparent #097e2a transparent transparent;
    border-top-right-radius: 22px;
  }
  &__image {
    width: 14.55581rem;
    height: 10.271rem;
    border-radius: 22px;
    background: #d9d9d9;
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
  }
  &__text {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
  }
  &__title {
    color: #000;
    text-align: center;
    font-size: 1.25rem;
  }
}
</style>
