<template>
    <!-- Content Header (Page header) -->
    <div class="content-header">
    <div class="container-fluid">
      <div class="row mb-2">
        <div class="col-sm-8">
          <h1 class="m-0"><router-link to="/ventas"><i class="fas fa-caret-square-left text-secondary"></i></router-link> Detalle venta 
          </h1>
          
        </div><!-- /.col -->
        <div class="col-sm-4">
          <ol class="breadcrumb float-sm-right">
            <li class="breadcrumb-item"><router-link :to="{ name:'dashboard'}">Home</router-link></li>
            <li class="breadcrumb-item active">Detalle</li>
          </ol>
        </div><!-- /.col -->
      </div><!-- /.row -->
    </div><!-- /.container-fluid -->
  </div>
  <!-- /.content-header -->

  <div class="card card-primary card-outline">
      <div class="card-body">
        <div class="row">
          <div class="col-md-12">
            <h2>{{ serie }} <span v-if="ventactivo==false" class="badge badge-danger">ANULADO</span> <span style="font-size: 15pt;">{{ motivo }}</span></h2>
          </div>
        </div>
          <div class="row">
              <div class="col-sm-7">
                <div class="card">
                    <div class="card-header bg-primary">
                        Detalle de venta
                    </div>
              
                <div class="card-body">
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
                        <input type="text" class="form-control form-control-md bg-white" readonly :value="serie" :class="{'is-valid':serie}">
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
                    </div><br>
                    <div class="row">
                      <div class="col-md-3">
                        Moneda
                        <input type="text" class="form-control form-control-lg text-md-left" readonly :value="moneda">
                      </div>
                      <div class="col-md-3">
                        Subtotal
                        <input type="text" class="form-control form-control-lg  text-md-left" readonly :value="subtotal">
                      </div>
                      <div class="col-md-3">
                        IGV
                        <input type="text" class="form-control form-control-lg text-md-left" readonly :value="igv_total">
                      </div>
                        <div class="col-md-3">
                          IMPORTE TOTAL
                          <input type="text" class="form-control form-control-lg bg-white text-md-left" readonly :value="formattedTotal(sumaTotal)">
                        </div>
                    </div>
                    <br>
                    <div class="row">
                      <div class="col-md-6">
                        <p>Metodo pago: {{ metodoPago }}</p>
                      </div>
                      <div class="col-md-6">
                        <p class="text-right">Fecha de venta: {{ fechaFormateada(fecha) }}</p>
                      </div>                      
                    </div>
                    <div class="row">
                      <div class="col-md-6">
                        <button v-if="ventactivo==false" class="btn btn-secondary ">Anulado</button>
                        <button v-else class="btn btn-danger " @click="anularVenta()">Anular Venta</button>
                      </div>
                      <div class="col-md-6 text-right">
                          <div>
                          <button class="btn btn-success btn-flat" @click="imprimir()">Imprimir</button></div>
                        </div>
                    </div>
                </div>
            </div>
              </div>
              <div class="col-sm-5">
                <div class="card">
                    <div class="card-header bg-info">
                        Datos de pedido
                    </div>
                <div class="card-body">
                <div class="input-group mb-4" >
                    <div class="input-group-append">
                          <button type="submit" class="btn btn-md btn-default">
                              Fecha de pedido &nbsp;&nbsp;
                          </button>
                    </div>
                    <input type="date" v-model="fechaPedido" class="form-control form-control-md bg-white" disabled>
                  </div>
                  <div class="input-group" >
                    <div class="input-group-append">
                          <button type="submit" class="btn btn-md btn-default">
                              Número de pedido
                          </button>
                    </div>
                    <input type="number" v-model="numPedido" class="form-control form-control-md bg-white" disabled>
                  </div><br>
                <div class="form-group">
                    <label for="exampleInputEmail1">Cliente:</label>
                    <input type="text" class="form-control bg-white" :class="cliente?'is-valid':''" :value="cliente" disabled>
                </div>
                <div class="form-group">
                    <label for="exampleInputEmail1">Vendedor:</label>
                    <input type="text" class="form-control bg-white" :class="{'is-valid':vendedor}" :value="vendedor" disabled>
                </div>
              </div>
         

            </div>
            </div>
          </div>

      </div>      

  </div><!-- /.card -->

</template>

<script>
    export default{
      props:{
            nombreUsuario:String,
            idUsuario:Number,
        },
      data(){
          return{
            idVenta:'',
            arrayPedido: [],
            arrayDetalle: [],
            cliente:'',
            comprobante:'',
            numPedido:'',
            fechaPedido:'',
            idComprob:'',
            fecha:'',
            serie:'',
            metodoPago:'',
            vendedor:'',
            motivo:'',
            subtotal:'',
            igv_total:'',
            moneda:'',

            numComprobante:'',
            ventactivo:'',
                        
            numBuscar:'',
            fechaBuscar:'',
            
          }
      },
      computed: {
     
        sumaTotal(){
          return Number(this.subtotal) + Number(this.igv_total)
        },
        id(){
            return this.$route.params.id
        }
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
          listarVenta(){
            let me = this
              this.$axios.get(`${process.env.VUE_APP_API_URL}/apiventa/ventas/${me.idVenta}/`)
              .then(function(response){console.log(response.data)
                  if(response.data){
                    me.cliente = response.data.cliente
                    me.idPedido = response.data.idPedido
                    me.comprobante = response.data.comprobanteobservacion
                    me.fechaPedido = response.data.fechaPedido
                    me.fecha = response.data.fecha
                    me.idComprob = response.data.tipComprobante
                    me.metodoPago = response.data.metodoPago
                    me.serie = response.data.serie+'-'+response.data.numComprobante
                    me.vendedor = response.data.vendedor
                    me.ventactivo = response.data.activo
                    me.motivo = response.data.observacion
                    me.numPedido = response.data.numPedido
                    me.comprobante = response.data.comprobante
                    me.subtotal = response.data.subtotal
                    me.igv_total = response.data.igv_total
                    me.moneda = response.data.moneda
                    me.listarDetalle()
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
     
          limpiar(){
            this.cliente=''; this.vendedor=''; this.idPedido=''; this.comprobante=''; this.arrayDetalle=[]; this.numPedido='';this.fechaPedido='';
            this.numComprobante=''; this.ventactivo=''
          },
          limpiarTodo(){
            this.cliente=''; this.vendedor=''; this.idPedido=''; this.comprobante=''; this.arrayDetalle=[];this.numBuscar=''; this.numPedido='';
            this.fechaPedido='';this.numComprobante=''; this.ventactivo=''
          },
          fechaFormateada(fecha) {
        // Separar la fecha en partes (año, mes, día)
          const partes = fecha.split('-');

          // Crear una nueva cadena en el formato deseado
          return `${partes[2]}/${partes[1]}/${partes[0]}`;
        },
       anularVenta(){
        let me = this
          this.$swal.fire({
          title: 'Anular Venta '+ me.serie,
          text: "Describe el motivo",
          icon: 'warning',
          input: 'text',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Si, Anular',
          preConfirm: (motivo)=>{
            me.motivo = motivo
          }
          }).then((result) => {
            if (result.isConfirmed) {
        
              this.$axios.post(`${process.env.VUE_APP_API_URL}/apiventa/ventas/`, { //URL ANULAR PEDIDO
                  idVenta: me.idVenta,
                  motivo: me.motivo,
                  idPedido: me.idPedido
                  //detalles: me.arrayDetalle,
              }).
              then((response)=>{
                console.log(response.data)
                me.listarVenta()
                me.$toastr.success('Venta anulado', 'Excelente!')
              }).
              catch((error)=>{
                console.error(error)
                me.$toastr.error('Error al anular venta', 'Error');
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
        this.idVenta = this.id
        const today = new Date()
        this.fechaBuscar = today.toISOString().split('T')[0];
        this.listarVenta()
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