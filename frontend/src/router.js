import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from './components/Dashboard.vue';
import ChatView from './components/ChatView.vue';
import ChatHistoryView from './components/ChatHistoryView.vue';

const routes = [
  { path: '/', component: Dashboard }, 
  { path: '/chat', name: 'ChatView', component: ChatView },
  { path: '/chat/history', component: ChatHistoryView },  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.name === 'ChatView') {
    document.body.classList.add('no-scroll');
  } else {
    document.body.classList.remove('no-scroll');
    document.body.classList.add('dash-no-scroll');
  }
  next();
});

export default router;
