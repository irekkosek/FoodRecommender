import { defineStore } from 'pinia'

export const useUserLoginStore = defineStore('user-login', {
  state: () => {
    return { nick: '' }
  },
  actions: {
    setUserNick(value: string) {
      this.nick = value
      localStorage.userNick = this.nick
    },
    getUserNick() {
      return localStorage.userNick
    }
  }
})
