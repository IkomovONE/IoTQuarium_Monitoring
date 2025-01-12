import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from './components/Dashboard.vue';
import ChatView from './components/ChatView.vue';
import ChatHistoryView from './components/ChatHistoryView.vue';

const routes = [
  { path: '/', component: Dashboard, meta: { title: 'Dashboard - IoT Quarium' } },
  { path: '/chat', name: 'ChatView', component: ChatView, meta: { title: 'Chat - IoT Quarium' } },
  { path: '/chat/history', component: ChatHistoryView, meta: { title: 'Chat History - IoT Quarium' } },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Update document title dynamically based on the route's meta title
router.beforeEach((to, from, next) => {
  // Set the title if it's defined in the meta field
  if (to.meta.title) {
    document.title = to.meta.title;
  } else {
    document.title = 'IoT Quarium Monitoring'; // Default title
  }

  // Handle scroll classes as per your logic
  if (to.name === 'ChatView') {
    document.body.classList.add('no-scroll');
  } else {
    document.body.classList.remove('no-scroll');
    document.body.classList.add('dash-no-scroll');
  }

  next();
});

export default router;
