<script setup lang="ts">
import InputText from 'primevue/inputtext'
import InputNumber from 'primevue/inputnumber'
import Chips from 'primevue/chips'
import Button from 'primevue/button'
import Divider from 'primevue/divider'
import { onMounted, ref, watch, type Ref } from 'vue'
import { RecipesData } from '@/views/database'
import { useRoute, useRouter } from 'vue-router'
import { useSaveRecipeStore } from '@/stores/saveRecipe'
import axios from 'axios'
import { useUserLoginStore } from '@/stores/userLogin'
import { data } from './data'

const router = useRouter()
const saveRecipeStore = useSaveRecipeStore()
const userLogin = useUserLoginStore()
const isFormValid = ref(false)

watch(isFormValid, (newVal) => {
  if (newVal) {
    // push new object to database
    const tempID = 100
    axios
      .post('http://127.0.0.1:8000/createRecipe', data, {
        headers: {
          'Access-Control-Allow-Origin': '*'
        }
      })
      .then((response) => {
        console.log(response)
      })
      .catch((error) => {
        console.log(error.response.data)
      })
    router.push({
      path: '/owned-recipe',
      query: {
        ...route.query,
        id: route.query.id ? route.query.id : tempID
      }
    })
  }
})

watch(
  () => saveRecipeStore.isFormSubmitted,
  (newVal) => {
    if (newVal) {
      if (
        !name.value ||
        !(ingredients.value.length > 0) ||
        !(tags.value.length > 0) ||
        !(stepsValues.value.length > 0) ||
        !enteredImageURL.value
      )
        isFormValid.value = false
      else isFormValid.value = true
      saveRecipeStore.setIsFormSubmitted(false)
    }
  }
)

const name = ref('Name')
const ingredients = ref(['milk'])
const tags = ref(['asian', 'easy'])
const stepsValues = ref(['Add more steps!'])
const enteredStep = ref('')
// const enteredPrepTime = ref(30)
const enteredImageURL = ref('temp')

// const formFields = ref([
//   {name: 'name', value: null},
//   {name: 'ingredients', value: ['milk']},
//   {name: 'tags', value: ['asian', 'easy']},
//   {name: 'stepsValues', value: ['Add more steps!']},
//   {name: 'enteredStep', value: ''},
//   {name: 'enteredPrepTime', value: 0}
// ])

const props = withDefaults(defineProps<{ recipe?: any; pageTitle: string }>(), {
  pageTitle: 'Title'
})

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
  // recipe.value = RecipesData.getProductsData().find(
  //   ({ id }) => id == (route.query.id as unknown as number)
  // )
  const r = props.recipe
  name.value = r.name
  ingredients.value = r.ingredients
  stepsValues.value = r.steps
  tags.value = (Object.keys(r) as (keyof typeof r)[]).filter((key) => {
    return r[key] === 1
  })

  tags.value = tags.value.map((el: any) => {
    return el.split('_').slice(1).join(' ')
  })
  enteredImageURL.value = r.thumbnail_url
})
</script>

<template>
  <div>
    <h2>{{ props.pageTitle }}</h2>
    <Divider />
    <div class="form__container">
      <span class="p-float-label">
        <InputText id="username" v-model="name" :class="name ?? `p-invalid`" />
        <label for="username">Recipe name</label>
      </span>
      <span class="p-float-label">
        <Chips id="chips" v-model="ingredients" separator=" " :class="ingredients ?? `p-invalid`" />
        <label for="chips">Ingredients</label>
      </span>
      <span class="p-float-label">
        <InputText
          input-id="image-url"
          v-model="enteredImageURL"
          :class="enteredImageURL ?? `p-invalid`"
        />
        <label for="image-url">Image URL</label>
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
      <!-- <div class="additional-info">
        <label for="prep-time">Prep Time</label>
        <InputNumber
          input-id="prep-time"
          v-model="enteredPrepTime"
          :min="0"
          :max="600"
          suffix=" mins"
          :class="enteredPrepTime ?? `p-invalid`"
        />
      </div> -->
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
