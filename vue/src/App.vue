<template>
  <body class="hold-transition sidebar-mini layout-fixed">
    <div class="wrapper">
    <HeaderContent v-if="usuarioAuth"></HeaderContent>
    <SidebarContent v-if="usuarioAuth" :nombreUsuario="nombreUsuario" :tipoUsuario="tipoUsuario"></SidebarContent>
      <div class="content-wrapper" v-if="usuarioAuth">
          <div class="content">
            <div class="container-fluid">
              <router-view :nombreUsuario="nombreUsuario" :idUsuario="idUsuario"></router-view>
            </div>
          </div>
      </div>
    <FooterContent v-if="usuarioAuth"></FooterContent>
    <div class="hold-transition login-page" v-else >
    <div class="login-box" @keyup.enter="login()">
        <!-- /.login-logo -->
        <div class="card card-outline card-primary">
          <div class="card-header text-center">
            <p class="h1 m-2"><b>Ventas</b>PRO</p>
          </div>
          <div class="card-body">
            <p class="login-box-msg">Ingrese sus credenciales</p>

            
              <div class="input-group mb-3">
                <input type="email" class="form-control" placeholder="Email" v-model="usuario">
                <div class="input-group-append">
                  <div class="input-group-text">
                    <span class="fas fa-envelope"></span>
                  </div>
                </div>
              </div>
              <div class="input-group mb-3">
                <input type="password" class="form-control" placeholder="Password" v-model="password">
                <div class="input-group-append">
                  <div class="input-group-text">
                    <span class="fas fa-lock"></span>
                  </div>
                </div>
              </div>
              <div class="row">
                <!-- /.col -->
                <div class="col-12">
                  <button type="button" @click="login()" class="btn btn-primary btn-block">Ingresar</button>
                </div>
                <!-- /.col -->
              </div>
            
          </div>
          <!-- /.card-body -->
        </div>
        <!-- /.card -->
      </div>
      <!-- /.login-box -->
      </div>

  </div>
</body>
</template>

<script>
import HeaderContent from './adminlte/HeaderContent.vue'
import SidebarContent from './adminlte/SidebarContent.vue'
import FooterContent from './adminlte/FooterContent.vue'
import jwt_decode from 'jwt-decode'

export default {
  name: 'App',
  components:{
        HeaderContent,
        SidebarContent,
        FooterContent,
  },
  data(){
    return{
      usuarioAuth: localStorage.getItem('authToken') ? true : false,
      usuario:'',
      password:'',
      hayError:false,
      arrayError:[],
      nombreUsuario:'',
      tipoUsuario:'',
    }
  },
  created(){
    this.getNombreUsuario()
  },
  methods:{
    validar(){
      this.hayError = false
      this.arrayError=[]
      if(this.password == ''){this.arrayError.push('La clave no puede estar vacio')}
      if(this.usuario == ''){this.arrayError.push('El usuario no puede estar vacio')}
      if(this.arrayError.length){
        this.hayError = true
      }
      return this.hayError
    },
    async login(){
      if(this.validar()){
        this.arrayError.forEach(element => {
          this.$toastr.error(element,'Atencion!')
        });
        return
      }
      try{
        let me = this
        const response = await me.$axios.post(`${process.env.VUE_APP_API_URL}/api/token/`,{
          username: me.usuario,
          password: me.password
        })
        const token =  response.data.access
        localStorage.setItem('authToken', token)
        console.log(token)
        
        this.usuarioAuth = true
        //this.$router.push('/dashboard');
        
        window.location.href = 'http://localhost:8080/dashboard'
      }
      catch(error){
        console.error('error al uniciar session')
        this.$toastr.error('Error al iniciar session', 'Error!')
      }
     
    },
    getNombreUsuario(){
      const token = localStorage.getItem('authToken')
      if(token){
        try{
          const payload = jwt_decode(token)
          console.log(payload)
          this.nombreUsuario = payload.username
          this.tipoUsuario = payload.grupo_id
          this.idUsuario = payload.user_id
        }
        catch(error){
          console.log('error al decodificar', error)
        }
        
      }
    },
   
  },
  mounted() {
    let inactivityTimer = null;
    let me = this
    function resetInactivityTimer() {
      clearTimeout(inactivityTimer);
      inactivityTimer = setTimeout(() => {
        // Redirige al usuario al login después de 10 segundos de inactividad.
        //router.push('/login');
        localStorage.removeItem('authToken')
        me.usuarioAuth = false
        //window.location.href = 'http://localhost:8080/'
        
      }, 18000000); // 18000000 milisegundos = 5 horas
    }

    resetInactivityTimer();

    // Agrega escuchadores de eventos para restablecer el temporizador cuando el usuario interactúa.
    window.addEventListener('mousemove', resetInactivityTimer);
    window.addEventListener('keydown', resetInactivityTimer);
  },
}
</script>

<style>

</style>
