<template>
  <div  id="app">
    <div class="main">
      <LogoRelatorio/>
    </div>
    <router-view/>
  </div>
</template>
<script>
import LogoRelatorio from '@/components/LogoRelatorio'

export default {
  components: {LogoRelatorio}
}
</script>

<style scoped>
.main{
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 30px;
  gap: 10px;
}
</style>