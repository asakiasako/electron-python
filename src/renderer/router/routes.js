import MainView from '@/components/MainView.vue'

const routes = [
  {
    name: 'main',
    path: '/',
    component: MainView
  },
  {
    path: '*',
    redirect: '/'
  }
]

export default routes
