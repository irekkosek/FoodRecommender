<script setup lang="ts">
import InputText from 'primevue/inputtext'
import Password from 'primevue/password'
import Button from 'primevue/button'
import { onMounted, ref } from 'vue'
import router from '../../router'
import { useUserLoginStore } from '@/stores/userLogin'

const mockedUser = { nick: 'cukinia', password: 'helloworld' }

const nick = ref()
const password = ref()

onMounted(() => {
  useUserLoginStore().setUserNick('')
})

const updateUserID = () => {
  // check if nick and password are in database, then
  if (!(nick.value === mockedUser.nick && password.value === mockedUser.password)) return
  useUserLoginStore().setUserNick(nick.value)
  router.push('/')
}
</script>

<template>
  <div>
    <h2>Welcome to FoodieFinder</h2>
    <span class="p-float-label">
      <InputText id="username" v-model="nick" :class="nick ?? `p-invalid`" />
      <label for="username">Username</label>
    </span>
    <span class="p-float-label">
      <Password
        id="password"
        v-model="password"
        :class="password ?? `p-invalid`"
        toggleMask
        :feedback="false"
      />
      <label for="password">Password</label>
    </span>
    <Button
      class="go-button"
      icon="pi pi-arrow-right"
      rounded
      aria-label="Arrow right"
      @click="updateUserID"
    />
  </div>
</template>

<style scoped lang="scss">
.go-button {
  background: #ebb222;
  border: none;
}

.p-inputtext {
  width: 15rem !important;
}
</style>
