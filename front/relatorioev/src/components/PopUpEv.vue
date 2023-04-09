<template>
  <div v-show="modalAberto" @click="fecharModal($event)" class="overlay">
    <div class="content">
        <img class="close" @click="$emit('fecharModal')" src="../assets/close.png"/>
        <div class="ficha-header">
            <img class="logo-img" src="../assets/logo62bi.png"/>
            <div class="header-text-info" v-if="ficha.ev">Ficha {{ficha.ev.grau_hieq}} {{ficha.ev.nome_guerra}}</div>
            <div class="image-ev" v-if="ficha.ev" :style="'background-image: url(' + ficha.ev.foto + ')'"></div>
        </div>
        <div v-if="ficha.ev" class="ficha-info">
            <div class="titulo-secao">
                Dados do Militar:
            </div>
            <div class="row">
                <div class="nome-guerra text-field row-text-field">
                    <div class="label">Nome de Guerra</div>
                    <div>{{ficha.ev.nome_guerra}}</div>
                </div>
                <div class="text-field row-text-field">
                    <div class="label">Número</div>
                    <div class="numero-ev">{{ficha.ev.numero}}</div>
                </div>
            </div>
            <div class="nome-completo text-field">
                <div class="label">Nome Completo</div>
                <div>{{ficha.ev.nome_completo}}</div>
            </div>
            <div class="row">
                <div class="text-field row-text-field">
                    <div class="label">Nome da Mãe</div>
                    <div>{{ficha.ev.nome_mae}}</div>
                </div>
                <div class="text-field row-text-field">
                    <div class="label">Nome do Pai</div>
                    <div>{{ficha.ev.nome_pai}}</div>
                </div>
            </div>
            <div class="row">
                <div class="text-field row-text-field">
                    <div class="label">Local de Nascimento</div>
                    <div>{{ficha.ev.local_nascimento}}</div>
                </div>
                <div class="text-field row-text-field">
                    <div class="label">Data de Nascimento</div>
                    <div>ESSE DADO AINDA NAO EXISTE</div>
                </div>
            </div>
            <div class="row">
                <div class="text-field row-text-field">
                    <div class="label">Subunidade</div>
                    <div>{{ficha.ev.om}}</div>
                </div>
                <div class="text-field row-text-field">
                    <div class="label">Grau Hierárquico</div>
                    <div v-if="ficha.ev">{{ficha.ev.grau_hieq}}</div>
                </div>
            </div>
            <div class="row">
                <div class="text-field row-text-field">
                    <div class="label">CPF</div>
                    <div>{{cpf}}</div>
                </div>
                <div class="text-field row-text-field">
                    <div class="label">Tipo Sanguíneo</div>
                    <div>{{ficha.ev.tipo_sanguineo}}</div>
                </div>
            </div>
            <div class="titulo-secao">
                Fatos Observados:
            </div>
            <div class="fato-observado" v-for="fo in ficha.fo" :key="fo.id">
                <FatoObservado :id="fo.id"/>
            </div>
                <AdicionarFO :fichaID="ficha.id"/>
        </div>
    </div>
  </div>
</template>

<script>
import { api } from '@/plugins/axios'
import FatoObservado from '@/components/FatoObservado.vue' 
import AdicionarFO from '@/components/AdicionarFO.vue' 
export default {
    components: {FatoObservado, AdicionarFO},
    data(){
        return{
            ficha: {},
            cpf: '',
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
            this.formatCPF()
        },
        formatCPF(){
            this.cpf = ''
            let cpfCru = this.ficha.ev.cpf
            let cpfFormatado = ''
            for(let i = 0; i < cpfCru.length; i++){
                if(i%3 == 0 && i != 0 && i != 9){
                    cpfFormatado += '.' + cpfCru[i]
                }else if(i==9){
                    cpfFormatado += '-' + cpfCru[i]
                }
                else{
                    cpfFormatado += cpfCru[i]
                }
            }
            this.cpf = cpfFormatado
        }
    },
    watch: {
        modalAberto(){
            if(this.modalAberto){
                this.getFichaEvSelecionado()
            }
        }
    },



    // RETIRAR DEPOIS!!!!!
    mounted(){
        this.getFichaEvSelecionado()
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
.ficha-info{
    padding-top: 25px;
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    align-items: center;
}
.titulo-secao{
    align-self: flex-start;
    font-weight: 300;
    font-size: 1.5rem;
    font-family: 'Roboto', sans-serif;
}
.row{
    display: flex;
    width: 100%;
    justify-content: space-around;
    margin-top: 15px;
}
.titulo-secao:not(:first-child){
    margin-top: 15px;
}
.text-field{
    position: relative;
    display: flex;
    border: 2px solid #dfdfdf;
    border-radius: 2px;
    padding: 8px;
    width: 95%;
    margin-top: 15px;
    align-items: center;
}
.row-text-field{
    width: 45%;
    margin-top: 0;
}
.label{
    position: absolute;
    top: -12px;
    left: 15px;
    background-color: #fff;
    font-weight: bolder;
}
.fato-observado{
    border: #dfdfdf 2px solid;
    border-radius: 2px;
    width: 95%;
    padding: 8px;
    margin-top: 15px;
    display: flex;
    flex-direction: column;
    position: relative;
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
    .text-field, .fato-observado {
        width: 91%;
    }
    .row{
        flex-direction: column;
        gap: 15px;
    }
    .row-text-field{
        width: initial;
    }
    .ficha-info::-webkit-scrollbar{
        display: none;
    }
}
</style>