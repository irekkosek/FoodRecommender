import { defineStore } from 'pinia'

export const useSetSavedIngredientsStore = defineStore('set-saved-ingredients', {
  state: () => {
    return { ingredients: '' }
  },
  actions: {
    setIngredients(value: string) {
      this.ingredients = value
      localStorage.ingredients = this.ingredients
    },
    getIngredients() {
      return localStorage.ingredients
    }
  }
})
