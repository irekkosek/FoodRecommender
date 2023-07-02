<script setup lang="ts"></script>
<template>
  <div class="wrapper">
    <div class="main__wrapper">
      <router-view v-slot="{ Component }">
        <transition name="fade">
          <component :is="Component" />
        </transition>
      </router-view>
    </div>
  </div>
</template>

<style lang="scss">
.wrapper {
  margin: 0 0 40px 0;
  background-color: rgb(255, 255, 255);
  border-top: 1px solid #e6e4d9;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 25px 0;
  overflow-x: hidden;
}
</style>
