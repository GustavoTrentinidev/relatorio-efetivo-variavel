<template>
    <div class="input-row">
        <input class="entrada-ev" v-model="busca_ev" type="text" placeholder="Busque por um EV">
        <div class="icon-pesquisa-holder">
            <img class="icon-pesquisa" src="../assets/search.png" alt="">
        </div>
    </div>
</template>

<script>
export default {
  watch:{
    busca_ev(){
      this.emitirBusca()
    }
  },
  data(){
    return{
      busca_ev: ''
    }
  },
  methods: {
    emitirBusca(){
      this.$emit('mudarValorBusca', this.busca_ev)
    }
  }
}
</script>

<style scoped>

.input-row{
  display: flex;
  align-items: center;
  gap: 10px;
  width: 30%;
}
.icon-pesquisa-holder{
  display: flex;
  align-items: center;
  justify-content: center;
  height: 30px;
  min-width: 30px;
  box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
  cursor: pointer;
  border-radius: 5px;
}
.icon-pesquisa{
  max-height: 20px;
}
.entrada-ev{
  border: 0;
  outline: 0;
  box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
  width: 100%;
  height: 30px;
  padding: 5px;
  font-size: 1.2rem;
}
@media only screen and (min-device-width: 390px) and (max-device-width: 844px) {

  .input-row{
    width: 85%;
  }

}
</style>