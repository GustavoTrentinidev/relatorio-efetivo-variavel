<template>
  <div class="auth-container">
      <div class="auth-title">Autentique-se no sistema</div>
      <div class="auth-form">
        <div class="form-title">Cadastro</div>
        <div class="form-field">
          <div class="input-label">Nome de usuário</div>
          <input class="form-input" v-model="POST_user.username" type="text">
        </div>
        <div class="form-field">
          <div>Senha</div>
          <input class="form-input" v-model="POST_user.password" type="text">
        </div>
        <div class="form-field">
          <div>Nome completo</div>
          <input class="form-input" v-model="POST_user.nome_completo" type="text">
        </div>
        <div class="form-field">
          <div>Nome de guerra</div>
          <input class="form-input" v-model="POST_user.nome_guerra" type="text">
        </div>
        <div class="form-field">
          <div>Número</div>
          <input class="form-input" v-model="POST_user.numero" type="text">
        </div>
        <div class="form-field">
          <div>Grau Hierárquico</div>
          <input class="form-input" v-model="POST_user.grau_hieq" type="text">
        </div>
        <div class="form-field">
          <div>Subunidade</div>
          <input class="form-input" v-model="POST_user.om" type="text">
        </div>
        <div class="error" v-if="error.active" >{{error.message}}</div>
        <button class="form-btn" @click="tryRegister">Cadastrar</button>
      </div>
      <div class="question">Já possui cadastro? Entre <strong style="cursor: pointer;" @click="trocarComponente">aqui</strong></div>
    </div>
</template>

<script>
import { api } from "@/plugins/axios"
import { mapActions } from "vuex"
export default {
  data(){
    return{
      error: {
        active: false,
        message: ''
      },
      POST_user: {}
    }
  },
  methods: {
    ...mapActions('auth', ['loginStore']),
    trocarComponente(){
        this.$emit("possuiCadastro")
    },
  async tryRegister(){
    this.error = {
      active: false,
      message: ''
    }
    if(!this.POST_user.username || !this.POST_user.password || !this.POST_user.numero || !this.POST_user.nome_completo|| !this.POST_user.nome_guerra || !this.POST_user.grau_hieq || !this.POST_user.om){
        this.error = {
            message: 'Preencha os campos requisitados.',
            active: true,
        }
    }else{
        try{
            await api.post('/aplicador/', this.POST_user)
            this.loginStore({
                username: this.POST_user.username,
                password: this.POST_user.password
              })
        }
        catch(e){
          console.log(e)
          const properties = ['username', 'password', 'numero', 'nome_completo', 'nome_guerra', 'grau_hieq', 'om']
          for(let p of properties){
            if(e.response.data[p]){
              this.error = {
                  message: p + ': ' + e.response.data[p][0],
                  active: true,
              }
            }
          }
        }
      }
    } 
  }
}
</script>

<style scoped>
.auth-container{
  width: 35%;
  height: 700px;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
  box-sizing: border-box;
  padding: 30px;
}
.auth-title{
  font-weight: 300;
  font-family: 'Roboto', sans-serif;
  font-size: 2rem;
}
.auth-form{
  width: 90%;
  display: flex;
  flex-direction: column;
  gap: 15px;
  align-items: center;
}
.form-title{
  margin: 15px 0 0 0;
  font-weight: 300;
  font-family: 'Roboto', sans-serif;
  font-size: 1.7rem;
}
.form-field{
  width: 90%;
}
.form-input{
  width: 100%;
  height: 30px;
  outline: 0;
  padding: 15px;
  box-sizing: border-box;
}
.input-label{
  font-size: 1rem;
}
.form-btn{
  background-color: #fff;
  border: 1px solid black;
  padding: 5px 10px 5px 10px;
  font-size: 1rem;
  cursor: pointer;
  transition: ease-in-out 120ms;
}
.form-btn:hover{
  background-color: rgb(8, 97, 0);
  color: #fff;
  border: 1px solid white;
}
.error{
  font-weight: bold;
  color: #e21818;
}
.auth-container{
  position: relative;
}
.question{
  position: absolute;
  bottom: 5px;
  right: 5px;
}
@media only screen and (min-device-width: 390px) and (max-device-width: 844px) {
    .auth-container{
      width: 80%;
      height: 750px;
    }
    .auth-form{
      width: 100%;
    }
}
</style>