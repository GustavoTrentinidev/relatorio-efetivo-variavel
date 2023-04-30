import { api, tokenChange, cleanToken } from "@/plugins/axios"
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
            cleanToken()
        }
    },
    actions: {
        async loginStore({commit, dispatch}, user){
            return new Promise((resolve, reject)=>{
                api.post('/token/', user).then(({ data })=>{
                    commit('setLoginInfo', data)
                    tokenChange(data.access)
                    router.push('/')
                    dispatch('aplicador/getUserDetail', {}, {root: true})
                    resolve()
                }).catch((err)=>{
                    reject(err)
                })
            })
        }
    }
}