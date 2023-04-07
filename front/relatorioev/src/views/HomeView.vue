<template>
    <div class="main">
      <LogoRelatorioVue/>
      <InputPesquisa @mudarValorBusca="getComNovoValor"/>
      <EvResultado :efetivos="evs"/>
    </div>
</template>

<script>
import { api } from "@/plugins/axios"
import LogoRelatorioVue from '../components/LogoRelatorio.vue'
import InputPesquisa from '../components/InputPesquisa.vue'
import EvResultado from '../components/EvResultado.vue'
export default {
    components: {LogoRelatorioVue, InputPesquisa, EvResultado},
    data(){
      return {
        evs: []
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