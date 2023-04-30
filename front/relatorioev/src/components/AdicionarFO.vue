<template>
    <div class="add-fo">
        <div class="form-add-fo" v-show="addFO">
            <div class="add-title">Adicione um Fato Observado</div>
            <div class="inputs-cima">
                <div class="field">
                    <div class="label">Fator</div>
                    <select class="fator-input" v-model="fo.fator">
                        <option value="Positivo">Positivo</option>
                        <option value="Negativo">Negativo</option>
                    </select>
                </div>
                <div class="field motivo">
                    <div class="label">Motivo</div>
                    <input type="text" v-model="fo.motivo" class="motivo-input" placeholder="Motivo">
                </div>
            </div>
            <div class="field desc">
                <div class="label">Descrição</div>
                <input type="text" v-model="fo.descricao" class="desc-input" placeholder="Descrição">
            </div>
        </div>
        <div class="fo-action-btns">
            <div class="add-btn" v-if="!addFO" @click="addFO = true">Adicionar FO</div>
            <div class="add-btn cadastrar-btn" v-if="addFO" @click="cadastrar">Cadastrar FO</div>
            <div class="add-btn cancel-btn" @click="cancelar" v-if="addFO">Cancelar</div>
        </div>
    </div>
</template>

<script>
import { api } from "@/plugins/axios"
import { mapState } from 'vuex'
export default {
    watch:{
        fichaID(){
            this.fo.ficha = this.fichaID
        }
    },
    computed: {
        ...mapState('aplicador', ['aplicador_dados']),
    },
    mounted(){
        this.fo.aplicador = this.aplicador_dados.id
    },
    props: ['fichaID'],
    data(){
        return{
            addFO: false,
            fo: {
                fator: 'Positivo',
                ficha: this.fichaID,
            },
        }
    },
    methods:{
        cancelar(){
            this.fo = {
                    fator: 'Positivo',
                    ficha: this.fichaID,
                    aplicador: this.aplicador_dados.id
                }
            this.addFO = false
        },
        async cadastrar(){
            await api.post('fo/', this.fo)
            this.$emit('focadastrado')
            this.cancelar()
        }
    }

}
</script>

<style scoped>
.add-fo{
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 80%;
    margin: 15px;
}
.add-btn{
    background-color: #33b249;
    color: #fff;
    font-size: 1rem;
    border-radius: 3px;
    padding: 5px;
    margin: 15px 0 15px 0;
    cursor: pointer;
}
.fo-action-btns{
    display: flex;
    gap: 15px;
}
.cancel-btn{
    background-color: #336eb2;
}
.cadastrar-btn{
    background-color: #e48203;
    
}
.form-add-fo{
    display: flex; 
    flex-direction: column;
    gap: 15px;
    width: 100%;
}
.add-title{
    font-size: 1.5rem;
    font-family: 'Roboto', sans-serif;
    font-weight: 300;
}
.field{
    position: relative;
}
.label{
    position: absolute;
    top: -10px;
    left: 15px;
    font-size: 1.2rem;
    font-weight: bold;
    background-color: #fff;
}
.inputs-cima{
    display: flex;
    gap: 15px;
}
.fator-input, .motivo-input, .desc-input {
    outline: 0;
    padding: 10px;
    font-size: 1rem;
}
.motivo, .motivo-input{
    width: calc(100% - 30px);
}
.desc, .desc-input{
    width: calc(100% - 15px);
}
@media only screen and (min-device-width: 390px) and (max-device-width: 844px) {
    .inputs-cima{
        flex-direction: column;
    }
    .motivo-input{
        width: calc(100% - 15px);
    }
}
</style>