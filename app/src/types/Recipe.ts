export interface BasicRecipe {
  id: number
  name: string
  description: string
  tags: string[]
  thumbnail_url: string
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
  video_url?: string
}
