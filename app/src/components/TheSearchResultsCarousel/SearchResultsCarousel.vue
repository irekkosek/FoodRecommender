<script setup lang="ts">
import { ref, onMounted, watch, type Ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import type { BasicRecipe } from '@/types/Recipe'
import Button from 'primevue/button'
import ToggleButton from 'primevue/togglebutton'
import Sidebar from 'primevue/sidebar'
import Divider from 'primevue/divider'
import RadioButton from 'primevue/radiobutton'

const router = useRouter()
const route = useRoute()
const recipes = ref()
const isListEmpty = ref()
const isFilterSidebarVisible = ref(false)
const isSortSidebarVisible = ref(false)
const selectedKeywords: any = ref([])
const sorting: Ref<boolean> = ref(false)
const sortingOptions = ['rating', 'prep time', 'course', 'number of ingredients', 'none']
const selectedSorting = ref('none')

const tags = [
  { name: 'Prep Time', values: ['< 15 mins', '< 30 mins', '< 45 mins'] },
  { name: 'Course', values: ['breakfast', 'lunch', 'dinner', 'dessert'] },
  { name: 'Cuisine', values: ['american', 'asian', 'european'] }
]

const props = withDefaults(
  defineProps<{ items?: any[]; recipesToShow?: 'all' | 'favourite' | 'owned' }>(),
  {
    recipesToShow: 'all'
  }
)

watch(recipes, () => {
  if (props.recipesToShow === 'favourite') {
    recipes.value = recipes.value.filter(({ isFavourite }: BasicRecipe) => {
      if (typeof isFavourite !== undefined) return isFavourite === true
      else return false
    })
  } else if (props.recipesToShow === 'owned') {
    recipes.value = recipes.value.filter(({ isOwned }: BasicRecipe) => {
      if (typeof isOwned !== undefined) return isOwned === true
      else return false
    })
  }
  isListEmpty.value = recipes.value.length
})

onMounted(() => {
  recipes.value = props.items
})

const goToRecipe = (recipeId: number, isOwned: boolean) => {
  router.push({
    path: isOwned ? '/owned-recipe' : '/recipe',
    query: {
      ...route.query,
      id: recipeId,
      previousPage: router.currentRoute.value.path
    }
  })
}

const addKeyword = (keywordName: string) => {
  if (selectedKeywords.value.includes(keywordName))
    selectedKeywords.value.splice(selectedKeywords.value.indexOf(keywordName), 1)
  else selectedKeywords.value.push(keywordName)
}

const changeKeywordFocus = (e: any) => {
  e.target.classList.toggle('active')
}

watch(isFilterSidebarVisible, () => {
  // filtering request to api
})

watch(isSortSidebarVisible, () => {
  // sorting request to api
})

watch(sorting, () => {
  // ascending/descending sorting request to api
})
</script>
<template>
  <div>
    <div v-if="isListEmpty" class="search-results-carousel">
      <div class="filtering-sorting-section">
        <Button
          icon="pi pi-filter"
          aria-label="Open filters"
          @click="isFilterSidebarVisible = true"
          class="floating-button"
        />
        <Button
          :label="`Sort by...`"
          aria-label="Open sorting"
          @click="isSortSidebarVisible = true"
          class="floating-button"
        />
        <ToggleButton
          v-model="sorting"
          onIcon="pi pi-sort-alpha-down"
          offIcon="pi pi-sort-alpha-up"
          onLabel=""
          offLabel=""
          class="w-full sm:w-10rem"
          aria-label="Sorting"
        />
      </div>
      <div class="search-results-carousel__wrapper">
        <div
          class="recipe"
          v-for="{ id, imageURL, title, tags, cuisines, isOwned, isFavourite } in recipes"
          @click="goToRecipe(id, isOwned)"
        >
          <div v-if="isOwned" class="recipe__owned-marker"></div>
          <div
            :class="`recipe__favourite-marker pi ${isFavourite ? 'pi-heart-fill' : 'pi-heart'}`"
          />
          <div class="recipe__image" :style="`background-image: url(${imageURL});`">
            <div class="recipe__image__overlay">
              <span class="recipe__title">{{ title }}</span>
              <div class="recipe__tags">
                <div class="recipe__tags__tags">
                  <span v-for="tag in tags">#{{ tag }} </span>
                </div>
                <div class="recipe__tags__cuisines">
                  <span v-for="cuisine in cuisines">#{{ cuisine }} </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <Sidebar v-model:visible="isFilterSidebarVisible" position="bottom">
        <h2>Filter by</h2>

        <div class="keywords__section" v-for="{ name, values } in tags">
          <Divider />
          <h3>{{ name }}</h3>
          <div class="keywords__container">
            <span
              v-for="(name, index) in values"
              :key="index"
              :class="[
                `keywords__container__tag`,
                `${selectedKeywords.includes(name) ? 'active' : ''}`
              ]"
              @click="addKeyword(name), changeKeywordFocus($event)"
              >{{ name }}</span
            >
          </div>
        </div>
      </Sidebar>

      <Sidebar v-model:visible="isSortSidebarVisible" position="bottom">
        <h2>Sort by</h2>
        <Divider />
        <div class="sorting-options">
          <div class="sorting-options__item" v-for="option in sortingOptions">
            <RadioButton
              v-model="selectedSorting"
              :inputId="option"
              :name="option"
              :value="option"
            />
            <label :for="option" class="ml-2">{{ option }}</label>
          </div>
        </div>
      </Sidebar>
    </div>
    <div v-else>
      <p>Nothing here for now 😉</p>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.keywords__section {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.sorting-options {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  &__item {
    display: flex;
    gap: 1rem;
  }
}
.keywords__container {
  display: flex;
  flex-direction: row;
  gap: 10px;
  flex-wrap: wrap;

  &__tag {
    color: #ebb222;
    text-align: center;
    font-size: 0.8rem;
    border-radius: 27px;
    border: 1px solid #ebb222;
    padding: 5px 10px;

    transition: 0.2s cubic-bezier(0.215, 0.61, 0.355, 1);

    &:hover {
      color: white;
      background-color: #ebb222;
      cursor: pointer;
    }
  }
  .active {
    color: white !important;
    background-color: #ebb222 !important;
  }
}
.search-button {
  background: #ebb222;
  border: none;
}
.search-results-carousel {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.75rem;
  .filtering-sorting-section {
    display: flex;
    flex-direction: row;
    gap: 0.8rem;
    align-items: center;
  }
}
.search-results-carousel__wrapper {
  display: flex;
  flex-direction: column;
  gap: 1.75rem;

  .recipe {
    display: flex;
    position: relative;
    flex-direction: column;
    align-items: center;
    gap: 2rem;

    &:hover {
      cursor: pointer;
      box-shadow: 0px 5px 10px 2px rgba(119, 119, 119, 0.436);
    }

    border-radius: 22px;
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

    &__favourite-marker {
      position: absolute;
      bottom: 0;
      right: 0;
      width: 2rem;
      height: 2rem;
      color: white;
    }

    &__image {
      width: 14.55581rem;
      height: 10.271rem;
      border-radius: 22px;
      background: #d9d9d9;
      background-position: center;
      background-size: cover;
      background-repeat: no-repeat;

      &__overlay {
        background: rgba(13, 13, 13, 0.61);
        height: 100%;
        width: 75%;
        float: right;
        border-radius: inherit;
        border-top-left-radius: 0;
        border-bottom-left-radius: 0;

        padding: 2rem 1rem;
        display: flex;
        flex-direction: column;
        gap: 1rem;
      }
    }
    &__title {
      color: #fff;
      font-size: 1rem;
    }
    &__tags {
      display: flex;
      flex-direction: column;
      &__cuisines,
      &__tags {
        color: #fff;
        font-size: 0.8rem;
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        gap: 0.5rem;
      }
    }
  }
}
</style>
