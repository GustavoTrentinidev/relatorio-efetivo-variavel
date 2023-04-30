import Vue from "vue"
import Vuex from "vuex"
import VuexPersistence from "vuex-persist"
Vue.use(Vuex)


const vuexLocal = new VuexPersistence({
    storage: window.localStorage,
    key: 'relatorioev-vue-django',
})

import { auth } from "./auth"
import { aplicador } from "./aplicador"


const modules = {
    auth,
    aplicador
}

export default new Vuex.Store({
    modules,
    plugins: [vuexLocal.plugin]
})