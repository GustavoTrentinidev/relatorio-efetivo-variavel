<template>
  <div class="auth-container">
      <div class="auth-title">Autentique-se no sistema</div>
      <div class="auth-form">
        <div class="form-title">Login</div>
        <div class="form-field">
          <div class="input-label">Nome de usuário</div>
          <input class="form-input" v-model="loginUser.username" type="text">
        </div>
        <div class="form-field password">
          <div>Senha</div>
          <input class="form-input" @keydown.enter="tryLogin" v-model="loginUser.password" :type="showPassword ? 'text' : 'password'">
          <img class="eye-icon" v-if="!showPassword" src="@/assets/eye.png" @click="showPassword = !showPassword" alt="">
          <img class="eye-icon" v-else src="@/assets/eye-off.png" @click="showPassword = !showPassword" alt="">
        </div>
        <div class="error" v-if="error.active" >{{error.message}}</div>
        <button class="form-btn" @click="tryLogin">Autenticar</button>
      </div>
      <div class="question">Não possui cadastro? Cadastre-se <strong style="cursor: pointer;" @click="trocarComponente">aqui</strong></div>
    </div>
</template>

<script>
// import { api } from "@/plugins/axios"
import { mapActions } from "vuex"


export default {
  computed: {
  },
  data(){
    return{
      error: {
        active: false,
        message: ''
      },
      loginUser: {},
      showPassword: false,
    }
  },
  methods: {
    ...mapActions('auth', ['loginStore']),
    trocarComponente(){
        this.$emit("naoPossuiCadastro")
    },
    async tryLogin(){
      if (!this.loginUser.username || !this.loginUser.password){
        this.error = {
          message: 'Preencha os campos requisitados.',
          active: true,
        }
      }else {
        this.error.active = false
        this.loginStore(this.loginUser).then().catch(e=>{
          this.error = {
            message: e.response.data.detail,
            active: true,
          }
        })
      }
    }
  }
}
</script>

<style scoped>
.auth-container{
  width: 35%;
  height: 400px;
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
.password{
  position: relative;
}
.eye-icon{
  position: absolute;
  top: 50%;
  right: 15px;
  width: 20px;
  cursor: pointer;
}
@media only screen and (min-device-width: 390px) and (max-device-width: 844px) {
    .auth-container{
      width: 80%;
      height: 500px;
    }
    .auth-form{
      width: 100%;
    }
}
</style>