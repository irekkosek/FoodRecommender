import type { ExtendedRecipe } from '@/types/Recipe'

export const RecipesData = {
  getProductsMini() {
    return Promise.resolve(this.getProductsData().slice(0, 5))
  },
  getProductsSmall() {
    return Promise.resolve(this.getProductsData().slice(0, 10))
  },
  getProducts() {
    return Promise.resolve(this.getProductsData())
  },
  getProductsData(): ExtendedRecipe[] {
    return [
      {
        id: 1,
        name: 'Mac and cheese',
        description: 'Awesome dinner.',
        video_url: 'https://www.google.pl/',
        thumbnail_url:
          'https://upload.wikimedia.org/wikipedia/commons/4/44/Original_Mac_n_Cheese_.jpg',
        tags: ['lunch', 'dinner'],
        ingredients: ['milk', 'eggs', 'cheese', 'water'],
        steps: ['Mix all dry ingredients', 'Combine with wet ingredients', 'Bake', 'Enjoy!'],
        USER_likes_RECIPES: false,
        USER_owns_RECIPES: false
      },
      {
        id: 2,
        name: 'Fish salad',
        description: 'Eat everyday!',
        video_url: 'https://www.google.pl/',
        thumbnail_url:
          'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8Mnx8fGVufDB8fHx8&w=1000&q=80',
        tags: ['lunch', 'breakfast'],
        ingredients: ['milk', 'eggs', 'cheese', 'water'],
        steps: ['Mix all dry ingredients', 'Combine with wet ingredients', 'Bake', 'Enjoy!'],
        USER_likes_RECIPES: false,
        USER_owns_RECIPES: true
      },
      {
        id: 3,
        name: 'Pancakes',
        description: 'Sweet as fuck :D',
        video_url: 'https://www.google.pl/',
        thumbnail_url:
          'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=480&q=80',
        tags: ['breakfast', 'dinner'],
        cuisines: ['american'],
        ingredients: ['milk', 'eggs', 'cheese', 'water'],
        steps: ['Mix all dry ingredients', 'Combine with wet ingredients', 'Bake', 'Enjoy!'],
        USER_likes_RECIPES: true,
        USER_owns_RECIPES: true
      },
      {
        id: 4,
        name: 'Pizza',
        description: 'Mamma mia Italiano',
        video_url: 'https://www.google.pl/',
        thumbnail_url:
          'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=481&q=80',
        tags: ['lunch', 'dinner'],
        cuisines: ['italian'],
        ingredients: ['milk', 'eggs', 'cheese', 'water'],
        steps: ['Mix all dry ingredients', 'Combine with wet ingredients', 'Bake', 'Enjoy!'],
        USER_likes_RECIPES: true,
        USER_owns_RECIPES: false
      },
      {
        id: 5,
        name: 'Something green',
        description: 'Maybe good',
        video_url: 'https://www.google.pl/',
        thumbnail_url:
          'https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80',
        tags: ['lunch', 'snack'],
        ingredients: ['milk', 'eggs', 'cheese', 'water'],
        steps: ['Mix all dry ingredients', 'Combine with wet ingredients', 'Bake', 'Enjoy!'],
        USER_likes_RECIPES: false,
        USER_owns_RECIPES: false
      },
      {
        id: 6,
        name: 'Mac and cheese',
        description: 'Awesome dinner.',
        video_url: 'https://www.google.pl/',
        thumbnail_url:
          'https://upload.wikimedia.org/wikipedia/commons/4/44/Original_Mac_n_Cheese_.jpg',
        tags: ['lunch', 'dinner'],
        cuisines: ['american'],
        ingredients: ['milk', 'eggs', 'cheese', 'water'],
        steps: ['Mix all dry ingredients', 'Combine with wet ingredients', 'Bake', 'Enjoy!'],
        USER_likes_RECIPES: false,
        USER_owns_RECIPES: false
      }
    ]
  }
}
