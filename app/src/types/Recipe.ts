export interface BasicRecipe {
  id: number
  title: string
  description: string
  tags: string[]
  imageURL: string
  isFavourite: any
  isOwned: boolean
}

export interface ExtendedRecipe extends BasicRecipe {
  diets?: string[]
  courses?: string[]
  cuisines?: string[]
  prepTime?: string
  cookTime?: string
  ingredients: string[]
  steps: string[]
  sourceURL?: string
}
