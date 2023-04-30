import Vue from "vue"
import Vuex from "vuex"
import VuexPersistence from "vuex-persist"
Vue.use(Vuex)


const vuexLocal = new VuexPersistence({
    storage: window.localStorage,
    key: 'relatorioev-vue-django',
})

import { auth } from "./auth"


const modules = {
    auth,
}

export default new Vuex.Store({
    modules,
    plugins: [vuexLocal.plugin]
})