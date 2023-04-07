<template>
  <div v-show="modalAberto" @click="fecharModal($event)" class="overlay">
    <div class="content">
        <img class="close" @click="$emit('fecharModal')" src="../assets/close.png"/>
        <div class="ficha-header">
            <img class="logo-img" src="../assets/logo62bi.png"/>
            <div class="header-text-info" v-if="ficha.ev">Ficha {{ficha.ev.grau_hieq}} {{ficha.ev.nome_guerra}}</div>
            <div class="image-ev" v-if="ficha.ev" :style="'background-image: url(' + ficha.ev.foto + ')'"></div>
        </div>
        {{ficha}}
    </div>
  </div>
</template>

<script>
import { api } from '@/plugins/axios'
export default {
    data(){
        return{
            ficha: {}
        }
    },
    props: ['modalAberto', 'evFichaID'],
    methods: {
        fecharModal(e){
            if(e.srcElement == this.$el){
                this.$emit('fecharModal')
            }
        },
        async getFichaEvSelecionado(){
            const { data } = await api.get(`ficha/${this.evFichaID}`)
            this.ficha = data
        }
    },
    watch: {
        modalAberto(){
            if(this.modalAberto){
                this.getFichaEvSelecionado()
            }
        }
    }
}
</script>

<style scoped>
.overlay{
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    position: absolute;
    top: 0;
    display: flex;
    align-items: center;
    justify-content: center;
}
.content{
    width: 50%;
    background-color: #fff;
    height: 80%;
    padding: 40px;
    box-sizing: border-box;
    position: relative;
    display: flex;
    flex-direction: column;
    word-break: break-word;
    /* overflow-y: scroll; */
}
.close{
    position: absolute;
    top: 8px;
    right: 8px;
    height: 25px;
    filter: invert(63%) sepia(0%) saturate(3%) hue-rotate(154deg) brightness(84%) contrast(82%);
    cursor: pointer;
}
.ficha-header{
    display: flex;
    height: 80px;
    /* border: 1px solid black; */
    align-items: center;
    gap: 10px;
}
.logo-img{
    max-height: 100%;
}
.header-text-info{
    font-size: 2.5rem;
    font-family: 'Roboto', sans-serif;
}
.image-ev{
    height: 70px;
    border: 1px red solid;
    width: 50px;
}

@media only screen and (min-device-width: 390px) and (max-device-width: 844px) {
    .content{
        width: 80%;
    }
    .header-text-info{
        font-size: 1.2rem;
    }
    .image-ev{
        height: 60px;
    }
}
</style>