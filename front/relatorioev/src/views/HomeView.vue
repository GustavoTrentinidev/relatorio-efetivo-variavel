<template>
    <div>
        {{ficha}}
    </div>
</template>

<script>
import { api } from "@/plugins/axios"
export default {
    data(){
      return {
        ficha: ''
      }
    },
    mounted(){
      this.getFicha()
    },
    methods: {
      async getFicha(){
        const {data} = await api.get('ficha')
        this.ficha = data
      }
    }
}
</script>
