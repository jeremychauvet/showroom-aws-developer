<template>
  <div>
    <button @click="getBooks">Get books</button>
    <h1 v-if="books"></h1>
    <p class="error" v-if="errorMessage"></p>
  </div>
</template>

<script>
export default {
  name: 'DisplayBooks',
  data () {
    return {
      books: '',
      errors: ''
    }
  },
  methods: {
    getBooks: function () {
      axios.get('/book/display')
        .then(response => {
          this.books = response.data.message
        })
        .catch(e => {
          this.errors = e
        })
    }
  }
}
</script>
