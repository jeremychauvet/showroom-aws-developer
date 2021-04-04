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
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  padding-bottom: 5em;
}

h1, h2 {
  font-family: 'Oswald', sans-serif;
  font-weight: 200 !important;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
