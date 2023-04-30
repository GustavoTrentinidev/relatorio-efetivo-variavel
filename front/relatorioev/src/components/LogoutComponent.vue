<template>
    <div class="logout">
        <div class="user-info">
            <img class="icon" src="@/assets/account.png" alt="">
            <div>{{aplicador_dados.grau_hieq}} {{aplicador_dados.nome_guerra}}</div>
        </div>
        <div class="sair" @click="logout">Sair</div>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'
import { mapState } from 'vuex'
export default {
    computed:{
        ...mapState('aplicador', ['aplicador_dados'])
    },
    methods:{
        ...mapMutations('auth', ['setLogout']),
        logout(){
            this.setLogout()
            this.$router.push('/auth')
        }
    }
}
</script>

<style scoped>
.logout{
    width: fit-content;
    height: 50px;
    position: absolute;
    top: 5px;
    right: 5px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-end;
}
.user-info{
    display: flex;
    gap: 5px;
    align-items: center;
}
.icon{
    height: 20px;
    width: 20px;
}
.sair{
    cursor: pointer;
}
@media only screen and (min-device-width: 390px) and (max-device-width: 844px) {
    .logout{
        bottom: 0;
        top: initial;
    }
}
</style>