import { defineStore } from 'pinia'

export const useUserLoginStore = defineStore('user-login', {
  state: () => {
    return { nick: '', id: -1 }
  },
  actions: {
    setUserNick(value: string) {
      this.nick = value
      localStorage.userNick = this.nick
    },
    getUserNick() {
      return localStorage.userNick
    },
    setUserId(value: number) {
      this.id = value
      localStorage.userId = this.id
    },
    getUserId() {
      return localStorage.userId
    }
  }
})
