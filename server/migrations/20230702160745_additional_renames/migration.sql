/*
  Warnings:

  - You are about to drop the `USER_likes_RECPIES` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "USER_likes_RECPIES" DROP CONSTRAINT "USER_likes_RECPIES_RECIPE_id_fkey";

-- DropForeignKey
ALTER TABLE "USER_likes_RECPIES" DROP CONSTRAINT "USER_likes_RECPIES_USER_id_fkey";

-- DropTable
DROP TABLE "USER_likes_RECPIES";

-- CreateTable
CREATE TABLE "USER_likes_RECIPES" (
    "USER_id" INTEGER NOT NULL,
    "RECIPE_id" INTEGER NOT NULL,

    CONSTRAINT "USER_likes_RECIPES_pkey" PRIMARY KEY ("USER_id","RECIPE_id")
);

-- AddForeignKey
ALTER TABLE "USER_likes_RECIPES" ADD CONSTRAINT "USER_likes_RECIPES_USER_id_fkey" FOREIGN KEY ("USER_id") REFERENCES "USERS"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "USER_likes_RECIPES" ADD CONSTRAINT "USER_likes_RECIPES_RECIPE_id_fkey" FOREIGN KEY ("RECIPE_id") REFERENCES "RECIPES"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
