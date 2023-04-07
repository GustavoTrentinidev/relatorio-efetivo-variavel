<template>
  <div v-show="modalAberto" @click="fecharModal($event)" class="overlay">
    <div class="content"></div>
  </div>
</template>

<script>
export default {
    props: ['modalAberto'],
    methods: {
        fecharModal(e){
            if(e.srcElement == this.$el){
                this.$emit('fecharModal')
            }
        }
    }
}
</script>

<style scoped>
.overlay{
    width: 100%;
    height: 100vh;
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
}
</style>