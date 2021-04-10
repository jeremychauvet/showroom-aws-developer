<template>
  <div class="books">

    <div class="container">
      <h2>Books</h2>

      <div class="alert alert-info" role="alert" v-if="books === null">
        Loading
      </div>

      <div class="alert alert-danger" role="alert" v-if="books === null && error != null">
        No books available.
      </div>
      <div class="row" v-else>
        <div class="col-md-4 mb-4" v-for="book in books" :key="book.message" >
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">{{ book.BookTitle }}</h5>
              <h6 class="card-subtitle mb-2 text-muted">{{ book.BookAuthor }}</h6>
              <p class="card-text">Stock : {{ book.BookStock }} - ISBN : {{ book.ISBN }}</p>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import { api } from '../api';

export default {
  name: 'Books',
  data () {
    return {
      books: null,
      error: null
    }
  },
  mounted () {
    api.get('/book/display')
    .then(response => {
      this.books = response.data
    })
    .catch(e => {
      this.error = e
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
