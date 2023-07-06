<script setup lang="ts">
import { computed, ref, watch, type Ref } from 'vue'
import Dock from 'primevue/dock'
import Dialog from 'primevue/dialog'
import Button from 'primevue/button'
import { useRoute, useRouter } from 'vue-router'
import { useSaveRecipeStore } from '@/stores/saveRecipe'

const saveRecipeStore = useSaveRecipeStore()

const router = useRouter()
const route = useRoute()

const modalVisible = ref()
const modalText = ref()
const modalConfirmed = ref()

type label =
  | 'Go Back'
  | 'Home'
  | 'Search'
  | 'Add Recipe'
  | 'Save Added Recipe'
  | 'Save Edited Recipe'
  | 'Edit Recipe'
  | 'Delete Recipe'
  | 'Discard Changes'

type item = {
  label: label
  icon: string
  command: () => any
}

type menuConf = {
  path: string
  buttons: label[]
}

const menuConfigurations: menuConf[] = [
  {
    path: '/login',
    buttons: []
  },
  {
    path: '/',
    buttons: ['Add Recipe', 'Search']
  },
  {
    path: '/add-recipe',
    buttons: ['Go Back', 'Save Added Recipe']
  },
  {
    path: '/edit-recipe',
    buttons: ['Delete Recipe', 'Discard Changes', 'Save Edited Recipe']
  },
  {
    path: '/recipe',
    buttons: ['Go Back']
  },
  {
    path: '/owned-recipe',
    buttons: ['Go Back', 'Edit Recipe']
  },
  {
    path: '/search',
    buttons: ['Go Back']
  },
  {
    path: '/search-result',
    buttons: ['Go Back', 'Add Recipe', 'Search']
  },
  {
    path: '/my-recipes',
    buttons: ['Go Back', 'Add Recipe']
  },
  {
    path: '/liked-recipes',
    buttons: ['Go Back', 'Add Recipe']
  },
  {
    path: '/shopping-list',
    buttons: ['Go Back']
  }
]

const routeName = computed(() => router.currentRoute.value.fullPath)
const currentButtonsArray = ref()

watch(routeName, (newVal) => {
  currentButtonsArray.value = menuConfigurations.find(
    (conf) => conf.path === newVal.split('?')[0]
  )?.buttons
})

const items: Ref<item[]> = ref([
  {
    label: 'Go Back',
    icon: 'src/assets/arrow-back.svg',
    command: () => {
      const { previousPage, id, ...restParams } = route.query
      if (['/liked-recipes', '/my-recipes', '/search-result'].includes(previousPage as string))
        router.push({
          path: previousPage as string,
          query: {
            ...restParams
          }
        })
      else if (['/', '/add-recipe'].includes(previousPage as string))
        router.push({
          path: previousPage as string
        })
      else router.push('/')
    }
  },
  {
    label: 'Home',
    icon: 'src/assets/home.svg',
    command: () => {
      router.push('/')
    }
  },
  {
    label: 'Search',
    icon: 'src/assets/search.svg',
    command: () => {
      router.push('/search')
    }
  },
  {
    label: 'Add Recipe',
    icon: 'src/assets/add.svg',
    command: () => {
      const { previousPage, id, ...restParams } = route.query
      router.push({
        path: '/add-recipe',
        query: {
          ...restParams,
          previousPage: router.currentRoute.value.path
        }
      })
    }
  },
  {
    label: 'Save Added Recipe',
    icon: 'src/assets/bookmark-tick.svg',
    command: () => {
      saveRecipeStore.setIsFormSubmitted(true)
    }
  },
  {
    label: 'Save Edited Recipe',
    icon: 'src/assets/bookmark-tick.svg',
    command: () => {
      saveRecipeStore.setIsFormSubmitted(true)
    }
  },
  {
    label: 'Edit Recipe',
    icon: 'src/assets/edit.svg',
    command: () => {
      router.push({
        path: '/edit-recipe',
        query: {
          ...route.query,
          id: route.query.id
        }
      })
    }
  },
  {
    label: 'Delete Recipe',
    icon: 'src/assets/delete.svg',
    command: () => {
      // modalVisible.value = true
      // modalText.value = 'Are you sure you want to delete this recipe?'
      const { previousPage, id, ...restParams } = route.query
      router.push({
        path: previousPage as string,
        query: {
          ...restParams
        }
      })
    }
  },
  {
    label: 'Discard Changes',
    icon: 'src/assets/undo.svg',
    command: () => {
      // modalVisible.value = true
      // modalText.value = 'Are you sure you want to discard changes?'
      router.push({
        path: '/owned-recipe',
        query: {
          ...route.query
        }
      })
    }
  }
])

const onDockItemClick = (event: any, item: any) => {
  if (item.command) {
    item.command()
  }
  event.preventDefault()
}

const checkIfIncludes = (label: any) => {
  const arr = currentButtonsArray.value
  if (!arr) {
    const path = router.currentRoute.value.fullPath
    currentButtonsArray.value = menuConfigurations.find(
      (conf) => conf.path === path.split('?')[0]
    )?.buttons
  }
  return currentButtonsArray.value.includes(label)
}
</script>

<template>
  <div class="main-menu">
    <div class="main-menu__wrapper">
      <Dock :model="items">
        <template #item="slotProps">
          <div
            v-if="checkIfIncludes(slotProps.item.label)"
            @click="onDockItemClick($event, slotProps.item)"
          >
            <img :src="slotProps.item.icon" />
          </div>
        </template>
      </Dock>
    </div>
    <Dialog
      v-model:visible="modalVisible"
      modal
      :closable="false"
      header="Header"
      :style="{ width: '95vw' }"
    >
      <p>
        {{ modalText }}
      </p>
      <template #footer>
        <Button icon="pi pi-times" @click="modalVisible = false" />
        <Button icon="pi pi-check" @click=";[(modalVisible = false), (modalConfirmed = true)]" />
      </template>
    </Dialog>
  </div>
</template>

<style lang="scss">
.main-menu {
  all: initial !important;

  .p-dock {
    background-color: rgb(255, 206, 81);
    height: auto;
  }
  .p-dock-item {
    background-color: rgb(255, 206, 81);
    border-radius: 100% !important;
    border: 3px solid white;
    transition: 0.2s;
    padding: 10px !important;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    .p-menuitem-content,
    img {
      width: 30px;
      height: 30px;
    }
    &-current {
      transform: scale(1.4) !important;
      border: 3.5px solid white;
      &:hover {
        cursor: pointer;
        filter: brightness(110%);
      }
    }
    &-prev,
    &-next {
      transform: scale(1.1) !important;
    }
  }
  .p-dock-list {
    position: relative;
    bottom: 20px;
    gap: 30px;
    &-container {
      height: 60px;
    }
  }
  .p-dock.p-dock-top .p-dock-list-container,
  .p-dock.p-dock-bottom .p-dock-list-container {
    overflow: visible !important;
  }
  li:not(:has(.p-menuitem-content div)) {
    display: none;
  }
  li[aria-label='Edit Recipe'] {
    background-color: #097e2a !important;
  }
  li[aria-label='Delete Recipe'] {
    background-color: #c11818 !important;
  }
}
.p-dialog-footer button {
  width: 3rem !important;
}
</style>
