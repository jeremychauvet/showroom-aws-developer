<template>
  <div class="books">
    <h1>Books</h1>

    <div>
      {{ info }}
    </div>
  </div>
</template>

<script>
import { api } from '../api';

export default {
  name: 'Books',
  data () {
    return {
      info: null
    }
  },
  mounted () {
    api.get('https://dzhchde09c.execute-api.eu-central-1.amazonaws.com/book/display')
    .then(response => {
      this.info = response
    })
    .catch(e => {
      this.errors.push(e)
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
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
