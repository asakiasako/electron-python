import Vue from 'vue'
import router from './router'
import store from './store'
import VueElectron from 'vue-electron'
import ElementUI from 'element-ui'
import './styles/element-theme.scss'
import './styles/global.scss'
import locale from 'element-ui/lib/locale/lang/en'
import AppRoot from '@/App'
import appState from './app-state'
import {rpcClient} from '@/rpc-client'

if (!process.env.IS_WEB) Vue.use(require('vue-electron'))
Vue.config.productionTip = false

Vue.use(VueElectron)
Vue.use(ElementUI, { size: 'medium', locale })

/* bind constants to Vue */
let bus = new Vue()
Vue.prototype.bus = bus
Vue.prototype.appState = appState
Vue.prototype.rpcClient = rpcClient

/* mount Vue instance to DOM */
/* eslint-disable no-new */
new Vue({
  el: '#app',
  template: '<app-root></app-root>',
  components: { 'app-root': AppRoot },
  router,
  store
})
