<template>
  <div id="app">
    <GlobalNav></GlobalNav>
    <router-view />
  </div>
</template>

<script>
import GlobalNav from "./components/GlobalNav";
export default {
  name: "App",
  components: {
    GlobalNav
  }
};
</script>

<style>
#app {
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
