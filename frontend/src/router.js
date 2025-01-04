import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from './components/Dashboard.vue';
import ChatView from './components/ChatView.vue';

const routes = [
  { path: '/', component: Dashboard }, 
  { path: '/chat', component: ChatView },  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
