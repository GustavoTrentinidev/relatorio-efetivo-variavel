<template>
  <div>
    <div class="main">
      <InputPesquisa @mudarValorBusca="getComNovoValor"/>
      <EvResultado :efetivos="evs" @botaoClicado="abrirModalAction"/>
    </div>
    <PopUpEv :modalAberto="modalAberto" @fecharModal="fecharModalAction" :evFichaID="idFichaEvSelecionado"/>
    <div class="logout">
      <div>sgtivan</div>
      <div @click="setLogout">Logout</div>
    </div>
  </div>
</template>

<script>
import { api } from "@/plugins/axios"
import InputPesquisa from '../components/InputPesquisa.vue'
import EvResultado from '../components/EvResultado.vue'
import PopUpEv from '../components/PopUpEv.vue'
import { mapMutations } from 'vuex'


export default {
    components: {InputPesquisa, EvResultado, PopUpEv},
    data(){
      return {
        evs: [],
        modalAberto: false,
        idFichaEvSelecionado: 0
      }
    },
    mounted(){
      this.getEv()
    },
    methods: {
      ...mapMutations('auth', ['setLogout']),
      async getEv(valor=''){
        const {data} = await api.get(`efetivovariavel/?search=${valor}`)
        this.evs = data
      },
      getComNovoValor(novoValor){
        this.getEv(novoValor)
        console.log(novoValor)
      },
      abrirModalAction(evFichaID){
        this.modalAberto = true
        this.idFichaEvSelecionado = evFichaID
      },
      fecharModalAction(){
        this.modalAberto = false
      }
    }
}
</script>

<style scoped>
.main{
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 30px;
  gap: 10px;
}
</style>