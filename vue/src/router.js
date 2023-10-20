import { createRouter, createWebHistory } from "vue-router";
 
//import Login from './pages/LogiN'
import DashBoard from './pages/DashBoard'
import ProveedoresVue from './pages/mantenedores/ProveedoresVue'
import CategoriasVue from './pages/mantenedores/CategoriasVue'
import ProductosVue from './pages/mantenedores/ProductosVue'
import UnidadMedida from './pages/mantenedores/UnidadMedida'

import EmpresaVue from './pages/empresa/EmpresaVue'
import ComprobanteS from './pages/empresa/ComprobanteS'
import MonedA from './pages/empresa/MonedA'

import CompraS from './pages/inventario/CompraS'
import NuevaCompra from './pages/inventario/NuevaCompra'
import CompraDetalle from './pages/inventario/CompraDetalle'
import AlmaceN from './pages/inventario/AlmaceN'

import Pedidos from './pages/venta/ListarPedido'
import NuevoPedido from './pages/venta/NuevoPedido'
import DetallePedido from './pages/venta/DetallePedido'
import Caja from './pages/venta/CajA'
import Ventas from './pages/venta/VentaS'
import DetalleVenta from './pages/venta/DetalleVenta'

const routes = [
    //{name: 'login', path: '/login', component: Login},
    {name: 'dashboard', path: '/dashboard', component: DashBoard, meta: {requiresAuth:true}},
    {name: 'proveedores', path: '/proveedores', component: ProveedoresVue},
    {name: 'categorias', path: '/categorias', component: CategoriasVue, meta:{requiresAuth:true}},
    {name: 'productos', path: '/productos', component: ProductosVue},
    {name: 'unidadmedida', path: '/unidadmedida', component: UnidadMedida},
    {name: 'configuracion', path: '/configuracion', component:EmpresaVue},
    {name: 'comprobantes', path: '/comprobantes', component:ComprobanteS},
    {name: 'moneda', path: '/moneda', component:MonedA},
    {name: 'compras', path: '/compras', component:CompraS},
    {name: 'nuevacompra', path: '/compras/nuevacompra', component:NuevaCompra},
    {name: 'compradetalle', path: '/compras/detalle/:id', component:CompraDetalle},
    {name: 'almacen', path: '/almacen', component:AlmaceN},
    {name: 'pedidos', path: '/pedidos', component:Pedidos},
    {name: 'nuevopedido', path: '/pedidos/nuevo', component:NuevoPedido},
    {name: 'detallepedido', path: '/pedidos/detalle/:id', component:DetallePedido},
    {name: 'caja', path: '/caja', component:Caja},
    {name: 'ventas', path: '/ventas', component:Ventas},
    {name: 'detalleventa', path: '/ventas/detalle/:id', component:DetalleVenta},
]

const router = createRouter({
    history:createWebHistory(),
    routes:routes
})

export default router