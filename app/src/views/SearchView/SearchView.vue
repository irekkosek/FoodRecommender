<script setup lang="ts">
import { ref } from 'vue'
import Chips from 'primevue/chips'
import Button from 'primevue/button'
import router from '@/router'

const selectedKeywords = ref(['pizza'])
const recommendedKeywords = ref(['asian', 'ramen', 'noodles', 'eggs', 'vegetarian'])

const addKeyword = (keywordName: string) => {
  if (selectedKeywords.value.includes(keywordName))
    selectedKeywords.value.splice(selectedKeywords.value.indexOf(keywordName), 1)
  else selectedKeywords.value.push(keywordName)
}

const goToSearchResult = () => {
  if (selectedKeywords.value.length <= 0) return
  router.push({
    path: '/search-result',
    query: {
      keywords: selectedKeywords.value
    }
  })
}

const changeKeywordFocus = (e: any) => {
  e.target.classList.toggle('active')
}
</script>

<template>
  <div>
    <h2>What dou you want to find?</h2>
    <div class="form__container">
      <Chips id="chips" v-model="selectedKeywords" separator=" " :allowDuplicate="false" />
    </div>
    <div class="recommended-keywords__container">
      <span
        v-for="(name, index) in recommendedKeywords"
        :key="index"
        class="recommended-keywords__container__tag"
        @click="addKeyword(name), changeKeywordFocus($event)"
        >{{ name }}</span
      >
    </div>
    <Button
      icon="pi pi-search"
      rounded
      aria-label="Search"
      class="search-button"
      @click="goToSearchResult"
    />
  </div>
</template>

<style lang="scss" scoped>
.recommended-keywords__container {
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
</style>
