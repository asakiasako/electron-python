import Init from '@/components/Init.vue'
import MainView from '@/components/MainView.vue'

const routes = [
  {
    name: 'entry',
    path: '/',
    redirect: {name: 'init'}
  },
  {
    name: 'init',
    path: '/init',
    component: Init
  },
  {
    name: 'main',
    path: '/main',
    component: MainView
  },
  {
    path: '*',
    redirect: '/'
  }
]

export default routes
