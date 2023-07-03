<script setup lang="ts">
import InputText from 'primevue/inputtext'
import InputNumber from 'primevue/inputnumber'
import Chips from 'primevue/chips'
import Button from 'primevue/button'
import { onMounted, ref, watch } from 'vue'
import { RecipesData } from '@/views/database'
import { useRoute } from 'vue-router'
import { useSaveRecipeStore } from '@/stores/saveRecipe'
import router from '@/router'

const saveRecipeStore = useSaveRecipeStore()
const isFormValid = ref(false)

watch(isFormValid, (newVal) => {
  if (newVal) {
    // push new object to database
    router.push({
      path: '/owned-recipe',
      query: {
        id: route.query.id ? route.query.id : Math.floor(Math.random() * 100)
      }
    })
  }
})

watch(
  () => saveRecipeStore.isFormSubmitted,
  (newVal) => {
    if (newVal) {
      if (
        !title.value ||
        !(ingredients.value.length > 0) ||
        !(tags.value.length > 0) ||
        !(stepsValues.value.length > 0) ||
        !enteredPrepTime.value
      )
        isFormValid.value = false
      else isFormValid.value = true
      saveRecipeStore.setIsFormSubmitted(false)
    }
  }
)

const title = ref(null)
const ingredients = ref(['milk'])
const tags = ref(['asian', 'easy'])
const stepsValues = ref(['Add more steps!'])
const enteredStep = ref('')
const enteredPrepTime = ref()

// const formFields = ref([
//   {name: 'title', value: null},
//   {name: 'ingredients', value: ['milk']},
//   {name: 'tags', value: ['asian', 'easy']},
//   {name: 'stepsValues', value: ['Add more steps!']},
//   {name: 'enteredStep', value: ''},
//   {name: 'enteredPrepTime', value: 0}
// ])

const props = withDefaults(defineProps<{ pageTitle: string }>(), { pageTitle: 'Title' })

const addStep = () => {
  stepsValues.value.push(enteredStep.value)
  enteredStep.value = ''
}

const removeStep = (stepID: number) => {
  stepsValues.value.splice(stepID, 1)
}

const route = useRoute()
const recipe = ref()

onMounted(() => {
  if (!route.query.id) return
  recipe.value = RecipesData.getProductsData().find(
    ({ id }) => id == (route.query.id as unknown as number)
  )
  const r = recipe.value
  title.value = r.title
  ingredients.value = r.ingredients
  stepsValues.value = r.steps
  tags.value = r.tags
})
</script>

<template>
  <div>
    <h2>{{ props.pageTitle }}</h2>
    <div class="form__container">
      <span class="p-float-label">
        <InputText id="username" v-model="title" :class="title ?? `p-invalid`" />
        <label for="username">Recipe title</label>
      </span>
      <span class="p-float-label">
        <Chips id="chips" v-model="ingredients" separator=" " :class="ingredients ?? `p-invalid`" />
        <label for="chips">Ingredients</label>
      </span>
      <div class="steps__container">
        <label>Steps</label>
        <span
          v-for="(step, index) in stepsValues"
          :key="index"
          class="step"
          :class="stepsValues ?? `p-invalid`"
        >
          <Button
            icon="pi pi-minus"
            outlined
            rounded
            aria-label="Remove"
            @click="removeStep(index)"
          />
          <span>{{ `${index + 1}. ${step}` }}</span>
        </span>
        <InputText v-model="enteredStep" placeholder="Write here next step" />
        <Button
          icon="pi pi-plus"
          rounded
          aria-label="Add"
          :disabled="enteredStep.length <= 0 ? true : false"
          @click="addStep()"
        />
      </div>
      <div class="additional-info">
        <label for="prep-time">Prep Time</label>
        <InputNumber
          input-id="prep-time"
          v-model="enteredPrepTime"
          :min="0"
          :max="600"
          suffix=" mins"
          :class="enteredPrepTime ?? `p-invalid`"
        />
      </div>
      <span class="p-float-label">
        <Chips id="chips" v-model="tags" separator=" " :class="tags ?? `p-invalid`" />
        <label for="chips">Tags</label>
      </span>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.step {
  display: flex;
  gap: 1rem;
}
</style>
