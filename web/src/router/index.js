import Vue from "vue";
import Router from "vue-router";
import Books from "../views/Books"
import Home from "../views/Home"

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home
    },
    {
      path: "/books",
      name: "Books",
      component: Books
    }
  ]
});
