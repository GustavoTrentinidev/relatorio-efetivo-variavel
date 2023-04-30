import { api } from "@/plugins/axios"
import router from "@/router"

export const auth = {
    namespaced: true,
    state: () => ({
        loggedIn: false,
        userAccess: {},
    }),
    mutations: {
        setLoginInfo(state, user){
            state.userAccess = user
            state.loggedIn = true
        }, 
        setLogout(state){
            state.userAccess = {}
            state.loggedIn = false
        }
    },
    actions: {
        async loginStore({commit}, user){
            return new Promise((resolve, reject)=>{
                api.post('/token/', user).then((data)=>{
                    commit('setLoginInfo', data)
                    router.push('/')
                    resolve()
                }).catch((err)=>{
                    reject(err)
                })
            })
        }
    }
}