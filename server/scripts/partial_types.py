from prisma.models import RECIPES
# RECIPES.create_partial('RECIPESWithoutId', optional={'id','USER_likes_RECIPES'})
RECIPES.create_partial('RECIPESWithoutId', exclude={'id','USER_likes_RECIPES','USER_owns_RECIPES'}) # works
# RECIPES.create_partial('RECIPESWithoutId', optional={'id','USER_likes_RECIPES'}) 
