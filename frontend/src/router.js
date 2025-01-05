import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from './components/Dashboard.vue';
import ChatView from './components/ChatView.vue';
import ChatHistoryView from './components/ChatHistoryView.vue';

const routes = [
  { path: '/', component: Dashboard }, 
  { path: '/chat', component: ChatView },
  { path: '/chat/history', component: ChatHistoryView },  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
