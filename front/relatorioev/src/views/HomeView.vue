<template>
    <div class="main">
      <LogoRelatorioVue/>
      <InputPesquisa/>
        {{ficha}}
    </div>
</template>

<script>
import { api } from "@/plugins/axios"
import LogoRelatorioVue from '../components/LogoRelatorio.vue'
import InputPesquisa from '../components/InputPesquisa.vue'
export default {
    components: {LogoRelatorioVue, InputPesquisa},
    data(){
      return {
        ficha: ''
      }
    },
    mounted(){
      this.getFicha()
    },
    methods: {
      async getFicha(){
        const {data} = await api.get('ficha')
        this.ficha = data
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