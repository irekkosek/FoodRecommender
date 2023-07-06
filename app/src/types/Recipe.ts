export interface BasicRecipe {
  id: number
  name: string
  description: string
  tags: string[]
  thumbnail_url: string
  USER_likes_RECIPES: any
  USER_owns_RECIPES: boolean
}

export interface ExtendedRecipe extends BasicRecipe {
  diets?: string[]
  courses?: string[]
  cuisines?: string[]
  prepTime?: string
  cookTime?: string
  ingredients: string[]
  steps: string[]
  video_url?: string
}
