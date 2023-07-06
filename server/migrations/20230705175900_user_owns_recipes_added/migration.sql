-- CreateTable
CREATE TABLE "USER_owns_RECIPES" (
    "USER_id" INTEGER NOT NULL,
    "RECIPE_id" INTEGER NOT NULL,

    CONSTRAINT "USER_owns_RECIPES_pkey" PRIMARY KEY ("USER_id","RECIPE_id")
);

-- AddForeignKey
ALTER TABLE "USER_owns_RECIPES" ADD CONSTRAINT "USER_owns_RECIPES_USER_id_fkey" FOREIGN KEY ("USER_id") REFERENCES "USERS"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "USER_owns_RECIPES" ADD CONSTRAINT "USER_owns_RECIPES_RECIPE_id_fkey" FOREIGN KEY ("RECIPE_id") REFERENCES "RECIPES"("id") ON DELETE RESTRICT ON UPDATE CASCADE;