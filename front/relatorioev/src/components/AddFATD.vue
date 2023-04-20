<template>
    <div class="add-fo">
        <div class="form-add-fo" v-show="addFATD">
            <div class="add-title">Adicione uma FATD</div>
            <div class="inputs-cima">
                <div class="field">
                    <div class="label">Punição</div>
                    <select class="fator-input" v-model="fatd.punicao">
                        <option value="Advertência">Advertência</option>
                        <option value="Repreensão">Repreensão</option>
                        <option value="Detenção">Detenção</option>
                        <option value="Prisão">Prisão</option>
                        <option value="Exclusão a bem da disciplina">Exclusão a bem da disciplina</option>
                    </select>
                </div>
                <div class="field motivo">
                    <div class="label">Descrição</div>
                    <textarea v-model="fatd.descricao" class="motivo-input"> </textarea>
                </div>
            </div>
        </div>
        <div class="fo-action-btns">
            <div class="add-btn" v-if="!addFATD" @click="addFATD = true">Adicionar FATD</div>
            <div class="add-btn cadastrar-btn" v-if="addFATD" @click="addFATD = true">Cadastrar FATD</div>
            <div class="add-btn cancel-btn" @click="cancelar" v-if="addFATD">Cancelar</div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['fichaID'],
    data(){
        return{
            addFATD: false,
            fatd: {
                punicao: 'Advertência',
                ficha: this.fichaID
            },
        }
    },
    methods:{
        cancelar(){
            this.fatd = {
                    punicao: 'Advertência',
                    ficha: this.fichaID
                }
            this.addFATD = false
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
    flex-direction: column;
    gap: 15px;
}
.fator-input, .motivo-input {
    outline: 0;
    padding: 10px;
    font-size: 1rem;
    resize: none;
    font-family: Arial, Helvetica, sans-serif;
}
.motivo, .motivo-input{
    width: calc(100% - 30px);
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