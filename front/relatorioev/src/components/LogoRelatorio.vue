<template>
  <div class="logo-row">
        <img class="logo-img" src="../assets/logo62bi.png"/>
        <div class="logo-text">
        Relatório Efetivo Variável 62° BI
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.logo-row{
  display: flex;
  gap: 20px;
  justify-content: space-around;
  align-items: center;
  box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
  border-radius: 5px;
  padding: 5px;
  width: 50%;
}
.logo-img{
  width: 60px;
}
.logo-text{
  font-size: 3rem;
  font-family: 'Roboto', sans-serif;
  font-weight: 400;
}
@media  screen and (max-width: 1366px) {
    .logo-text{
      font-size: 2.3rem;
    }
}

@media only screen and (min-device-width: 390px) and (max-device-width: 844px) {
    .logo-row{
      width: 80%;
    }
    .logo-text{
      font-size: 1.5rem;
    }
    .logo-img{
      width: 50px;
    }
}
</style>