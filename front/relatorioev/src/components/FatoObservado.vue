<template>
  <div>
    <div class="fator">
        Fator: {{fo.fator}}
    </div>
    <div class="motivo">
        Motivo: {{fo.motivo}}
    </div>
    <div v-if="fo.data" class="data">
        Data: {{fo.data.split('-').reverse().join('/')}}
    </div>
    <div class="descricao">
        <div class="descricao-label">
            Descricao 
        </div>
        <div class="descricao-texto">
            {{fo.descricao}}
        </div>
    </div>
    <div class="aplicador">
        <div>Aplicado por: {{fo.aplicador.grau_hieq}} {{fo.aplicador.nome_guerra}}</div>
        <div>{{fo.aplicador.om}}</div>
    </div>
  </div>
</template>

<script>
import { api } from '@/plugins/axios'
export default {
    props: ['id'],
    data(){
        return{
            fo: {}
        }
    },
    methods:{
        async getFO(){
            const { data } = await api.get(`fo/${this.id}`)
            this.fo = data
        }
    },
    mounted(){
        this.getFO()
    }
}
</script>

<style>
.descricao{
    border: 2px solid #504b4b;
    border-radius: 5px;
    padding: 8px;
    align-self: center;
    width: 90%;
    margin: 10px;
    height: fit-content;
    position: relative;
}
.descricao-label{
    position: absolute;
    top: -10px;
    left: 10px;
    font-weight: bold;
    background-color: #fff;
}
.aplicador{
    position: absolute;
    top: 0;
    right: 5px;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}

@media only screen and (min-device-width: 390px) and (max-device-width: 844px) {
    .aplicador{
        position: initial;
    }
}
</style>