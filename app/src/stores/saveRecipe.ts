import { defineStore } from 'pinia'

export const useSaveRecipeStore = defineStore('save-recipe', {
  state: () => {
    return { isFormSubmitted: false }
  },
  actions: {
    setIsFormSubmitted(value: boolean) {
      this.isFormSubmitted = value
    }
  }
})
