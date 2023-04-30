import { api } from "@/plugins/axios"


export const aplicador = {
    namespaced: true,
    state: {
        aplicador_dados: {}
    },
    mutations: {
        setDadosAplicador(state, dados){
            state.aplicador_dados = dados
        }
    },
    actions: {
        async getUserDetail({commit}){
            const { data } = await api.get('user-detail')
            const [aplicadordata] = data
            commit('setDadosAplicador', aplicadordata)
        }
    }
}