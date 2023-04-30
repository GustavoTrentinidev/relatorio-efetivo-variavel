<template>
  <div class="main">
    <LoginComponentVue v-if="possuiCadastro" @naoPossuiCadastro="trocaPossuiCadastroParaFalse"/>
    <RegisterComponentVue v-else @possuiCadastro="trocaPossuiCadastroParaTrue"/>
  </div>
</template>

<script>
import LoginComponentVue from "../components/LoginComponent.vue";
import RegisterComponentVue from "../components/RegisterComponent.vue";
export default {
  components: {LoginComponentVue, RegisterComponentVue},
  data(){
    return{
      possuiCadastro: true,
    }
  },
  methods:{
    trocaPossuiCadastroParaFalse(){
      this.possuiCadastro = false
    },
    trocaPossuiCadastroParaTrue(){
      this.possuiCadastro = true
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