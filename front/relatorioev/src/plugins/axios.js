import axios from "axios"
import store from "@/store"


axios.defaults.baseURL = "https://backend-newslayers-production.up.railway.app/"

export const api = axios.create({
    baseURL: "http://127.0.0.1:8000/"
})

const tokenChange = (token = store.state.auth.userAccess.access) => {
    if (token){
        api.defaults.headers.common["Authorization"] = `Bearer ${token}`
    }
    console.log(api.defaults.headers.common["Authorization"])
}
const cleanToken = () =>{
    api.defaults.headers.common["Authorization"] = ''
}



export {tokenChange, cleanToken}