<script setup lang="ts">
import loader from '@/assets/hot-food.json'
import { LottieAnimation } from 'lottie-web-vue'
</script>

<template>
  <div class="loader-wrapper">
    <lottie-animation ref="anim" :animationData="loader" :loop="true" :autoPlay="true" :speed="1" />
    <h2>Loading...</h2>
  </div>
</template>

<style lang="scss" scoped>
.loader-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  min-width: 100vw;
  background-color: rgba(255, 255, 255, 0.833);
  z-index: 1000;
  div {
    width: 200px;
    transform: translateY(-50px);
  }
}
</style>
