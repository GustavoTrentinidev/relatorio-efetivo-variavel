<template>
  <div>
    <div class="main">
      <InputPesquisa @mudarValorBusca="getComNovoValor"/>
      <EvResultado :efetivos="evs" @botaoClicado="abrirModalAction"/>
    </div>
    <PopUpEv :modalAberto="modalAberto" @fecharModal="fecharModalAction" :evFichaID="idFichaEvSelecionado"/>
    <LogoutComponent/>
  </div>
</template>

<script>
import { api } from "@/plugins/axios"
import InputPesquisa from '../components/InputPesquisa.vue'
import EvResultado from '../components/EvResultado.vue'
import PopUpEv from '../components/PopUpEv.vue'
import LogoutComponent from '../components/LogoutComponent.vue'


export default {
    components: {InputPesquisa, EvResultado, PopUpEv, LogoutComponent},
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