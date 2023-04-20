<template>
  <div class="fatd">
    <div class="fatd-property">
      Punição: <div class="punicao">{{fatd.punicao}}</div> 
    </div>
    <div class="fatd-property-date">
      Data: {{fatd.data.split('-').reverse().join('/')}}
    </div>
    <div class="fatd-property-desc">
      <div class="label-desc">Descrição</div>
      <div class="text-desc">{{fatd.descricao}}</div>
    </div>
    <div class="fatd-aplicator">
      Aplicado por: {{fatd.aplicador.grau_hieq}} {{fatd.aplicador.nome_guerra}}
      <div>{{fatd.aplicador.om}}</div>
    </div>
  </div>
</template>

<script>
import { api } from "@/plugins/axios"
export default {
  props: ["id"],
  data(){
    return {
      fatd: {}
    }
  },
  methods: {
    async getFATD(){
      const { data } = await api.get(`/fatd/${this.id}`)
      this.fatd = data
      console.log(this.fatd)
    }
  },
  mounted(){
    this.getFATD()
  }
}
</script>

<style scoped> 
.fatd{
  display: flex;
  flex-direction: column;
  position: relative;
}
.fatd-property{
  display: flex;
  gap: 5px;
  align-items: center;
}
.punicao{
  font-weight: bold;
  font-size: 1.2rem;
  color: red;
}
.fatd-property-desc{
  margin: 10px;
  border: 2px solid #504b4b;
  padding: 8px;
  border-radius: 5px;
  position: relative;
}
.label-desc{
  position: absolute;
  top: -10px;
  left: 10px;
  font-weight: bold;
  background-color: #fff;
}
.text-desc{
  font-weight: 500;
}
.fatd-aplicator{
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: center;
  position: absolute;
  right: 0;
}
@media only screen and (min-device-width: 390px) and (max-device-width: 844px) {
    .fatd-aplicator{
        position: initial;
    }
}
</style>