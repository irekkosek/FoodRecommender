<script setup lang="ts">
import { app } from '@/main'
import router from '@/router'
import { computed, onMounted, ref, watch } from 'vue'
import { RouterView } from 'vue-router'
import MainMenu from './components/TheMainMenu/MainMenu.vue'
import Button from 'primevue/button'
import Menu from 'primevue/menu'

const showFooter = ref()
const showContent = ref()
const isSaveRecipeButtonClicked = ref()

const routeName = computed(() => router.currentRoute.value.fullPath)

const menu = ref()
const items = ref([
  {
    items: [
      {
        label: 'My Recipes',
        icon: 'pi pi-bookmark',
        command: () => {
          router.push('/my-recipes')
        }
      },
      {
        label: 'Favourites',
        icon: 'pi pi-heart',
        command: () => {
          router.push('/liked-recipes')
        }
      },
      {
        label: 'Shopping List',
        icon: 'pi pi-shopping-cart',
        command: () => {
          router.push('/shopping-list')
        }
      }
    ]
  }
])

const toggle = (event: any) => {
  menu.value.toggle(event)
}

watch(routeName, () => {
  getPath()
})

watch(isSaveRecipeButtonClicked, () => {
  console.log('hello')
})

onMounted(() => {
  getPath()
})

const goBack = () => {
  router.push('/login')
}

const getPath = () => {
  showFooter.value = routeName.value !== '/login'
  showContent.value = localStorage.userID !== -1 || routeName.value === '/login'
}
</script>

<template>
  <div class="menu">
    <Button
      type="button"
      class="pi pi-bars"
      @click="toggle"
      aria-haspopup="true"
      aria-controls="overlay_menu"
    />
    <Menu ref="menu" id="overlay_menu" :model="items" :popup="true" />
  </div>
  <div class="main">
    <RouterView v-if="showContent" />

    <div class="error" v-else>
      <h2>You are not logged in!</h2>
      <h3>Go back!</h3>
      <Button
        icon="pi pi-arrow-left"
        rounded
        aria-label="Go back"
        class="go-back-button"
        @click="goBack()"
      />
    </div>
  </div>
  <div class="footer" v-if="showFooter && showContent">
    <MainMenu @save-recipe-button-clicked="isSaveRecipeButtonClicked = true" />
  </div>
</template>

<style lang="scss" scoped>
.go-back-button {
  background: #ebb222;
  border: none;
}
.error {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  height: 100vh;
}
</style>
