<template>
    <!-- Content Header (Page header) -->
    <div class="content-header">
    <div class="container-fluid">
      <div class="row mb-2">
        <div class="col-sm-6">
          <h1 class="m-0">Caja</h1>
        </div><!-- /.col -->
        <div class="col-sm-6">
          <ol class="breadcrumb float-sm-right">
            <li class="breadcrumb-item"><router-link :to="{ name:'dashboard'}">Home</router-link></li>
            <li class="breadcrumb-item active">Caja</li>
          </ol>
        </div><!-- /.col -->
      </div><!-- /.row -->
    </div><!-- /.container-fluid -->
  </div>
  <!-- /.content-header -->

  <div class="card card-primary card-outline">
      <div class="card-body">
          <div class="row">
            <div class="col-sm-5">
                <div class="card">
                    <div class="card-header bg-info">
                        Buscar Pedido
                    </div>
                <div class="card-body">
                  <div class="row">
                    <div class="col-sm-12">
                      <div class="input-group mb-4" >
                        <div class="input-group-append">
                              <button type="submit" class="btn btn-md btn-default">
                                  Fecha de venta &nbsp;&nbsp;
                              </button>
                        </div>
                        <input type="date" v-model="fechaBuscar" class="form-control form-control-md">
                      </div>
                    </div>
               
                  <div class="col-sm-10">
                    <div class="input-group" v-on:keyup.enter="listarPedido(1,fechaBuscar,numBuscar)">
                      <div class="input-group-append">
                            <button type="submit" class="btn btn-md btn-default">
                                Núm. de venta
                            </button>
                      </div>
                      <input type="number" v-model="numBuscar" class="form-control form-control-md" autofocus>
                      <div class="input-group-append">
                          <button type="submit" class="btn  btn-info" @click="listarPedido(1,fechaBuscar,numBuscar)">
                              <i class="fa fa-search"></i> Buscar
                          </button>
                      </div>
                    </div>
                  </div>
                  <div class="col-sm-2">
                    <button class="btn btn-danger btn-block" @click="limpiarTodo()">Borrar</button>
                  </div>
                  
                  <div class="col-sm-12 mt-3">
                    <div class="form-group">
                      <label for="exampleInputEmail1">Nombre del Cliente:</label>
                      <input type="text" class="form-control bg-white" :class="cliente?'is-valid':''" :value="cliente" disabled>
                    </div>
                  </div>
                <div class="col-sm-12">
                  <div class="form-group">
                    <label for="exampleInputEmail1">N° Documento del Cliente:</label>
                    <input type="text" class="form-control bg-white" :class="cliente_doc?'is-valid':''" :value="cliente_doc" disabled>
                  </div>
                </div>
                <div class="col-sm-12">
                  <div class="form-group">
                      <label for="exampleInputEmail1">Vendedor:</label>
                      <input type="text" class="form-control bg-white" :class="{'is-valid':vendedor}" :value="vendedor" disabled>
                  </div>
                </div>
                </div>
                </div>
                </div>
              </div>
              
              <div class="col-sm-7">
                <div class="card">
                    <div class="card-header bg-primary">
                        Detalle de venta
                    </div>
              
                <div class="card-body">
                  <div class="row">
                    <div class="col-md-6">
                      <h3>Venta: N° {{ numPedido }}</h3>
                    </div>
                    <div class="col-md-6">
                      <h3 v-if="fechaPedido" class="text-right">{{ fechaFormateada(fechaPedido) }}</h3>
                    </div>
                  </div>
                    <div class="input-group mb-4" >
                        <div class="input-group-append">
                            <button type="submit" class="btn btn-md btn-default">
                                Comprobante
                            </button>
                        </div>
                        <input type="text" :class="{'is-valid':comprobante}" :value="comprobante" class="form-control form-control-md bg-white" readonly>
                        <div class="input-group-append">
                            <button type="submit" class="btn btn-md btn-default">
                                Serie N°
                            </button>
                        </div>
                        <input type="text" class="form-control form-control-md bg-white" readonly :value="serie+'-'+numComprobante" :class="{'is-valid':ventactivo}">
                    </div>
                    <div class="table-responsive">
                    <table class="table table-sm table-striped table-bordered">
                        <thead class="bg-warning">
                            <tr>
                                <th>Producto</th>
                                <th>Descripcion</th>
                                <th>Cantidad</th>
                                <th>Precio Uni</th>
                                <th class="text-right">Importe</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="de in arrayDetalle" :key="de.id">
                                <td>{{ de.producto }}</td>
                                <td>{{ de.umVenta }}</td>
                                <td>{{ de.cantidad }}</td>
                                <td>{{ de.precio }}</td>
                                <td class="text-right">{{ formattedTotal(de.cantidad * de.precio) }}</td>
                            </tr>
                        </tbody>
                    </table>
                    </div>
                    <div class="row mt-2">
                        <div class="col-md-3">
                            Moneda
                            <input type="text" class="form-control form-control-lg " readonly :value="moneda">
                        </div>
                        <div class="col-md-3">
                          Sub Total
                            <input type="text" class="form-control form-control-lg " readonly :value="subtotal">
                        </div>
                        <div class="col-md-3">
                          IGV
                          <input type="text" class="form-control form-control-lg " readonly :value="igv_total">
                        </div>
                        <div class="col-md-3">
                          <strong>IMPORTE TOTAL</strong>
                            <input type="text" class="form-control form-control-lg bg-white text-primary" readonly :value="formattedTotal(sumaTotal)">
                        </div>
                        <div class="offset-md-9 col-md-3 text-right mt-3">
                          <button v-if="ventactivo" class="btn btn-secondary btn-lg" >Pagado</button>
                          <button v-else class="btn btn-success btn-lg btn-block" @click="cobrar()"><i class="fas fa-hand-point-up"></i> Cobrar</button>
                        </div>
                    </div>
                    <hr>
                    <div class="row">
                      <div class="offset-md-6 col-md-6 text-right">
                          <div v-if="ventactivo">
                          <button class="btn btn-success btn-flat" @click="imprimir()">Imprimir</button></div>
                        </div>
                    </div>
                </div>
                </div>
              </div>
              
          </div>

      </div>      

  </div><!-- /.card -->

</template>
<script>
    import { ref, onMounted } from 'vue' //sobre fechas
    import { DateTime } from 'luxon' //timezone manejo
    export default{
      setup() {
        const fechaBuscar = ref('');
        onMounted(() => {
          const today = DateTime.now().setZone('America/Lima');
          fechaBuscar.value = today.toISODate();
        });
        return {
          fechaBuscar,
        };
      },
      props:{
            nombreUsuario:String,
            idUsuario:Number,
        },
      data(){
          return{
            idPedido:'',
            arrayPedido: [],
            arrayDetalle: [],
            cliente:'',
            cliente_doc:'',
            usuario:'',
            comprobante:'',
            numPedido:'',
            fechaPedido:'',
            idComprob:'',
            subtotal:'',
            igv_total:'',
            moneda:'',

            numComprobante:'',
            ventactivo:'',
            idVenta:'',
            serie:'',
                        
            numBuscar:'',           
          }
      },
      computed: {
     
        sumaTotal(){
          return Number(this.igv_total) + Number(this.subtotal)
        },
      },
      methods:{
          formattedTotal(amount) {
            return new Intl.NumberFormat('es-PE', {
            style: 'currency',
            currency: 'PEN',
            minimumFractionDigits: 2,
            maximumFractionDigits: 2,
            }).format(amount);
          },
          listarPedido(pageNumber = 1,fechaBuscar, numBuscar){
            if(this.fechaBuscar=='' || this.numBuscar==''){
                this.$toastr.error('Ingrese una fecha y número','Campos vacíos')
                return
            }
              let me = this
              this.$axios.get(`${process.env.VUE_APP_API_URL}/apiventa/pedidos/?page=${pageNumber}&numero=${numBuscar}&fecha=${fechaBuscar}`)
              .then(function(response){
                me.arrayPedido = response.data.results
                  if(me.arrayPedido.length){
                    if(me.arrayPedido[0]['activo']==0){me.$toastr.error('Este pedido esta anulado','Pedido N. '+me.numBuscar);me.limpiar(); return}
                    me.cliente = me.arrayPedido[0]['cliente']
                    me.cliente_doc = me.arrayPedido[0]['cliente_doc']
                    me.vendedor = me.arrayPedido[0]['usuario']
                    me.idPedido = me.arrayPedido[0]['id']
                    me.comprobante = me.arrayPedido[0]['comprobante']
                    me.numPedido = me.arrayPedido[0]['numero']
                    me.fechaPedido = me.arrayPedido[0]['fecha']
                    me.idComprob = me.arrayPedido[0]['idComprob']
                    me.subtotal = me.arrayPedido[0]['subtotal']
                    me.igv_total = me.arrayPedido[0]['igv_total']
                    me.moneda = me.arrayPedido[0]['moneda']
                    me.listarDetalle()
                    me.listarVenta()
                  }else{me.$toastr.info('No se encontraron datos','Sin registro');me.limpiar()}
              })
          },
          
          listarDetalle(){
            let me = this
            this.$axios.get(`${process.env.VUE_APP_API_URL}/apiventa/detalle/?idPedido=${me.idPedido}`)
              .then(function(response){
                  me.arrayDetalle = response.data
              })
          },
          listarVenta(){
            let me = this
            this.$axios.get(`${process.env.VUE_APP_API_URL}/apiventa/caja/?search=${me.idPedido}`)
              .then(function(response){
                  if(response.data && response.data.length > 0){
                    me.ventactivo = response.data[0]['activo']
                    me.numComprobante = response.data[0]['numComprobante']
                    me.serie = response.data[0]['serie']
                    me.idVenta = response.data[0]['id']
                  }else{
                    me.numComprobante=''
                    me.serie='',
                    me.ventactivo=''
                    me.idVenta=''
                  }
              })
          },
          limpiar(){
            this.cliente=''; this.cliente_doc=''; this.vendedor=''; this.idPedido=''; this.comprobante=''; this.arrayDetalle=[]; this.numPedido='';this.fechaPedido='';
            this.numComprobante=''; this.ventactivo='';this.serie='';this.igv_total=0;this.subtotal=0;
          },
          limpiarTodo(){
            this.cliente=''; this.cliente_doc=''; this.vendedor=''; this.idPedido=''; this.comprobante=''; this.arrayDetalle=[];this.numBuscar=''; this.numPedido='';
            this.fechaPedido='';this.numComprobante=''; this.ventactivo=''; this.serie='';this.igv_total=0;this.subtotal=0;
          },
          fechaFormateada(fecha) {
        // Separar la fecha en partes (año, mes, día)
          const partes = fecha.split('-');

          // Crear una nueva cadena en el formato deseado
          return `${partes[2]}/${partes[1]}/${partes[0]}`;
        },
        cobrar(){
          let me = this
          this.$swal.fire({
          title: 'Cobrar venta',
          text: "Esta seguro?",
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Si, Cobrar'
          }).then((result) => {
            if (result.isConfirmed) {
              this.$axios.post(`${process.env.VUE_APP_API_URL}/apiventa/caja/`, { //URL COBRAR VENTA
                  idUsuario: me.idUsuario, //usuario logueado
                  tipComprobante:me.idComprob,
                  observacion:'',
                  idPedido:me.idPedido,
                  metodoPago:'Efectivo',
                  numComprobante:'0',
                  serie:'',
              }).
              then((response)=>{
                console.log(response.data)
                me.listarPedido(1,me.fechaBuscar,me.numBuscar)
                me.$toastr.success('Venta cobrada', 'Excelente!')
                me.$socket.send(JSON.stringify({
                  'message':'nueva venta'
                }))
              }).
              catch((error)=>{
                console.error(error)
                me.$toastr.error('Error al cobrar', 'Error');
              })
            }
          })
        },
        imprimir(){
          window.open(`${process.env.VUE_APP_API_URL}/impresiones/comprobante/` + this.idVenta, '_blank')
        }
      },
          
      watch: {
   
      },
      mounted(){
        
      }
  }
</script>

<style scoped>.modal{
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  overflow: auto;
}
.modal-overlay{
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}
.modal-content{
  width: 40%;
  background-color: white;
  margin-top: 100px;
}
</style>