<template>
  <div class="resultados">
    <div class="ev-result" v-for="ev in efetivos" :key="ev.id">
      <div class="dados">
        <div class="image-ev" :style="'background-image: url(' + ev.foto + ')'"></div>
        <div class="texto-dados-ev">
          <div class="nome-ev">
            {{ev.grau_hieq}}
            {{ev.nome_guerra}}
          </div>
          <div class="num-ev">
            {{ev.numero}}
          </div>
          <div class="om-ev">
            {{ev.om}}
          </div>
        </div>
      </div>
      <div class="botao-informacoes" @click="$emit('botaoClicado', ev.ficha)">
        <img class="icon-botao" src="../assets/plus.png"/>
        <div class="texto-botao">Informações</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    props: ['efetivos']
}
</script>

<style scoped>
.resultados{
  width: 50%;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.ev-result{
  display: flex;
  height: 5rem;
  border-radius: 5px;
  box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
  align-items: center;
  padding: 5px 10px 5px 10px;
  gap: 15px;
  justify-content: space-between;
}
.dados{
  display: flex;
  align-items: center;
  gap: 15px;
}
.image-ev{
  border-radius: 3px;
  height: 70px;
  width: 50px;
  background-position: center;
  background-size: cover;
}
.texto-dados-ev{
  display: flex;
  flex-direction: column;
  align-self: flex-start;
  font-size: 1.1rem;
}
.nome-ev{
  margin-top: 6px;
  font-size: 1.3rem;
  color: #00660c;
  font-weight: 800;
}
.botao-informacoes{
  display: flex;
  gap: 10px;
  color: white;
  background-color: #00660c;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
  font-weight: 700;
  font-family: 'Roboto', sans-serif;
}
.icon-botao{
  width: 20px;
}

@media only screen and (min-device-width: 390px) and (max-device-width: 844px) {
  .resultados{
    width: 85%;
  }
  .texto-botao{
    display: none;
  }

}
</style>