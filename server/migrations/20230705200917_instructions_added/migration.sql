-- CreateTable
CREATE TABLE "INSTRUCTIONS" (
    "id" SERIAL NOT NULL,
    "step" TEXT NOT NULL,
    "step_number" INTEGER NOT NULL,
    "recipe_id" TEXT NOT NULL,

    CONSTRAINT "INSTRUCTIONS_pkey" PRIMARY KEY ("id")
);
